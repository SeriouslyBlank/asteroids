from circleshape import CircleShape
import pygame



class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)


	def draw(self, screen):
		pygame.draw.circle(screen,"white", self.position, self.radius, width = 2)


	def update(self, dt):
		self.position += (self.velocity * dt)


	def collided(self, other):
		total_rad = self.radius + other.radius
		dist = self.position.distance_to(other.position)

		if total_rad <= dist:
			return True
		return False

		
		