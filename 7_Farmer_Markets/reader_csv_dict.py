import csv
import math

def reader_csv(file): #чтение из файла
    with open(file, 'r', newline='') as f:
        content = csv.reader(f)
        rows=list(content)
        #for item in rows:
            #print(item)
            #print()
        return rows

def list_to_dict(rows): #запись в словари
    headers = rows[0]
    dict_market = {}

    for item in rows[1:]:
        key = item[0].strip()
        if not key.isdigit():
            print(f"Error key: {key}")

        inner = {headers[i]: item[i].strip() for i in range(1, len(item))} #генератор словарей
        dict_market[key] = inner

    return dict_market

def dict_to_list(dict_market):
    short_market_list = []
    for k,v in dict_market.items():
        row = [k] + list(v.values())
        short_market_list.append(row)
    return short_market_list


M_FILE_LIST = reader_csv('Export.csv') #глобальные значения для списка и словаря

M_FILE_DICT = list_to_dict(M_FILE_LIST)

def short_market_info(M_FILE_DICT = M_FILE_DICT): #выводит информацию из словаря в список.
    short_market_list = []
    for k, v in M_FILE_DICT.items():  # укороченная информация о рынках
        row = [
            k,
            v['MarketName'],
            v['city'],
            v['State'],
            v['street'],
            v['zip'],
            v['y'], #latitude
            v['x'], #longitude
        ]
        short_market_list.append(row)

    return short_market_list #Список затем подается для работы со страницей


short_market_list = short_market_info()
# print(short_market_list)


def page_bh(curr_page , divider):#поведение страницы - делает срез списка и печатает через пробелы
    cur_list = short_market_list

    total_rows = len(cur_list) - 1  # минус заголовок
    total_pages = math.ceil(total_rows / divider)

    if curr_page < 1:
        curr_page = 1
    elif curr_page > total_pages:
        curr_page = total_pages


    start=1+(curr_page-1)*divider
    end = min(1 + curr_page * divider, len(cur_list))
    displ_vision = cur_list[start:end]

    for i in displ_vision:
        print(", ".join(i))
        print()

    return curr_page

def displ_fn(curr_page, divider = 10, click = "n"): #если получает на вход n p -движется вперед назад

    total_rows = len(short_market_list) - 1 #отнимаем первую строку заголовков
    total_pages = math.ceil(total_rows / divider)

    if click == "n":
        if curr_page < total_pages:
            curr_page += 1
        else:
            print(f"Вы уже на последней странице ({total_pages})")
    elif click == "p":
        if curr_page > 1:
            curr_page -= 1
        else:
            print("Вы уже на первой странице")
    elif click == "s":
        if curr_page != 1:
            curr_page = 1
        else:
            print("Вы уже на первой странице")
    elif click == "l":
        if curr_page != total_pages:
            curr_page = total_pages
        else:
            print("Вы уже на последней странице")

    curr_page = page_bh(curr_page, divider)
    print(f'curr_page: {curr_page}')
    print(f'divider: {divider}')

    return curr_page





