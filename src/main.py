import pygame
from player import Player
pygame.init()

window_width = 800
window_height = 600
dist_from_edge = 20

screen = pygame.display.set_mode((window_width, window_height))
running = True

player1 = Player()
player2 = Player()
player1.set_pos(dist_from_edge, window_height / 2 - player1.get_height() / 2)
player2.set_pos(window_width - player2.get_width() - dist_from_edge, window_height / 2 - player2.get_height() / 2)

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

	screen.fill((0, 0, 0))
	player1.render(screen)
	player2.render(screen)
	pygame.display.flip()

pygame.quit()