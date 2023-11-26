import numpy as np
import pygame
from utilities import game_state
from gui import *

g = game_state(columns, rows)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
running = True
screen.fill(WHITE)

PAUSE = True

while running:
    draw_grid(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONUP and PAUSE:
            mouse_x, mouse_y = event.pos
            x_coordinate, y_coordinate = find_top_left((mouse_x, mouse_y))
            x_array, y_array = find_rect_in_array((mouse_x, mouse_y))
            if g.state[x_array][y_array]:
                draw_white_rect((x_coordinate, y_coordinate), screen)
            else:
                draw_black_rect((x_coordinate, y_coordinate), screen)
            g.change_state((x_array, y_array))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                PAUSE = False
                g.update_state()
                draw_state(g, screen)
            elif event.key == pygame.K_ESCAPE:
                PAUSE = True
                g.clear_state()
                draw_state(g, screen)
        elif event.type == pygame.MOUSEBUTTONUP:
            PAUSE = True
    
    pygame.display.update()