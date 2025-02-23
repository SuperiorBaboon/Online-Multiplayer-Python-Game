import pygame
pygame.init()

class Floor:
    def __init__(self):
        self.x = 0
        self.y = 200
        self.width = 200
        self.height = 50
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
