from first_condition import w, h,  cell_first
from PIL import Image, ImageDraw
from graphic import visualize_grid
import numpy as np
import time

def print_grid(grid):
    for row in grid:
        print(*row)

def step_life(grid):
    neighbors = (
        np.roll(grid, 1, 0) + np.roll(grid, -1, 0) +
        np.roll(grid, 1, 1) + np.roll(grid, -1, 1) +
        np.roll(np.roll(grid, 1, 0), 1, 1) +
        np.roll(np.roll(grid, 1, 0), -1, 1) +
        np.roll(np.roll(grid, -1, 0), 1, 1) +
        np.roll(np.roll(grid, -1, 0), -1, 1)
    )

    new_grid = np.where( (grid == 1) & ((neighbors == 2) | (neighbors == 3))  , 1, 0) #if cell =1 (alive) and neigb.= 2 or 3 use 1, else 0

    new_grid = np.where(  (grid == 0) & (neighbors == 3)  , 1, new_grid) #new cell created
    return new_grid

def grid_to_tuple(grid): #to compared
    return tuple(grid.flatten())




grid_np = np.array(cell_first(w, h))

print_grid(grid_np)

previous_states = {grid_to_tuple(grid_np)}

visual_steps = 10
for step in range(visual_steps):

        grid_np= step_life(grid_np)
        print_grid(grid_np)
        visualize_grid(grid_np.tolist(), f'step_{step}.png')
        time.sleep(1)

        current_state = grid_to_tuple(grid_np)
        if current_state in previous_states:
            print(f'\n️ Стоп! Повтор состояния {step}!')
            print(f'Программа остановлена.')
            break

        previous_states.add(current_state)
print('Готово!')


