import numpy as np
from copy import deepcopy

class game_state:
    def __init__(self, x, y):
        self.size_x = x
        self.size_y = y
        self.state = np.zeros((self.size_x, self.size_y), dtype=bool)
    
    def print_state(self):
        for row in self.state:
            for cell in row:
                print(int(cell), end=" ")
            print()

    def change_state(self, coordinates):
        x, y = coordinates
        if self.state[x][y]:
            self.state[x][y] = 0
        else:
            self.state[x][y] = 1

    def clear_state(self):
        self.state = np.zeros((self.size_x, self.size_y), dtype=bool)
    
    def update_state(self):
        next_state = deepcopy(self.state)
        for i in range(self.size_x):
            for j in range(self.size_y):
                neighbour_coordinates = ((i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1))
                live_cells = 0
                for neighbour in neighbour_coordinates:
                    x, y = neighbour
                    if (0 <= x < self.size_x) and (0 <= y < self.size_y) and self.state[x][y]:
                        live_cells += 1
                if self.state[i][j] == 1:
                    if (0 <= live_cells < 2):
                        next_state[i][j] = 0
                    elif (2 <= live_cells <= 3):
                        next_state[i][j] = 1
                    elif (live_cells > 3):
                        next_state[i][j] = 0
                else:
                    if live_cells == 3:
                        next_state[i][j] = 1
        self.state = deepcopy(next_state)
