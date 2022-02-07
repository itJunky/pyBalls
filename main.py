import random
import math
import time
import sys
import pygame

balls_count = 100
ball_size = 20
pygame.init()
balls = []
black = 0, 0, 0
size = scr_width, scr_height = 1200, 800
screen = pygame.display.set_mode(size)
# "intro_ball.gif"
ball_image_file = "bzz_green_ball.gif"


class Ball:
    def __init__(self, first_x, first_y, speed=5, bsz=25):
        ball_img = pygame.image.load(ball_image_file).convert_alpha()
        bl_size = (bsz, bsz)
        self.TARGET = [400, 200]
        self.INTARGET = False
        self.FLASHING = 0
        self.ball_img = pygame.transform.scale(ball_img, bl_size)
        self.speed = [speed, speed]
        if first_x or first_y:
            self.rect = ball_img.get_rect(topleft=(first_x, first_y), size=bl_size)
        else:
            self.rect = ball_img.get_rect(size=bl_size)

    def tick(self):
        self.get_next_step_coordinates()
        self.check_target()
        self.check_borders()
        self.check_contact()
        self.set_img()
        screen.blit(self.ball_img, self.rect)

    def check_borders(self):
        if self.rect.left < 0 or self.rect.right > scr_width:
            self.change_direction(x=True)

        if self.rect.top < 0 or self.rect.bottom > scr_height:
            self.change_direction(y=True)

    def change_direction(self, x=False, y=False):
        if x: self.speed[0] = -self.speed[0]
        if y: self.speed[1] = -self.speed[1]

    def get_next_step_coordinates(self):
        '''
        Осуществляет сдвиг экземпляра шара
        '''
        x = self.rect.x
        y = self.rect.y
        xk = self.TARGET[0]  # координаты цели
        yk = self.TARGET[1]
        Dl = self.get_speed()
        distance = math.sqrt((xk-x)**2+(yk-y)**2)
        if distance > 0.:
            x = x+Dl*(xk-x)/distance  # Считаем насколько надо сдвинуться по Х
            y = y+Dl*(yk-y)/distance  # По Y
        elif ball_size > distance > 0.:  # Пока сюда никогда не заходим
            x = x-Dl*(xk-x)/distance  # Откатываемся назад
            y = y-Dl*(yk-y)/distance  # В случае коллизии

        self.rect.x = int(x)
        self.rect.y = int(y)

    def get_speed(self):
        # TODO change formula
        return abs(self.speed[0])

    def check_target(self):
        distance = math.sqrt((self.TARGET[0] - self.rect.x) ** 2 +
                             (self.TARGET[1] - self.rect.y) ** 2)
        if distance < 1.1 * ball_size:
            self.INTARGET = True
            self.set_target()

    def set_target(self):
        lft_brd = 1
        rgt_brd = scr_width - ball_size
        top_brd = 1
        btm_brd = scr_height - ball_size
        if self.TARGET[0] > self.rect.x:
            # Х новой цели меньше текущей координаты Х мяча
            rgt_brd = self.rect.x
        else:
            lft_brd = self.rect.x
        if self.TARGET[1] > self.rect.y:
            btm_brd = self.rect.y
            if btm_brd < 1: btm_brd = 1
        else:
            top_brd = self.rect.y

        try:
            self.TARGET = [random.randint(lft_brd, rgt_brd),
                           random.randint(top_brd, btm_brd)
            ]
        except Exception as e:
            print(f'{e} -- l {lft_brd}, t {top_brd}, r {rgt_brd}, b {btm_brd}')

    def check_contact(self):
        if self.FLASHING > 0:
            self.FLASHING -= 1

    def set_img(self):
        if self.FLASHING:
            ball_img = pygame.image.load("bzz_blue_ball.gif").convert_alpha()
        elif self.INTARGET:
            ball_img = pygame.image.load("bzz_red_ball.gif").convert_alpha()
            self.INTARGET = False
        else:
            ball_img = pygame.image.load("bzz_green_ball.gif").convert_alpha()

        self.ball_img = pygame.transform.scale(ball_img, (ball_size, ball_size))


# Start main circle of program
if __name__ == '__main__':
    name = 'Baller'
    print(f'Hi, {name}')

    for i in range(balls_count):
        balls.append(Ball(
            random.randint(1, scr_width-ball_size),
            random.randint(1, scr_height-ball_size),
            random.randint(2, 8),
            bsz=ball_size)
        )

    NEED_NEW_TRG = False
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                NEED_NEW_TRG = True

        rng = range(0, len(balls))
        for b1 in rng:
            balls[b1].tick()
            if NEED_NEW_TRG:
                balls[b1].TARGET = [Mouse_x, Mouse_y]

            for b2 in range(b1 + 1, len(balls)):
                if balls[b1] == balls[b2]: continue
                distance = math.sqrt((balls[b1].rect.x - balls[b2].rect.x) ** 2 +
                                     (balls[b1].rect.y - balls[b2].rect.y) ** 2)
                if distance < 1 * ball_size:
                    balls[b1].FLASHING = 4
                    balls[b2].FLASHING = 4
                    # balls[b1].change_direction(x=True,y=True)
                    # balls[b2].change_direction(x=True,y=True)
                    balls[b1].set_target()
                    balls[b2].set_target()

        if NEED_NEW_TRG:
            NEED_NEW_TRG = False

        pygame.display.flip()
        screen.fill(black)
        time.sleep(50/1000)
