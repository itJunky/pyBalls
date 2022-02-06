import random
import time

import pygame, sys

pygame.init()
black = 0, 0, 0
size = width, height = 1000, 800
screen = pygame.display.set_mode(size)


class Ball:
    def __init__(self, first_x, first_y, speed=5):
        ball_img = pygame.image.load("intro_ball.gif").convert_alpha()
        bsz = 25
        bl_size = (bsz, bsz)
        self.ball_img = pygame.transform.scale(ball_img, bl_size)
        self.speed = [speed, speed]
        if first_x or first_y:
            self.rect = ball_img.get_rect(topleft=(first_x, first_y))
        else:
            self.rect = ball_img.get_rect(size=bl_size)

    def show(self):
        self.rect = self.rect.move(self.speed)
        self.change_direction() # if needed
        screen.blit(self.ball_img, self.rect)


    def change_direction(self):
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]


# Start main circle of program
if __name__ == '__main__':
    name = 'Baller'
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    balls = []
    for i in range(30):
        balls.append(Ball(random.randint(1, width-100), random.randint(1, height-100), random.randint(1, 9)))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        for ball in balls:
            ball.show()

        pygame.display.flip()
        screen.fill(black)
        time.sleep(20/1000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
