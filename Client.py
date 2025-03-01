import pygame
from Network import Network
from player import Player
from Floor import Floor

width = 1900
height = 1024
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

floor = Floor()


def move(p):
    keys = pygame.key.get_pressed()
    original_pos = (p.x, p.y)  # Store original position for collision resolution
    p.y -= p.yVel

    # Handle movement
    if keys[pygame.K_a]:
        p.x -= p.xVel

    if keys[pygame.K_d]:
        p.x += p.xVel

    if keys[pygame.K_w]:
        if p.collide:
            p.yVel = 5

    if keys[pygame.K_i]:
        print("emote")

    if keys[pygame.K_o]:
        print("Heavy Attack")

    if keys[pygame.K_k]:
        print("light attack")

    if keys[pygame.K_p]:
        print("block")

    # Update player rectangle
    p.update()

    # Resolve collision
    if p.check_collision(floor):
        p.yVel = 0
        p.collide = True
        resolve_collision(p, floor)
    else:
        p.yVel -= 0.1
        p.collide = False

def resolve_collision(player, obj):
    """Resolves collision by moving the player out of the object on the shortest axis."""
    # Calculate overlap on all sides
    overlap_left = player.rect.right - obj.rect.left
    overlap_right = obj.rect.right - player.rect.left
    overlap_top = player.rect.bottom - obj.rect.top
    overlap_bottom = obj.rect.bottom - player.rect.top

    # Find the smallest overlap
    smallest_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

    # Move the player out on the axis of the smallest overlap
    if smallest_overlap == overlap_left:
        player.x -= overlap_left
    elif smallest_overlap == overlap_right:
        player.x += overlap_right
    elif smallest_overlap == overlap_top:
        player.y -= overlap_top
    elif smallest_overlap == overlap_bottom:
        player.y += overlap_bottom

    player.update()  # Update the rect with the new position

def redrawWindow(win, player, player2):
    win.fill((0, 0, 0))
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
        clock.tick(180)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        move(p)
        redrawWindow(win, p, p2)

main()
