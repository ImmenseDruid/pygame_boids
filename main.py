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
partitionsNumX = 30
partitionsNumY = 30
partitionSizeX = SCREEN_WIDTH // partitionsNumX
partitionSizeY = SCREEN_HEIGHT // partitionsNumY

def draw():
	screen.fill((0, 0, 0))

	#for i in range(SCREEN_WIDTH // partitionSizeX):
	#	pygame.draw.line(screen, (255,255,255), (i * partitionSizeX, 0), (i * partitionSizeX, SCREEN_HEIGHT))
	#for j in range(SCREEN_HEIGHT // partitionSizeY):
	#	pygame.draw.line(screen, (255,255,255), (0, j * partitionSizeY), (SCREEN_WIDTH, j * partitionSizeY))
		


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
		#print(str(int(boid.x // partitionSizeX)) + '/' + str(len(partitions)))
		#print(str(int(boid.y // partitionSizeY)) + '/' + str(len(partitions)))
		for i in range(-1, 2):
			for j in range(-1, 2):
				partitions[int(boid.x // partitionSizeX + partitionsNumX - 1 + i) % len(partitions)][int(boid.y // partitionSizeY + partitionsNumY - 1 + j) % len(partitions[0])].append(boid)


	# max_boids iterations
	# 1000
	removeMe = []
	for boid in boids:
		temp = partitions[(int(boid.x // partitionSizeX) + i + partitionsNumX - 1) % len(partitions)][(int(boid.y // partitionSizeY) + j + partitionsNumY - 1) % len(partitions[0])]
		boid.update(temp)
		if boid.lifeSpan <= 0:
			removeMe.append(boid)
	#	boid.update(boids)

	for boid in removeMe:
		boids.remove(boid)

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

	delta = clock.tick(30)

	boidSpawnTimer -= delta / 1000

	if len(boids) < max_boids and boidSpawnTimer <=  0:
		boids.append(boid.Boid(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, random.random() * 2 - 1, random.random() * 2 - 1,  SCREEN_WIDTH, SCREEN_HEIGHT, (random.randrange(1, 255), random.randrange(1, 255), random.randrange(1, 255))))
		boidSpawnTimer = boidSpawnTimerResetValue
		print(len(boids))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	draw()

	update()

	#print(1000 / delta)
	
	




pygame.quit()
quit()