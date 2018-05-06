import pygame, os
from player import Player
from ball import Ball
from settings import *

def init():
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (20,20)
	pygame.init()
	global screen, player1, player2, ball, start_time, win_clock
	screen = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
	start_time = win_clock = pygame.time.get_ticks()
	pygame.display.set_caption("Pung")

	player1 = Player()
	player2 = Player()
	ball = Ball()

	player1.set_pos(dist_from_edge, window_height / 2 - player1.get_height() / 2)
	player2.set_pos(window_width - player2.get_width() - dist_from_edge, window_height / 2 - player2.get_height() / 2)
	player1.init_score(window_width / 4, window_height / 16)
	player2.init_score(window_width - window_width / 4, window_height / 16)
	ball.reset()

def handle_input():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			return True

	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_w]:
		if player1.y > 0:
			player1.move(0, -Player.speed)
	if pressed_keys[pygame.K_s]:
		if player1.y < window_height - player1.get_height():
			player1.move(0, Player.speed)
	if pressed_keys[pygame.K_UP]:
		if player2.y > 0:
			player2.move(0, -Player.speed)
	if pressed_keys[pygame.K_DOWN]:
		if player2.y < window_height - player2.get_height():
			player2.move(0, Player.speed)
	if pressed_keys[pygame.K_ESCAPE]:
		return True

	return False

def has_won():
	won1 = player1.won()
	won2 = player2.won()

	if won1 or won2:
		font_size = 50
		font_type = "Times New Roman"
		font = pygame.font.SysFont(font_type, font_size)

		if won1:
			message = "Player 1 won!"
		else:
			message = "Player 2 won!"

		game_over_msg_size = 13
		esc_msg_size = 17
		game_over = font.render(message, False, (5, 165, 62))
		esc = font.render("Press ESC to exit", False, (255, 0, 0))
		game_over_pos = (window_width / 2 - (game_over_msg_size * font_size) / 2, window_height / 2 - font_size / 2)
		esc_pos = (window_width / 2 - (esc_msg_size * font_size) / 2, window_height - window_height / 5)

		screen.blit(game_over, game_over_pos)
		screen.blit(esc, esc_pos)
		pygame.display.update()
		return True
	return False

def draw():
	global start_time, win_clock

	current_time = pygame.time.get_ticks()
	if current_time - start_time > 1000 / FPS:
		start_time = pygame.time.get_ticks()
		winner = ball.out_of_boundaries(player1, player2)
		if winner[0]:
			win_clock = pygame.time.get_ticks()
			ball.reset(winner[1])

		screen.fill((0, 0, 0))

		current_time = pygame.time.get_ticks()
		if current_time - win_clock > 2000:
			ball.move()
			ball.bounce(player1, player2)
			ball.render(screen)

		player1.render(screen)
		player2.render(screen)
		player1.render_score(screen)
		player2.render_score(screen)
		pygame.draw.line(screen, (255, 255, 255), (window_width / 2, 0), (window_width / 2, window_height))
		pygame.display.update()

def main_loop():
	running = True
	game_is_over = False

	while running:
		if handle_input():
			running = False

		if game_is_over:
			continue

		game_is_over = has_won()
		draw()

	pygame.quit()

if __name__ == "__main__":
	init()
	main_loop()
