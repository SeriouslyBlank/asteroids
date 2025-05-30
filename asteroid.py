from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random
from scoreboard import Scoreboard

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.rotation = 0


	def draw(self, screen):
		pygame.draw.circle(screen,"white", self.position, self.radius, width = 2)
		

	def update(self, dt):
		self.position += (self.velocity * dt)



	def split(self, score):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			score.add_points(100)
			return
		else:
			rand_angle = random.uniform(20, 50)
			velo_1 = self.velocity.rotate(rand_angle)
			velo_2 = self.velocity.rotate(-rand_angle)
			new_rad = self.radius - ASTEROID_MIN_RADIUS
			ast_1 = Asteroid(self.position.x, self.position.y, new_rad)
			ast_2 = Asteroid(self.position.x, self.position.y, new_rad)
			ast_1.velocity = velo_1 * 1.2
			ast_2.velocity = velo_2 * 1.2
			score.add_points(25)