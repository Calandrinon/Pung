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
		self.speed = 7

	def reset(self, winner=0):
		self.start_x = window_width / 2 - self.get_width() / 2
		self.start_y = window_height / 2 - self.get_height() / 2
		self.finish_x = None
		self.finish_y = None
		self.set_pos(self.start_x, self.start_y)

		if winner == 0:
			if random.randint(0, 2) == 1:
				self.finish_x = window_width
				self.sign_x = 1
			else:
				self.finish_x = 0
				self.sign_x = -1
		else:
			if winner == 2:
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
		self.f = lambda x: self.slope * (self.x - self.finish_x) + self.finish_y

	def move(self):
		super(Ball, self).set_pos(self.x + self.sign_x * self.speed, self.f(self.x + self.sign_x * self.speed))

	def touches_side_wall(self):
		q = False
		if self.y <= 0:
			self.set_pos(self.x, 1)
			q = True

		if self.y >= window_height - super(Ball, self).get_height():
			self.set_pos(self.x, window_height - super(Ball, self).get_height() - 1)
			q = True
		return q

	def out_of_boundaries(self, p1, p2):
		q = False
		p = 0
		if self.x > p2.x:
			p1.score.increase()
			q = True
			p = 1
		if self.x < p1.x:
			p2.score.increase()
			q = True
			p = 2
		return (q, p)

	def bounce(self, p1, p2):
		if self.collision(p1) or self.collision(p2):
			self.finish_x = self.start_x
			self.finish_y = self.y + (self.y - self.start_y)
			self.start_x = self.x
			self.start_y = self.y
			self.slope = (self.finish_y - self.start_y) / (self.finish_x - self.start_x)
			self.f = lambda x: self.slope * (self.x - self.finish_x) + self.finish_y
			if self.finish_x - self.x < 0:
				self.sign_x = -1
			else:
				self.sign_x = 1

		if self.touches_side_wall():
			self.finish_x = self.x + (self.x - self.start_x)
			self.finish_y = self.start_y
			self.start_x = self.x
			self.start_y = self.y
			self.slope = (self.finish_y - self.start_y) / (self.finish_x - self.start_x)
			self.f = lambda x: self.slope * (self.x - self.finish_x) + self.finish_y
			if self.finish_x - self.x < 0:
				self.sign_x = -1
			else:
				self.sign_x = 1
