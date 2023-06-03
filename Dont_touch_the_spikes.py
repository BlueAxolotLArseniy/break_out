import pygame
import random
from threading import Timer
pygame.init()

# pygame.mixer.music.load('berd_soung.mp3')
# pygame.mixer.music.play(-1)

def move_throns_right():
    direction = 'left'
    berd.rect.x = 755
    numer_x = 0
    number = -15
    berd.transform_left('player2.png')
    if steps == 5:
        steps_direction = 'up'
    if steps == 0:
        steps_direction = 'down'

def move_throns_left():
    direction = 'right'
    berd.rect.x = 0
    numer_x = 0
    number = 15
    berd.transform_right('player.png')
    if steps == 5:
        steps_direction = 'up'
    if steps == 0:
        steps_direction = 'down'


def gravitation():
    global number_gravitation, berd, direction, number, numer_x, thorn, thorn2, randomazer, steps, steps_direction, run
    if berd.rect.colliderect(thorn) or berd.rect.colliderect(thorn2):
        run = False
    number_gravitation -= 0.5
    berd.rect.y -= number_gravitation
    if berd.rect.bottom >= 500:
        number_gravitation = 0
        berd.rect.y = 475
    if direction == 'right':
        numer_x += 0.5
    if direction == 'left':
        numer_x -= 0.5
    if numer_x % 1 == 0:
        berd.rect.move_ip(number, 0)
    if berd.rect.right >= 801:
        Timer(1, move_throns_right).start()
    if berd.rect.x <= -1:
        Timer(1, move_throns_left).start()
    if berd.rect.y <= 0:
        berd.rect.y = 0
        number_gravitation = -1

sc = pygame.display.set_mode((800, 500))

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.rect = self.image.get_rect(center=(x, y))
    def transform_left(self, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
    def transform_right(self, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 255, 255))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))


class Let(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.rect = self.image.get_rect(center=(x, y))

clock = pygame.time.Clock()

berd = Player(400, 250, 'player.png')

thorn = Let(10, -300, 'thorn.png')
thorn2 = Let(10, 600, 'thorn.png')

FPS = 60
number_gravitation = 0
numer_x = 0
direction = 'right'
number = 15
randomazer = 50
steps = 1
steps_direction = 'down'

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            number_gravitation = 13
            print(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                number_gravitation = 3
                print(0)

    sc.fill((0, 0, 0))
    gravitation()
    sc.blit(berd.image, berd.rect)
    sc.blit(thorn.image, thorn.rect)
    sc.blit(thorn2.image, thorn2.rect)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()