import random

with open('size_grid.txt', 'r') as file:
    # Считываем строки без символов переноса строки \n
    lines = file.read().splitlines()
    #print(lines)
    inp_w = lines[0]
    inp_h = lines[1]
    inp_it = lines[2]


w=int(inp_w)
h=int(inp_h)
it=int(inp_it)

def cell_first(w, h):
    if w<8 or h < 8:
        print("Ошибка: поле слишком маленькое. Значение ширины и высоты поля должны быть более 8")
        return None

    cx = w // 2 # центр
    cy =  h // 2

    rand_a = random.randint(1, cx-2)
    rand_b = random.randint(1, cy-3)

    radius = random.choice([rand_a, rand_b])  # выбираем случайный радиус

    field = [[0 for i in range(w)] for i in range(h)]
    #print(field)

    for y in range(h):
        for x in range(w):
            # расстояние от центра
            dist = abs(x - cx) + abs(y - cy)

            # если клетка попадает в радиус — делаем её 1
            if dist <= radius:
                field[y][x] = 1



    return field




