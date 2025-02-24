import pygame

class Player:
    def __init__(self, x, y, width, height, color, yVel, collide):
        self.yVel = yVel
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.xVel = 1
        self.rect = pygame.Rect(x, y, width, height)
        self.collide = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self):
        self.rect.topleft = (self.x, self.y)

    def check_collision(self, other):
        """Check if this player collides with another object."""
        return self.rect.colliderect(other.rect)
