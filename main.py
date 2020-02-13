import pygame
from image_coords import get_bytes_image

def update():
    bio = get_bytes_image(coords, spn)
    img = pygame.image.load(bio)
    screen.blit(img, (0, 0))

coords = [37.910831, 59.132040]
spn = 0.125
keys = {
    pygame.K_UP: (0, 1),
    pygame.K_DOWN: (0, -1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0)
}

screen = pygame.display.set_mode((650, 450))
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
                if coords[1] > 90 - spn / 2:
                    coords[1] = 90 - spn / 2
                if coords[1] < -90 + spn / 2:
                    coords[1] = -90 + spn / 2
                if coords[0] < -180:
                    coords[0] = 360 - coords[0]
                if coords[0] > 180:
                    coords[0] = -360 + coords[0]
                update()
            if k == pygame.K_PAGEUP:
                spn *= 2
                if spn > 40:
                    spn /= 2
                update()
            if k == pygame.K_PAGEDOWN:
                spn /= 2
                if spn < 0.002:
                    spn *= 2
                update()
    pygame.display.flip()