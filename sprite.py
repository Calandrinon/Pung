import pygame

class Sprite:
	_speed = 5

	def __init__(self, x, y, image_path):
		self.x = x
		self.y = y
		self.image = pygame.image.load(image_path)

	def render(self, dest_surface):
		dest_surface.blit(self.image, (self.x, self.y))

	def move(self, offset_x, offset_y):
		self.x += offset_x
		self.y += offset_y