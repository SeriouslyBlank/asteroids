import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
import sys


def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	x = SCREEN_WIDTH/2
	y = SCREEN_HEIGHT/2
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable)
	asteroidfield = AsteroidField()

	player = Player(x, y, PLAYER_RADIUS)

	running = True
	while running:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		        return
		screen.fill("black")

		for thing in drawable:
			thing.draw(screen)		

		for thing in updateable:
			thing.update(dt)
			


		for aster in asteroids:
			if player.collided(aster) == True:
				print("Game over!")
				sys.exit()


		
		dt = clock.tick(60) / 1000

		pygame.display.flip()

if __name__ == "__main__":
    main()