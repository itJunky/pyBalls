import random
import time
import sys
import pygame

balls_count = 10
ball_size = 15
pygame.init()
balls = []
black = 0, 0, 0
size = scr_width, scr_height = 1400, 800
screen = pygame.display.set_mode(size)


class Ball:
    def __init__(self, first_x, first_y, speed=5, bsz=25):
        ball_img = pygame.image.load("intro_ball.gif").convert_alpha()
        bl_size = (bsz, bsz)
        self.ball_img = pygame.transform.scale(ball_img, bl_size)
        self.speed = [speed, speed]
        if first_x or first_y:
            self.rect = ball_img.get_rect(topleft=(first_x, first_y), size=bl_size)
        else:
            self.rect = ball_img.get_rect(size=bl_size)

    def show(self):
        self.rect = self.rect.move(self.speed)
        self.change_direction()  # if needed
        screen.blit(self.ball_img, self.rect)

    def change_direction(self):
        if self.rect.left < 0 or self.rect.right > scr_width:
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > scr_height:
            self.speed[1] = -self.speed[1]


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
