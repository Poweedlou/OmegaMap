import pygame
from image_coords import get_bytes_image

def update():
    bio = get_bytes_image(coords, spn)
    img = pygame.image.load(bio)
    screen.blit(img, (0, 0))

coords = [50.00001, 50.00001]
spn = 1
keys = {
    pygame.K_UP: (0, 1),
    pygame.K_DOWN: (0, -1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0)
}

screen = pygame.display.set_mode((600, 450))
update()
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
                update()
            if k == pygame.K_PAGEUP:
                spn *= 2
            if k == pygame.K_PAGEDOWN:
                spn /= 2
    pygame.display.flip()