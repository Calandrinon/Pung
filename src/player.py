import pygame
from sprite import *

class Player(Sprite):
	def __init__(self):
		super(Player, self).__init__("../res/player.jpg")