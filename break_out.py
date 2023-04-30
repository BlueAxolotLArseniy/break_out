import pygame
import random
pygame.init()

def move_paddle():
    global direction, move_direction_ball
    if paddle.rect.colliderect(ball.rect):
        direction = 'Up'
        coordinats[0] = paddle.rect.x - ball.rect.x + 12.5
        move_direction_ball = coordinats[0] / 3.055555555555555555555555555555555555555555555555555555555555555555555555555555555555555555 / 9
        move_direction_ball -= move_direction_ball * 2
    if start_move_ball and direction == 'Down':
        ball.rect.move_ip(0, 1)
    elif start_move_ball and direction == 'Up':
        ball.rect.move_ip(move_direction_ball, -1)
    if ball.rect.y < 5:
        direction = 'Down'

def stop_move_paddle():
    if event.pos[0] < 266 / 2 + 27.5 and event.pos[1] < 250 + 7.5:
        paddle.rect.x, paddle.rect.y = 266 / 2, 250
    elif event.pos[0] > 532 + 133 - 27.5 and event.pos[1] < 250 + 7.5:
        paddle.rect.x, paddle.rect.y = 532 - 55 + 133, 250
    elif event.pos[0] > 532 - 27.5 + 133:
        paddle.rect.x, paddle.rect.y = 532 - 55 + 133, event.pos[1] - 7.5
    elif event.pos[0] < 266 + 27.5 - 133:
        paddle.rect.x, paddle.rect.y = 266 / 2, event.pos[1] - 7.5
    elif event.pos[1] < 250 + 7.5:
        paddle.rect.x, paddle.rect.y = event.pos[0] - 27.5, 250
    elif event.pos[0] < 532 + 133 and event.pos[0] > 266 - 133 and event.pos[1] > 250:
        paddle.rect.x, paddle.rect.y = event.pos[0] - 27.5, event.pos[1] - 7.5

def collision_control():
    if paddle.rect.colliderect(ball.rect):
        direction = 'Up'

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.rect = self.image.get_rect(center=(x, y))

class blocks(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*6.8, self.image.get_height()*6.8))
        self.rect = self.image.get_rect(center=(x, y))

class BALL(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.rect = self.image.get_rect(center=(x, y))

sc = pygame.display.set_mode((800, 500))
pos = 0
fsd = False
FPS = 80
start_move_ball = False
start_move_ball_game = False
start_move_ball_game_list = [0, 0]
direction = 'Down'
move_direction_ball = float(random.randint(-9, 9) / 10)
coordinats = [0, 0]
#pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

block1 = blocks(200, 120, 'stoP.png')

ball = BALL(400, 200, 'Ball.png')

paddle = Paddle(0, 0, 'Мышь.png')

f1 = pygame.font.Font(None, 36)
text1 = f1.render(str(round(clock.get_fps())), 1, (180, 0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            stop_move_paddle()
            sc.blit(ball.image, ball.rect)
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_move_ball = True

    sc.fill((0, 0, 0))
    sc.blit(ball.image, ball.rect)
    sc.blit(paddle.image, paddle.rect)
    sc.blit(block1.image, block1.rect)
    clock.tick(FPS)

    move_paddle()

    pygame.draw.rect(sc, (255, 255, 255), (266 / 2, 0, 266 * 2, 255), 5)
    pygame.draw.rect(sc, (255, 255, 255), (266 / 2, 250, 266 * 2, 255), 5)
    sc.blit(f1.render((str(round(clock.get_fps()))), 5, (180, 0, 0)), (750, 5))
    # stop_move_paddle()

    pygame.display.update()