import pygame
import random
import boid

pygame.init()

SCREEN_WIDTH = 2000 // 1
SCREEN_HEIGHT = 1400 // 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

max_boids = 500
boids = []

def draw():
	screen.fill((0, 0, 0))

	for boid in boids:
		boid.draw(screen)

	pygame.display.update()

def update():
	for boid in boids:
		

	for boid in boids:
		boid.update(boids)

clock = pygame.time.Clock()
t1 = 0
t2 = 0

boidSpawnTimer = 1
boidSpawnTimerResetValue = .1
while run:

	clock.tick(60)
	
	delta = 1 / 60


	boidSpawnTimer -= delta

	if len(boids) < max_boids and boidSpawnTimer <= 0:

		boids.append(boid.Boid(random.random() * SCREEN_WIDTH, random.random() * SCREEN_HEIGHT, random.random() * 2 - 1, random.random() * 2 - 1,  SCREEN_WIDTH, SCREEN_HEIGHT, (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))))
		boidSpawnTimer = boidSpawnTimerResetValue

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	draw()

	update()
	
	print(len(boids))




pygame.quit()
quit()