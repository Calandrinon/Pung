import pygame
pygame.init()
FPS = 90
info = pygame.display.Info()
window_width = info.current_w 
window_height = info.current_h
dist_from_edge = 20
unit = int(window_width / 15)