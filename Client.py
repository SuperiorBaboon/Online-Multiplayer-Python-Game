import pygame
from Network import Network
from player import Player
from Floor import floor
global bits

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

floor = floor()

def check_collision(obj1, obj2):
    """Checks if two objects collide."""
    return (obj1.coords.x < obj2.coords.x2 and
            obj1.coords.x2 > obj2.coords.x and
            obj1.coords.y < obj2.coords.y2 and
            obj1.coords.y2 > obj2.coords.y)

def move(p):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        p.x -= p.vel

    if keys[pygame.K_RIGHT]:
        p.x += p.vel

    if keys[pygame.K_UP]:
        p.y -= p.vel

    if keys[pygame.K_DOWN]:
        p.y += p.vel

    p.update()

def redrawWindow(win,player, player2):
    win.fill((0,0,0))
    player.draw(win)
    player2.draw(win)
    floor.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        move(p)
        redrawWindow(win, p, p2)

main()