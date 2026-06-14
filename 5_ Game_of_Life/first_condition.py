import random
w=20 #fild width
h=20 #fild height

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

