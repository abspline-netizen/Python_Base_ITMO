from first_condition import grid, w, h
from PIL import Image, ImageDraw
from graphic import visualize_grid
import numpy as np
import time
import csv

while True:
    it=input(f"Введите целое число количества итераций: ")
    if  it.isdigit():
        it=int(it)
        break
    print("Ошибка. Введите целое число итераций" )



def print_grid(grid):
    for row in grid:
        print(*row)

def out_to_csv(all_iterations):
    with open('out_to_csv.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for step_num, grid in enumerate(all_iterations, start=0):
            writer.writerow([f"Step_{step_num}"])
            writer.writerows(grid)
            writer.writerow([])


def step_life(grid):

    alive = grid>0

    padded = np.pad(grid, 1)
    neighbors = sum(
        padded[i:i+grid.shape[0], j:j+grid.shape[1]]
        for i in (0,1,2)
        for j in (0,1,2)
        if not (i == 1 and j == 1)
    )
    new_grid = np.zeros_like(grid)

    dead_mask = alive == False
    birth_mask = (dead_mask) & (neighbors == 3)
    new_grid[birth_mask] = 1
    survive_mask = (alive == True) & ((neighbors == 2) | (neighbors == 3))
    new_grid[survive_mask] = grid[survive_mask] + 1
    print()

    return new_grid

def grid_to_tuple(grid):
    return tuple(tuple(int(x) for x in row) for row in grid)

grid_np = np.array(grid)
print_grid(grid_np)
previous_states = {grid_to_tuple(grid_np)}
visualize_grid(grid_np.tolist(), f'step_0_first_condition.png')

visual_steps = it


all_iterations = []
all_iterations.append(grid_np.copy())


for step in range(visual_steps):

        grid_np= step_life(grid_np)
        print_grid(grid_np)
        visualize_grid(grid_np.tolist(), f'step_{step+1}.png')
        time.sleep(1)
        all_iterations.append(grid_np.copy())

        current_state = grid_to_tuple(grid_np)
        if current_state in previous_states:
            print(f'\n️ Стоп! Повтор состояния {step+1}!')
            print(f'Программа остановлена.')
            break

        previous_states.add(current_state)
print('Готово!')

out_to_csv(all_iterations)


