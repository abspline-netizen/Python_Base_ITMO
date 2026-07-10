import csv

def csv_to_grid(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)

        field=[]
        for row in reader:
            num = [int(i) for i in row]
            field.append(num)

    return field


grid=csv_to_grid('first.csv')

w=len(grid[0])
h=len(grid)
#print(grid, w, h)


