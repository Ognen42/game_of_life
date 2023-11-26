import numpy as np
import pygame
from utilities import game_state

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_HEIGHT = 1080
WINDOW_WIDTH = 1080
square_side_length = 24
rows = WINDOW_HEIGHT // square_side_length
columns = WINDOW_WIDTH // square_side_length

def find_top_left(mouse_coordinates):
    mouse_x, mouse_y = mouse_coordinates
    x = int(mouse_x - (mouse_x % square_side_length))
    y = int(mouse_y - (mouse_y % square_side_length))
    return (x, y)

def find_rect_in_array(coordinates):
    x, y = coordinates
    return (x // square_side_length, y // square_side_length)

def draw_black_rect(coordinates, screen):
    x_coordinate, y_coordinate = coordinates
    rect = pygame.Rect(int(x_coordinate), int(y_coordinate), 20, 20)
    pygame.draw.rect(screen, BLACK, rect, width=0)
    
def draw_white_rect(coordinates, screen):
    x_coordinate, y_coordinate = coordinates
    rect = pygame.Rect(int(x_coordinate), int(y_coordinate), 20, 20)
    pygame.draw.rect(screen, WHITE, rect, width=0)

def draw_grid(screen):
    for x in range(WINDOW_WIDTH // square_side_length):
        for y in range(WINDOW_HEIGHT // square_side_length):
            rect = pygame.Rect(x * square_side_length, y * square_side_length, square_side_length, square_side_length)
            pygame.draw.rect(screen, WHITE, rect, 1)

def draw_state(g, screen):
    for i in range(columns):
        for j in range(rows):
            if g.state[i][j]:
                draw_black_rect((i * square_side_length, j * square_side_length), screen)
            else:
                draw_white_rect((i * square_side_length, j * square_side_length), screen)