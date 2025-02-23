import pygame

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vel = 1
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def update(self):
        self.rect.topleft = (self.x, self.y)

    def check_collision(self, other):
        """Check if this player collides with another object."""
        return self.rect.colliderect(other.rect)
