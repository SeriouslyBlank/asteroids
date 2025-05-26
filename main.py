import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
import sys
from shot import *
from scoreboard import Scoreboard

def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	x = SCREEN_WIDTH/2
	y = SCREEN_HEIGHT/2
	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shot_grp = pygame.sprite.Group()
	Scoreboard.containers = (drawable)
	Shot.containers = (shot_grp, updateable, drawable)
	Player.containers = (updateable, drawable)
	Asteroid.containers = (asteroids, updateable, drawable)
	AsteroidField.containers = (updateable)
	asteroidfield = AsteroidField()
	score = Scoreboard()

	player = Player(x, y, PLAYER_RADIUS)

	running = True
	while running:
		for event in pygame.event.get():
		    if event.type == pygame.QUIT:
		    	print("Window Closed")
		        running = False
		    if event.type == pygame.KEYDOWN:
		        if event.key == pygame.K_ESCAPE:
		            print("Escape pressed!")
		            running = False 

		screen.fill("black")
		score.draw(screen)

		for thing in drawable:
			thing.draw(screen)		

		for thing in updateable:
			thing.update(dt)
		keys = pygame.key.get_pressed()



		for aster in asteroids:
			if player.collided(aster) == True:
				print("Game over!")
				sys.exit()
			for bullet in shot_grp:
				if bullet.collided(aster) ==True:
					bullet.kill()
					aster.split(score)


		
		dt = clock.tick(60) / 1000

		pygame.display.flip()

if __name__ == "__main__":
    main()