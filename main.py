import time

import pygame, sys

pygame.init()
size = width, height = 800, 600
speed = [2, 2]
speed2 = [3, 3]
speed3 = [4, 4]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball_img = pygame.image.load("intro_ball.gif").convert_alpha()
bl_size = (15, 15)
ball_img = pygame.transform.scale(ball_img, bl_size)
ball = ball_img.get_rect(size=bl_size)

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def show(ballrect, speed):
    # Use a breakpoint in the code line below to debug your script.

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.blit(ball_img, ballrect)
    pygame.display.flip()

    return ballrect, speed


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = 'Baller'
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    ball = ball_img.get_rect(topleft=(100, 350), size=bl_size)
    ball2 = ball_img.get_rect(topleft=(200, 300), size=bl_size)
    ball3 = ball_img.get_rect(topleft=(300, 300), size=bl_size)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ball, speed = show(ball, speed)
        ball2, speed2 = show(ball2, speed2)
        ball3, speed3 = show(ball3, speed3)

        screen.fill(black)
        time.sleep(20/1000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
