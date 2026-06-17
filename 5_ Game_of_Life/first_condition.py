import random

with open('size_grid.txt', 'r') as file:
    # Считываем строки без символов переноса строки \n
    lines = file.read().splitlines()
    #print(lines)
    inp_w = lines[0]
    inp_h = lines[1]

w=int(inp_w)
h=int(inp_h)

def cell_first(w, h):
    cx = w // 2
    cy =  h // 2  # центр
    rand_a = random.randint(1, 3)
    rand_b = random.randint(5, 8)

    radius = random.choice([rand_a, rand_b])  # выбираем случайный радиус

    field = [[0 for _ in range(w)] for _ in range(h)]
    #print(field)

    for y in range(h):
        for x in range(w):
            # расстояние от центра
            dist = abs(x - cx) + abs(y - cy)

            # если клетка попадает в радиус — делаем её 1
            if dist <= radius:
                field[y][x] = 1

    return field

