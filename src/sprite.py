import pygame

class Sprite:
	speed = 5

	def __init__(self, image_path):
		self.x = 0
		self.y = 0
		self.image = pygame.image.load(image_path)
		self.height = self.image.get_height()
		self.width = self.image.get_width()

	def render(self, dest_surface):
		dest_surface.blit(self.image, (self.x, self.y))

	def set_pos(self, x, y):
		self.x = x
		self.y = y 

	def move(self, offset_x, offset_y):
		self.set_pos(self.x + offset_x, self.y + offset_y)

	def get_width(self):
		return self.width

	def get_height(self):
		return self.height