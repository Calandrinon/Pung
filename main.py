import pygame
pygame.init()

window_width = 800
window_height = 600

screen = pygame.display.set_mode((window_width, window_height))
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()