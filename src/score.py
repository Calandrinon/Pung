import pygame

class Score:
    def __init__(self, x, y, font, color):
        self.amount = 0
        self.x = x
        self.y = y
        self.font = font
        self.color = color
        self.score_font = pygame.font.SysFont(font, 70)

    def increase(self):
        self.amount += 1

    def render(self, dest_surface):
        text = self.score_font.render(str(self.amount), False, self.color)
        dest_surface.blit(text, (self.x, self.y))
