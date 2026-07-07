from PIL import Image, ImageDraw
from first_condition import w,h

CELL_SIZE = 20

def fild_init (width, height): #game begin from fild building (width, height)
    img_fild = Image.new(mode = 'RGB', size=(width, height), color = (144,83,32))

    #img_fild.save('fild_print.png')
    return img_fild

#fild_visual = fild_init(w, h)


def cell_img_l(): # size of cell and color (width, height) l_ d_ - life and died colors
    c_life = Image.new(mode='RGB', size=(20, 20), color=(99, 255, 180))
    draw = ImageDraw.Draw(c_life)
    draw.rectangle([0, 0, CELL_SIZE-3, CELL_SIZE-3], outline=(255, 255, 255), width=1)
    #c_life.save('c_life.png')
    return c_life

#c_life = cell_img_l()

def cell_img_d(): # size of cell and color (width, height) l_ d_ - life and died colors
    c_died = Image.new(mode='RGB', size=(20, 20), color=(91, 156, 68))

    #c_died.save('c_died.png')
    return c_died

#c_died = cell_img_d()




def visualize_grid(grid, filename='output.png'):

    c_life = cell_img_l()
    c_died = cell_img_d()

    # Создаем новое поле
    fild_visual = fild_init(w*CELL_SIZE, h*CELL_SIZE)

    # Рисуем каждую клетку
    for y in range(h):
        for x in range(w):
            x_pos = x * CELL_SIZE
            y_pos = y * CELL_SIZE

            if grid[y][x] == 1:
                fild_visual.paste(c_life, (x_pos, y_pos))
            else:
                fild_visual.paste(c_died, (x_pos, y_pos))

    fild_visual.save(filename)
    return fild_visual

