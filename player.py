import pygame
global bits

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3
        x2 = x + self.width
        y2 = y + self.height
        self.coords = (x,y,x2,y2)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)