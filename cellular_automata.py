import pygame
import random
import sys
from pygame.locals import *

import box

# 定义窗口宽高
win_width = 800
win_height = 800
row_cell_num = 160
# 初始状态活的单元数量
life_num = 4800


# 绘图
def draw(win, cells: [box.Cell]):
    for cell in cells:
        if cell.value == 0:
            color = (255, 255, 255)
        else:
            color = (0, 0, 0)
        pygame.draw.rect(win, color, pygame.Rect(
            cell.x,
            cell.y,
            cell.width,
            cell.height,
        ))


def run():
    # 是否完成了初始化绘图
    init = False
    # 控制暂停
    change_start = True
    pygame.init()
    # 初始化容器
    box_control = box.Box(row_cell_num, row_cell_num, win_width, win_height)
    # 初始化活的单元
    if life_num > 0:
        for i in range(0, life_num):
            row, col = random.randint(0, box_control.row_num - 1), random.randint(0, box_control.col_num - 1)
            box_control.cells[row][col].value = 1

    # 初始化窗口
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('Cellular Automata')
    clock = pygame.time.Clock()

    while True:
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                # 支持按空格暂停/恢复状态变更
                change_start = not change_start
        if not init:
            # 初始化
            init = True
            all_cells = box_control.get_all_cells()
            draw(win, all_cells)
        else:
            if change_start:
                update_cells = box_control.flush()
                draw(win, update_cells)
        pygame.display.update()


if __name__ == '__main__':
    # 启动程序
    run()
