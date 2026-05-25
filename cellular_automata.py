import pygame
import random
import sys
from pygame.locals import *

import box

# 定义窗口宽高
grid_width = 800
grid_height = 800
log_panel_width = 280
win_width = grid_width + log_panel_width
win_height = grid_height
row_cell_num = 160
# 初始状态活的单元数量
life_num = 4800
max_log_lines = 40
frame_rate = 60
simulation_interval_ms = 1000
help_button_rect = pygame.Rect(grid_width + 12, 12, 92, 30)
pause_button_rect = pygame.Rect(grid_width + 116, 12, 116, 30)
close_help_rect = pygame.Rect(690, 178, 78, 30)


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


def draw_log_panel(win, font, logs: [str], running: bool):
    pygame.draw.rect(win, (34, 34, 34), pygame.Rect(grid_width, 0, log_panel_width, win_height))
    pygame.draw.line(win, (90, 90, 90), (grid_width, 0), (grid_width, win_height))
    pygame.draw.rect(win, (70, 70, 70), help_button_rect)
    pygame.draw.rect(win, (70, 70, 70), pause_button_rect)
    win.blit(font.render('Help', True, (240, 240, 240)), (help_button_rect.x + 26, help_button_rect.y + 7))
    pause_text = 'Pause' if running else 'Resume'
    win.blit(font.render(pause_text, True, (240, 240, 240)), (pause_button_rect.x + 28, pause_button_rect.y + 7))

    status = 'Running' if running else 'Paused'
    lines = [f'Status: {status}', 'Operation log:'] + logs[-max_log_lines:]
    for index, line in enumerate(lines):
        text = font.render(line, True, (240, 240, 240))
        win.blit(text, (grid_width + 12, 92 + index * 18))


def draw_help(win, font):
    overlay = pygame.Surface((win_width, win_height))
    overlay.set_alpha(170)
    overlay.fill((0, 0, 0))
    win.blit(overlay, (0, 0))

    help_rect = pygame.Rect(230, 150, 560, 420)
    pygame.draw.rect(win, (245, 245, 245), help_rect)
    pygame.draw.rect(win, (55, 55, 55), help_rect, 2)
    pygame.draw.rect(win, (210, 210, 210), close_help_rect)
    pygame.draw.rect(win, (55, 55, 55), close_help_rect, 1)
    win.blit(font.render('Close', True, (20, 20, 20)), (close_help_rect.x + 20, close_help_rect.y + 7))

    lines = [
        'Help',
        '',
        'Conway Game of Life',
        'Each cell is either alive or dead.',
        'The board updates from all cells at the same time.',
        '',
        'Rules',
        '- Alive cell with fewer than 2 neighbors dies.',
        '- Alive cell with 2 or 3 neighbors stays alive.',
        '- Alive cell with more than 3 neighbors dies.',
        '- Dead cell with exactly 3 neighbors becomes alive.',
        '',
        'Controls',
        '- Space: pause or resume simulation.',
        '- Left click a grid cell: toggle alive/dead.',
        '- Esc or Close: close this help window.',
    ]
    for index, line in enumerate(lines):
        color = (20, 20, 20)
        text = font.render(line, True, color)
        win.blit(text, (help_rect.x + 24, help_rect.y + 24 + index * 22))


def run():
    # 是否完成了初始化绘图
    init = False
    # 控制暂停
    change_start = True
    show_help = False
    operation_logs = [
        'Space: pause/resume',
        'Click: toggle cell',
    ]
    pygame.init()
    font = pygame.font.SysFont(None, 22)
    # 初始化容器
    box_control = box.Box(row_cell_num, row_cell_num, grid_width, grid_height)
    # 初始化活的单元
    if life_num > 0:
        for i in range(0, life_num):
            row, col = random.randint(0, box_control.row_num - 1), random.randint(0, box_control.col_num - 1)
            box_control.cells[row][col].value = 1

    # 初始化窗口
    win = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('Cellular Automata')
    clock = pygame.time.Clock()
    last_step_time = pygame.time.get_ticks()

    def toggle_pause(source: str, now_time: int):
        nonlocal change_start, last_step_time
        change_start = not change_start
        status = 'resumed' if change_start else 'paused'
        operation_logs.append(f'{source}: {status}')
        draw_log_panel(win, font, operation_logs, change_start)
        last_step_time = now_time

    while True:
        clock.tick(frame_rate)
        now = pygame.time.get_ticks()
        user_updated_cell = False
        redraw_help = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if show_help and event.type == KEYDOWN and event.key != K_ESCAPE:
                continue
            if event.type == KEYDOWN and event.key == K_SPACE:
                # 支持按空格暂停/恢复状态变更
                toggle_pause('Space', now)
            if event.type == KEYDOWN and event.key == K_ESCAPE and show_help:
                show_help = False
                operation_logs.append('Help: closed')
                draw(win, box_control.get_all_cells())
                draw_log_panel(win, font, operation_logs, change_start)
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if show_help:
                    if close_help_rect.collidepoint(event.pos):
                        show_help = False
                        operation_logs.append('Help: closed')
                        draw(win, box_control.get_all_cells())
                        draw_log_panel(win, font, operation_logs, change_start)
                    continue
                if help_button_rect.collidepoint(event.pos):
                    show_help = True
                    operation_logs.append('Help: opened')
                    draw_log_panel(win, font, operation_logs, change_start)
                    redraw_help = True
                    continue
                if pause_button_rect.collidepoint(event.pos):
                    toggle_pause('Button', now)
                    continue
                # 支持鼠标左键切换指定单元的生死状态
                result = box_control.toggle_cell_at_position(*event.pos)
                if result is not None:
                    cell, row, col = result
                    draw(win, [cell])
                    user_updated_cell = True
                    status = 'alive' if cell.value == 1 else 'dead'
                    operation_logs.append(f'Cell ({row}, {col}) -> {status}')
                    draw_log_panel(win, font, operation_logs, change_start)
                    last_step_time = now
        if not init:
            # 初始化
            init = True
            all_cells = box_control.get_all_cells()
            draw(win, all_cells)
            draw_log_panel(win, font, operation_logs, change_start)
            last_step_time = now
        else:
            if change_start and not show_help and not user_updated_cell and now - last_step_time >= simulation_interval_ms:
                update_cells = box_control.flush()
                draw(win, update_cells)
                draw_log_panel(win, font, operation_logs, change_start)
                last_step_time = now
        if show_help and redraw_help:
            draw_help(win, font)
        pygame.display.update()


if __name__ == '__main__':
    # 启动程序
    run()
