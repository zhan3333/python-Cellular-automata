import pygame, sys, random
import box_control
from pygame.locals import *

win_width = 800
win_height = 800
box_num = 160
life_num = 4800
change_start = True

pygame.init()
boxs = box_control.init_boxs(box_num, win_width, win_height, life_num)
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('zhan')
clock = pygame.time.Clock()


def flush_box(box_color, rect):
    pygame.draw.rect(win, box_color, rect)


def get_random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


while True:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            change_start = not change_start

    if change_start:
        for x in range(0, box_num):
            for y in range(0, box_num):
                if boxs[x][y]['value'] == 0:
                    color = (255, 255, 255)
                else:
                    color = (0, 0, 0)
                    # color = get_random_color()
                flush_box(color,
                          pygame.Rect(
                              boxs[x][y]['x'],
                              boxs[x][y]['y'],
                              boxs[x][y]['width'],
                              boxs[x][y]['height'],
                          ))
        box_control.change_boxs(boxs)

    pygame.display.update()