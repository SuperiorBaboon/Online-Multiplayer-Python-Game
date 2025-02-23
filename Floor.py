import pygame
pygame.init()

class floor():
    def __init__(self):
        self.x=0
        self.y=200
        self.width=200
        self.height=50
        self.color = (255,255,255)
        self.rect = (self.x, self.y, self.width, self.height)
        x2 = self.x + self.width
        y2 = self.y + self.height
        self.coords = (self.x, self.y, x2, y2)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)