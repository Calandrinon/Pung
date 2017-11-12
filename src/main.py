import pygame
from player import Player
from ball import Ball
from settings import *
pygame.init()

screen = pygame.display.set_mode((window_width, window_height))
running = True

player1 = Player()
player2 = Player()
player1.set_pos(dist_from_edge, window_height / 2 - player1.get_height() / 2)
player2.set_pos(window_width - player2.get_width() - dist_from_edge, window_height / 2 - player2.get_height() / 2)

ball = Ball()
ball.reset()

start_time = pygame.time.get_ticks()

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_w]:
		player1.move(0, -Player.speed)
	if pressed_keys[pygame.K_s]:
		player1.move(0, Player.speed)
	if pressed_keys[pygame.K_UP]:
		player2.move(0, -Player.speed)
	if pressed_keys[pygame.K_DOWN]:
		player2.move(0, Player.speed)

	current_time = pygame.time.get_ticks()
	if current_time - start_time > 1000/FPS:
		start_time = pygame.time.get_ticks()
		screen.fill((0, 0, 0))
		player1.render(screen)
		player2.render(screen)
		ball.render(screen)
		pygame.display.flip()

pygame.quit()