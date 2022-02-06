import random
import math
import time
import sys
import pygame

balls_count = 10
ball_size = 15
pygame.init()
balls = []
black = 0, 0, 0
size = scr_width, scr_height = 400, 400
screen = pygame.display.set_mode(size)


class Ball:
    def __init__(self, first_x, first_y, speed=5, bsz=25):
        ball_img = pygame.image.load("intro_ball.gif").convert_alpha()
        bl_size = (bsz, bsz)
        self.TARGET = [scr_width, scr_height]
        self.ball_img = pygame.transform.scale(ball_img, bl_size)
        self.speed = [speed, speed]
        if first_x or first_y:
            self.rect = ball_img.get_rect(topleft=(first_x, first_y), size=bl_size)
        else:
            self.rect = ball_img.get_rect(size=bl_size)

    def show(self):
        self.get_new_coordinates()
        self.change_direction()
        # self.rect = self.rect.move(self.speed)
        screen.blit(self.ball_img, self.rect)

    def change_direction(self):
        if self.rect.left < 0 or self.rect.right > scr_width:
            self.speed[0] = -self.speed[0]
            return True

        if self.rect.top < 0 or self.rect.bottom > scr_height:
            self.speed[1] = -self.speed[1]
            return True

        return False

    def get_new_coordinates(self):
        '''
        Осуществляет сдвиг экземпляра инфузории
        '''
        x = self.rect.x
        y = self.rect.y
        xk = self.TARGET[0]  # координаты цели
        yk = self.TARGET[1]
        Dl = self.get_inf_speed()
        distance = math.sqrt((xk-x)**2+(yk-y)**2)
        if distance > 0.:
            x = x+Dl*(xk-x)/distance  # Считаем насколько надо сдвинуться по Х
            y = y+Dl*(yk-y)/distance  # По Y
        elif distance > 0.:
            x = x-Dl*(xk-x)/distance  # Откатываемся назад
            y = y-Dl*(yk-y)/distance  # В случае коллизии

        self.rect.x = int(x)
        self.rect.y = int(y)

    def get_inf_speed(self):
        # TODO change formula
        return abs(self.speed[0])


# Start main circle of program
if __name__ == '__main__':
    name = 'Baller'
    print(f'Hi, {name}')

    for i in range(balls_count):
        balls.append(Ball(
            random.randint(1, scr_width-ball_size),
            random.randint(1, scr_height-ball_size),
            random.randint(1, 9),
            bsz=ball_size)
        )

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        for ball in balls:
            ball.show()

        pygame.display.flip()
        screen.fill(black)
        time.sleep(20/1000)
