import pygame
from score import *
from sprite import *
from settings import *

class Player(Sprite):
	def __init__(self):
		super(Player, self).__init__("../res/player.jpg")

	def init_score(self, x, y):
		self.score = Score(x, y, "Comic Sans MS", (150, 150, 150))

	def render_score(self, dest_surface):
		self.score.render(dest_surface)

	def won(self):
		if self.score.amount == 10:
			return True
		return False
