import pygame
import random
from sprite import *
from settings import *

class Ball(Sprite):
	sign_x = 1

	def __init__(self):
		super(Ball, self).__init__("../res/ball.jpg")
		self.start_x = window_width / 2 - self.get_width() / 2
		self.start_y = window_height / 2 - self.get_height() / 2
		self.finish_x = None
		self.finish_y = None
		self.set_pos(self.start_x, self.start_y)
		self.speed = 5

	def reset(self):
		if random.randint(0, 2) == 1:
			self.finish_x = window_width
			self.sign_x = 1
		else:
			self.finish_x = 0
			self.sign_x = -1

		finish_y_option1 = random.randint(unit, window_height / 2 - unit)
		finish_y_option2 = random.randint(window_height / 2 + unit, window_height - unit)
		if random.randint(0, 2) == 1:
			self.finish_y = finish_y_option1
		else:
			self.finish_y = finish_y_option2

		self.slope = (self.finish_y - self.start_y) / (self.finish_x - self.start_x)
		self.f = lambda x: self.slope * (x - self.finish_x) + self.finish_y
		print(self.finish_x, self.finish_y)
		print(self.start_x, self.start_y)

	def move(self):
		super(Ball, self).set_pos(self.x + self.sign_x * self.speed, self.f(self.x + self.sign_x * self.speed))
