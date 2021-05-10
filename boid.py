import pygame
import random
import math



def normalize(vector):
	mag = math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])
	if mag == 0:
		return [0, 0]
	else:
		return [vector[0] / mag, vector[1] / mag]

def clamp(vector, high):
	mag = math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])
	if mag > high:
		v = normalize(vector)
		v[0] = v[0] * high
		v[1] = v[1] * high
		return v
	else:
		return vector

def add(v1, v2):
	return [v1[0] + v2[0], v1[1] + v2[1]]


class Boid():
	maxSpeed = 5
	maxForce = 20

	def __init__(self, x, y, vx, vy, screenWidth, screenHeight, color):
		self.x = x
		self.y = y

		self.vx = vx
		self.vy = vy

		self.ax = 0
		self.ay = 0

		self.forces = []

		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

		self.color = color

		self.sight = 100

		self.separationForce = [0,0]
		self.alignmentForce = [0,0]
		self.cohesionForce = [0,0]

		self.separationWeight = .3 #between .2 - 1
		self.cohesionWeight = 1 #between 0 and .5
		self.alignmentWeight = .5 #between 0 and 1

		self.mass = 5
		



	def draw(self, screen):
		#v = math.sqrt(self.vx * self.vx + self.vy * self.vy)
		#p1Offset = ( 6 * self.vx,  6 * self.vy)
		#p1 = (self.x + p1Offset[0], self.y + p1Offset[1]) 
		#p2Offset = (self.vx - 6 * ((self.vx / self.vy) if self.vy == 0 else 1), self.vy - 6 * ((self.vx / self.vy) if self.vy == 0 else 1))
		#p2 = (self.x + p2Offset[0], self.y + p2Offset[1]) 
		#p3Offset = (self.vx + 6 * ((self.vx / self.vy) if self.vy == 0 else 1), self.vy + 6 * ((self.vx / self.vy) if self.vy == 0 else 1))
		#p3 = (self.x + p3Offset[0], self.y + p3Offset[1]) 

		#pygame.draw.polygon(screen, self.color, [p1, p2, p3])
		pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 5)


	def keepOnScreen(self):
		b = -10
		if self.x < -b:
			self.x = self.screenWidth + b

		if self.y < -b:
			self.y = self.screenHeight + b

		if self.x > self.screenWidth + b:
			self.x = -b

		if self.y > self.screenHeight + b:
			self.y = -b



	def steering(self, target):
		v = normalize(target)
		v[0] *= self.maxSpeed - self.vx
		v[1] *= self.maxSpeed - self.vy
		return clamp(v, self.maxForce)


	def update(self, boids):
		separationForce = [0, 0]
		alignmentForce = [0, 0]
		cohesionForce = [0, 0]

		averageVel = [0, 0]
		averagePos = [0, 0]

		self.ax = 0
		self.ay = 0
		self.forces = []
		
		
		
	

		numBoidsICanSee = 0

		for boid in boids:
			dist = math.sqrt((self.x - boid.x) * (self.x - boid.x) + (self.y - boid.y) * (self.y - boid.y))
			if boid != self and dist < self.sight:
				averageVel[0] += boid.vx
				averageVel[1] += boid.vy

				averagePos[0] += boid.x
				averagePos[1] += boid.y

				x = (self.x - boid.x) / (dist * dist) if dist > 0 else 1
				y = (self.y - boid.y) / (dist * dist) if dist > 0 else 1
				separationForce = add(separationForce,[x, y])


				#self.forces.append(self.steering([separationForce[0] * self.separationWeight, separationForce[1] * self.separationWeight]))
				numBoidsICanSee += 1
				
		if numBoidsICanSee > 0:
			averageVel[0] /= numBoidsICanSee
			averageVel[1] /= numBoidsICanSee

			averagePos[0] /= numBoidsICanSee
			averagePos[1] /= numBoidsICanSee


		alignmentForce[0] = (averageVel[0])
		alignmentForce[1] = (averageVel[1])


		cohesionForce[0] = (averagePos[0] - self.x) 
		cohesionForce[1] = (averagePos[1] - self.y)

		separationForce = normalize(separationForce)
		alignmentForce = normalize(alignmentForce)
		cohesionForce = normalize(cohesionForce)
		
		

		self.separationForce = self.steering([separationForce[0] * self.separationWeight, separationForce[1] * self.separationWeight])
		self.alignmentForce = self.steering([alignmentForce[0] * self.alignmentWeight, alignmentForce[1] * self.alignmentWeight])
		self.cohesionForce = self.steering([cohesionForce[0] * self.cohesionWeight, cohesionForce[1] * self.cohesionWeight])

		self.forces.append(self.separationForce) 
		self.forces.append(self.alignmentForce) 
		self.forces.append(self.cohesionForce)
		
		

		for force in self.forces:
			self.ax += force[0] / self.mass
			self.ay += force[1] / self.mass

		self.x += self.vx
		self.y += self.vy

		self.vx += self.ax
		self.vy += self.ay 

		v = math.sqrt(self.vx * self.vx + self.vy * self.vy)

		self.vx = (self.vx / v) if v != 0 else random.random()
		self.vy = (self.vy / v) if v != 0 else random.random()

		self.vx *= self.maxSpeed
		self.vy *= self.maxSpeed

		self.keepOnScreen()



