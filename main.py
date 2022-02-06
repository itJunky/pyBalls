import random
import math
import time
import sys
import pygame

balls_count = 100
ball_size = 15
pygame.init()
balls = []
black = 0, 0, 0
size = scr_width, scr_height = 1200, 800
screen = pygame.display.set_mode(size)
# "intro_ball.gif"
ball_image_file = "bzz_ball.gif"

class Ball:
    def __init__(self, first_x, first_y, speed=5, bsz=25):
        ball_img = pygame.image.load(ball_image_file).convert_alpha()
        bl_size = (bsz, bsz)
        self.TARGET = [400, 200]
        self.ball_img = pygame.transform.scale(ball_img, bl_size)
        self.speed = [speed, speed]
        if first_x or first_y:
            self.rect = ball_img.get_rect(topleft=(first_x, first_y), size=bl_size)
        else:
            self.rect = ball_img.get_rect(size=bl_size)

    def tick(self):
        self.get_new_coordinates()
        self.check_target()
        self.change_direction()
        screen.blit(self.ball_img, self.rect)

    def change_direction(self):
        if self.rect.left < 0 or self.rect.right > scr_width:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > scr_height:
            self.speed[1] = -self.speed[1]

    def get_new_coordinates(self):
        '''
        Осуществляет сдвиг экземпляра инфузории
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
        elif distance > 0.:
            x = x-Dl*(xk-x)/distance  # Откатываемся назад
            y = y-Dl*(yk-y)/distance  # В случае коллизии

        self.rect.x = int(x)
        self.rect.y = int(y)

    def get_speed(self):
        # TODO change formula
        return abs(self.speed[0])

    def set_target(self):
        self.TARGET = [random.randint(1, scr_width - ball_size),
                       random.randint(1, scr_height - ball_size)
        ]

    def check_target(self):
        distance = math.sqrt((self.TARGET[0] - self.rect.x) ** 2 + (self.TARGET[1] - self.rect.y) ** 2)
        if distance <= ball_size:  # Если текущая еда ближе чем предыдущая ближайшая
            self.set_target()


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

        for ball in balls:
            ball.tick()
            if NEED_NEW_TRG:
                ball.TARGET = [Mouse_x, Mouse_y]

        if NEED_NEW_TRG:
            NEED_NEW_TRG = False

        pygame.display.flip()
        screen.fill(black)
        time.sleep(20/1000)
