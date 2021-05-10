import pygame
import random
import boid

pygame.init()

SCREEN_WIDTH = 2000 // 1
SCREEN_HEIGHT = 1400 // 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

max_boids = 1000
boids = []

partitions = []
partitionsNumX = 10
partitionsNumY = 10
partitionSizeX = SCREEN_WIDTH // partitionsNumX
partitionSizeY = SCREEN_HEIGHT // partitionsNumY

def draw():
	screen.fill((0, 0, 0))

	for i in range(SCREEN_WIDTH // partitionSizeX):
		pygame.draw.line(screen, (255,255,255), (i * partitionSizeX, 0), (i * partitionSizeX, SCREEN_HEIGHT))
	for j in range(SCREEN_HEIGHT // partitionSizeY):
		pygame.draw.line(screen, (255,255,255), (0, j * partitionSizeY), (SCREEN_WIDTH, j * partitionSizeY))
		


	for boid in boids:
		boid.draw(screen)

	pygame.display.update()

def update():
	for i in range(len(partitions)):
		for j in range(len(partitions[i])):
			partitions[i][j] = []

	# partitionNumX * partitionNumY iterations
	# 100

	for boid in boids:
		partitions[int(boid.x // partitionSizeX)][int(boid.y // partitionSizeY)].append(boid)


	# max_boids iterations
	# 1000

	for boid in boids:
		temp = []
		for i in range(-1, 1):
			for j in range(-1, 1):
				#if int(boid.x // partitionSizeX) + i >= 0 and int(boid.y // partitionSizeY) + j >= 0 and int(boid.x // partitionSizeX) + i < len(partitions) and int(boid.y // partitionSizeY) + j > len(partitions[0]):
					temp.extend(partitions[int(boid.x // partitionSizeX) + i][int(boid.y // partitionSizeY) + j])
		boid.update(temp)
	#	boid.update(boids)

	#max boid iterations * size of temp
	#1000 * size of temp

clock = pygame.time.Clock()
t1 = 0
t2 = 0

boidSpawnTimer = 1
boidSpawnTimerResetValue = .1

for i in range(SCREEN_WIDTH // partitionSizeX):
	partitions.append([])
	for j in range(SCREEN_HEIGHT // partitionSizeY):
		partitions[i].append([])


while run:

	clock.tick(60)
	
	delta = 1 / 60


	boidSpawnTimer -= delta

	if len(boids) < max_boids:
		boids.append(boid.Boid(random.random() * SCREEN_WIDTH, random.random() * SCREEN_HEIGHT, random.random() * 2 - 1, random.random() * 2 - 1,  SCREEN_WIDTH, SCREEN_HEIGHT, (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))))
		boidSpawnTimer = boidSpawnTimerResetValue
		print(len(boids))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	draw()

	update()
	
	




pygame.quit()
quit()