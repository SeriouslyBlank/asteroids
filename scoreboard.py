import pygame

class Scoreboard:
    def __init__(self, font_size=36, color=(255, 255, 255)):
        self.score = 0
        self.font = pygame.font.SysFont(None, font_size)
        self.color = color

    def add_points(self, points):
        self.score += points

    def draw(self, screen, position=(10, 10)):
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_text, position)
