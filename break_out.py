import pygame
import random
pygame.init()

def move_ball():
    global direction, move_direction_ball, start_ball
    if start_ball:
        ball.rect.move_ip(0, 2)
    if paddle.rect.colliderect(ball.rect):
        start_ball = False
        direction = 'Up'
        if paddle.rect.centerx + random.randint(22, 27) - ball.rect.centerx < 0:
            move_direction_ball = 3
        elif paddle.rect.centerx + random.randint(22, 27) - ball.rect.centerx > 0:
            move_direction_ball = -3
        elif paddle.rect.centerx + random.randint(15, 18) - ball.rect.centerx < 0:
            move_direction_ball = 2
        elif paddle.rect.centerx + random.randint(15, 18) - ball.rect.centerx > 0:
            move_direction_ball = -2
        elif paddle.rect.centerx + random.randint(7, 9) - ball.rect.centerx < 0:
            move_direction_ball = 1
        elif paddle.rect.centerx + random.randint(7, 9) - ball.rect.centerx > 0:
            move_direction_ball = -1
        elif paddle.rect.centerx + random.randint(0, 5) - ball.rect.centerx < 0:
            move_direction_ball = 0
        elif paddle.rect.centerx + random.randint(0, 5) - ball.rect.centerx > 0:
            move_direction_ball = 0
    if start_move_ball and direction == 'Down' and start_ball == False:
        ball.rect.move_ip(move_direction_ball, 2)
    elif start_move_ball and direction == 'Up':
        ball.rect.move_ip(move_direction_ball, -2)
    if ball.rect.y < 5:
        direction = 'Down'
    if ball.rect.x <= 0 or ball.rect.x >= 800 - 15:
        move_direction_ball -= move_direction_ball * 2
    if ball.rect.y >= 500 - 15:
        exit()
    if ball.rect.colliderect(block1):
        move_direction_ball -= move_direction_ball * 2
        if ball.rect.y < block1.rect.y:
            direction = 'Up'
            move_direction_ball = move_direction_ball - move_direction_ball * 2
        else:
            direction = 'Down'
            move_direction_ball = move_direction_ball - move_direction_ball * 2
        block1.rect.x = -200
    if ball.rect.colliderect(block2):
        move_direction_ball -= move_direction_ball * 2
        if ball.rect.y < block2.rect.y:
            direction = 'Up'
            move_direction_ball = move_direction_ball - move_direction_ball * 2
        else:
            direction = 'Down'
            move_direction_ball = move_direction_ball - move_direction_ball * 2
        block2.rect.x = -200
    if ball.rect.colliderect(block3):
        move_direction_ball -= move_direction_ball * 2
        if ball.rect.y < block3.rect.y:
            direction = 'Up'
            move_direction_ball = move_direction_ball - move_direction_ball * 2
        else:
            direction = 'Down'
            move_direction_ball = move_direction_ball - move_direction_ball * 2
        block3.rect.x = -200
    if ball.rect.colliderect(block4):
        move_direction_ball -= move_direction_ball * 2
        if ball.rect.y < block4.rect.y:
            direction = 'Up'
            move_direction_ball = move_direction_ball - move_direction_ball * 2
        else:
            direction = 'Down'
            move_direction_ball = move_direction_ball - move_direction_ball * 2
        block4.rect.x = -200
    if ball.rect.colliderect(block5):
        move_direction_ball -= move_direction_ball * 2
        if ball.rect.y < block5.rect.y:
            direction = 'Up'
            move_direction_ball = move_direction_ball - move_direction_ball * 2
        else:
            direction = 'Down'
            move_direction_ball = move_direction_ball - move_direction_ball * 2
        block5.rect.x = -200
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
    delete = False
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
move_direction_ball = 0
coordinats = 0
start_ball = False
one_this = 0
apokalipsis = False
#pygame.mouse.set_visible(False)

clock = pygame.time.Clock()

block1 = blocks(200, 120, 'stoP.png')
block2 = blocks(300, 120, 'stoP.png')
block3 = blocks(400, 120, 'stoP.png')
block4 = blocks(500, 120, 'stoP.png')
block5 = blocks(600, 120, 'stoP.png')


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
            if one_this == 0:
                start_move_ball = True
                start_ball = True
                one_this = 1

    sc.fill((0, 0, 0))
    sc.blit(ball.image, ball.rect)
    sc.blit(paddle.image, paddle.rect)

    sc.blit(block1.image, block1.rect)
    sc.blit(block2.image, block2.rect)
    sc.blit(block3.image, block3.rect)
    sc.blit(block4.image, block4.rect)
    sc.blit(block5.image, block5.rect)

    clock.tick(FPS)

    move_ball()

    pygame.draw.rect(sc, (255, 255, 255), (266 / 2, 0, 266 * 2, 255), 5)
    pygame.draw.rect(sc, (255, 255, 255), (266 / 2, 250, 266 * 2, 255), 5)
    sc.blit(f1.render((str(round(clock.get_fps()))), 5, (180, 0, 0)), (750, 5))
    # stop_move_paddle()

    pygame.display.update()