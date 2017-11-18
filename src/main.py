import pygame, os
from player import Player
from ball import Ball
from settings import *

def init():
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,20)
	pygame.init()
	global screen, player1, player2, ball
	screen = pygame.display.set_mode((window_width, window_height))

	player1 = Player()
	player2 = Player()
	ball = Ball()

	player1.set_pos(dist_from_edge, window_height / 2 - player1.get_height() / 2)
	player2.set_pos(window_width - player2.get_width() - dist_from_edge, window_height / 2 - player2.get_height() / 2)
	player1.init_score()
	player2.init_score()
	ball.reset()

def handle_input():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_w]:
		player1.move(0, -Player.speed)
	if pressed_keys[pygame.K_s]:
		player1.move(0, Player.speed)
	if pressed_keys[pygame.K_UP]:
		player2.move(0, -Player.speed)
	if pressed_keys[pygame.K_DOWN]:
		player2.move(0, Player.speed)

	return False

def main_loop():
	start_time = pygame.time.get_ticks()

	while True:
		if handle_input():
			break

		current_time = pygame.time.get_ticks()
		if current_time - start_time > 1000/FPS:
			start_time = pygame.time.get_ticks()
			winner = ball.out_of_boundaries(player1, player2)
			if winner[0]:
				ball.reset(winner[1])
			ball.move()
			ball.bounce(player1, player2)
			screen.fill((0, 0, 0))
			player1.render(screen)
			player2.render(screen)
			player1.render_score(screen)
			player2.render_score(screen)
			pygame.draw.line(screen, (255, 255, 255), (window_width / 2, 0), (window_width/2, window_height))
			ball.render(screen)
			pygame.display.flip()

	pygame.quit()

if __name__ == "__main__":
	init()
	main_loop()
