import pygame


def update(coords, spn):
    
coords = [50, 50]
spn = 1
keys = {
    pygame.K_UP: (0, 1),
    pygame.K_DOWN: (0, -1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0)
}
screen = pygame.display.set_mode((600, 450))
screen.blit(, (0, 0))
pygame.display.flip()
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            k = e.key
            if k in list(keys.keys()):
                dx, dy = keys[k]
                dx *= spn / 2
                dy *= spn / 2
                coords[0] += dx
                coords[1] += dy
                update(coords, spn)
            screen = pygame.display.set_mode((450, 450))
            screen.blit(d[pos % len(d)], (0, 0))
            pygame.display.flip()