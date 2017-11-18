import pygame
from score import *
from sprite import *
from settings import *

class Player(Sprite):
	def __init__(self):
		super(Player, self).__init__("../res/player.jpg")

	def init_score(self):
		self.score = Score(self.x, window_height - window_height / 8, "Comic Sans MS", (255, 255, 255))

	def render_score(self, dest_surface):
		self.score.render(dest_surface)
