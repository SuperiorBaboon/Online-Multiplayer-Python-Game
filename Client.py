import pygame
from Network import Network
from player import Player
from Floor import Floor

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

floor = Floor()

def move(p):
    keys = pygame.key.get_pressed()
    original_pos = (p.x, p.y)  # Store original position for collision resolution

    # Handle movement
    if keys[pygame.K_LEFT]:
        p.x -= p.vel
    if keys[pygame.K_RIGHT]:
        p.x += p.vel
    if keys[pygame.K_UP]:
        p.y -= p.vel
    if keys[pygame.K_DOWN]:
        p.y += p.vel

    # Resolve collision
    if p.check_collision(floor):
        resolve_collision(p, floor)

    # Update player rectangle
    p.update()

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
