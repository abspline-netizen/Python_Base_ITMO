from reader_csv_dict import short_market_list
from users_action import user_action
import math
ALL_DATA = short_market_list
# print(ALL_DATA)


def radius_coord(lat, lon, radius_miles = 100 ):

    R = 3958.8
    rad_dist = radius_miles / R

    min_lat = lat - math.degrees(rad_dist)
    max_lat = lat + math.degrees(rad_dist)

    delta_lon = math.degrees(rad_dist / math.cos(math.radians(lat)))

    min_lon = lon - delta_lon
    max_lon = lon + delta_lon

    return min_lon, max_lon, min_lat, max_lat

def fmid_to_coord (fmid, radius_miles ):

    for i in ALL_DATA:
        if fmid == i[0]:
            point_lon = float(i[7])
            point_lat = float(i[6])
            print(point_lat, point_lon)
            point_coord_range  = radius_coord(point_lat, point_lon, radius_miles)
            return point_coord_range #возвращает список с диапазоном координат (4 значения), кот относятся к fmid


def coord_to_market(point_coord_range): #список с 4 значениями
    min_lon, max_lon, min_lat, max_lat = point_coord_range
    for item in ALL_DATA:
        if item[6].strip() == '' or item[7].strip() == '':
            continue

        lon = float(item[7])
        lat = float(item[6])
        if min_lon<lon<max_lon and min_lat<lat<max_lat:
            print(', '.join(item))
            return

# d = fmid_to_coord('1019847', 100)
# print(f'd {d}')
# g = coord_to_market(d)
# print(g)

def zip_fn():
   print(f"\t ===============================")
   print(f'\tПоиск по ZIP коду')
   print(f"\tend - выход из команды")
   while True:
       inp = str(input('Введите ZIP код для поиска: '))
       if inp.lower() == 'end':
           break

       if len(inp) ==5 and inp.isdigit():
           print(f'Вы ввели {inp}')

           for line in ALL_DATA: # прошли по всем строкам данных
                if inp == line[5]: # если введеное равно значению первого индекса


                    print(
                        f'ZIP Code {inp} относиться к населенному пункту {line[2]}, штат {line[3]}, Market: {line[1]} '
                         )
                    break
           else:
               print('Не найдено!')
               continue
       else:
           print('Ошибка ввода')
           continue
# a = zip_fn()
# print(a)

def city_st_fn():
    print(f"\t ===============================")
    print(f'\t Поиск по городу и штату')
    print(f"\t end - exit from command")


    while True:
        list_cs = []
        inp_city = input('ВВедите название города для поиска: ')
        print(inp_city)

        if inp_city.lower() == 'end':
            break

        if not inp_city.replace(' ', '').isalpha():
            print('Ошибка ввода названия города')
            continue

        inp_city = inp_city.lower().title()
        list_cs.append(inp_city)


        while True:
            inp_state = input('Введите название штата: ')
            print(inp_state)

            if not (inp_state.replace(' ', '').isalpha()):
                print('Ошибка ввода названия штата')
                continue

            inp_state = inp_state.lower().title()
            list_cs.append(inp_state)
            break

        mr_list = []
        line_str = ''
        for line in ALL_DATA:
            if len(line)>=6:
                if (line[2]==list_cs[0]) and (line[3]==list_cs[1]):
                    mr_result=line[1]
                    mr_list.append(mr_result)
                    fmid = line[1]
                    print(f'fmid = {fmid}, mr_result = {mr_result}')
                    mr_list.append(fmid)
                    for item in line:
                        line_str += item



        if len(mr_list)>0:
            # zip_str = ", ".join(str(item) for item in mr_list)
            print(f'Market: {mr_list[0]}, {inp_city}, {inp_state} ')

        else:
            print('Do not found Market')
            break


        while True:
                m_info = input(f'\t\t  Доступные расширенные команды в поиске по городу и штату:  \n'
                               f"\t\t  ---------------------------- \n"
                               f'\t\t  m or more - больше информации о рынке \n'
                               f'\t\t  r or rad - поиск других рынков в радиусе 30 миль \n'
                               f'\t\t  d or dif - поиск других рынков в заданном пользователем радиусе, миль (например, 50) \n'
                               f'\t\t  k or keep - продолжить работу с основной командой поиска по городу и штату \n'
                               f'\t\t  end - выход из команды \n'
                               f"\t\t  ---------------------------- \n"
                               f"\t\t  u or user - добавить отзыв на найденный рынок \n"
                               f"\t\t  ---------------------------- \n"
                               f'\t\t  Введите команду => ')

                if m_info.lower() in ('m', 'more'):
                    print(line_str)

                elif m_info.lower() in ('r', 'rad'):
                    # radius_mails = 30
                    # fmid = mr_list[1]
                    # search_range = fmid_to_coord(fmid, radius_mails) #спислок с 4 координатами на выходе
                    # markets_in_radius = coord_to_market(search_range)
                    # print(markets_in_radius)
                    print("Выводит рынки на фиксированном расстоянии от заданного 30 миль")
                    pass

                elif m_info.lower() in ('d', 'dif'):
                    # radius_mails = int(input('Enter radius mails(exemple, 50): '))
                    # fmid = mr_list[1]
                    # search_range = fmid_to_coord(fmid, radius_mails) #спислок с 4 координатами на выходе
                    # markets_in_radius = coord_to_market(search_range)
                    # print(markets_in_radius)
                    print("Выводит рынки - расстоянии задает пользователь")
                    pass



                elif m_info.lower() in ('k', 'keep'):
                    break

                elif m_info.lower() in ('end'):
                    break

                elif m_info.lower() in ('u', 'user'):
                    var=user_action(fmid)
                    print(var)





 # b = city_st_fn()
 # print(b)
# if __name__ == '__main__':
#     short_market_list