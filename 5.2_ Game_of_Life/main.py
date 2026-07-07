from first_condition import grid, w, h
from PIL import Image, ImageDraw
from graphic import visualize_grid
import numpy as np
import time

while True:
    it=input(f"Введите целое число количества итераций: ")
    if  it.isdigit():
        it=int(it)
        break
    print("Ошибка. Введите целое число итераций" )



def print_grid(grid):
    for row in grid:
        print(*row)


def step_life(grid):
    padded = np.pad(grid, 1)
    neighbors = sum(
        padded[i:i+grid.shape[0], j:j+grid.shape[1]]
        for i in (0,1,2)
        for j in (0,1,2)
        if not (i == 1 and j == 1)
    )

    new_grid = ((grid == 1) & ((neighbors == 2) | (neighbors == 3))) | \
               ((grid == 0) & (neighbors == 3))
    new_grid = new_grid.astype(int)

    return new_grid

def grid_to_tuple(grid):
    return tuple(tuple(int(x) for x in row) for row in grid)

grid_np = np.array(grid)

print_grid(grid_np)

previous_states = {grid_to_tuple(grid_np)}

visual_steps = it
for step in range(visual_steps):

        grid_np= step_life(grid_np)
        print_grid(grid_np)
        visualize_grid(grid_np.tolist(), f'step_{step+1}.png')
        time.sleep(1)

        current_state = grid_to_tuple(grid_np)
        if current_state in previous_states:
            print(f'\n️ Стоп! Повтор состояния {step+1}!')
            print(f'Программа остановлена.')
            break

        previous_states.add(current_state)
print('Готово!')


