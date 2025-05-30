import pygame
from circleshape import CircleShape
import random
from constants import *
class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	def draw(self, screen):
		pygame.draw.circle(screen,"purple",self.position,self.radius,width=2)
	def update(self, dt):
		self.position+=self.velocity*dt
	def split(self):
		self.kill()
		if self.radius<=ASTEROID_MIN_RADIUS:
			return
		else:
			random_angle=random.uniform(20,50)
			vector=[self.velocity.rotate(random_angle),
				self.velocity.rotate(-random_angle)]
			radius=self.radius-ASTEROID_MIN_RADIUS
			for v in vector:
				a=Asteroid(self.position.x,self.position.y,radius)
				a.velocity=v*1.2
