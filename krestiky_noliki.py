import pygame
import random
pygame.init()

sc = pygame.display.set_mode((800, 500))

clock = pygame.time.Clock()
FPS = 60

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.draw.aaline(sc, (255, 255, 255), [200 + 139, 450], [200 + 139, 50])
    pygame.draw.aaline(sc, (255, 255, 255), [200 + 139 + 139, 450], [200 + 139 + 139, 50])
    pygame.draw.aaline(sc, (255, 255, 255), [200, 450 + 139], [200 + 139 + 139, 450 + 139])
    pygame.display.update()
    clock.tick(FPS)
