from zip_util import read_zip_all
import math

ALL_DATA=read_zip_all()
#print(ALL_DATA[0])
#print(ALL_DATA[20])

def decimal_to_dms(decimal):
    degrees = int(decimal)
    minutes_float = abs(decimal - degrees) * 60
    minutes = int(minutes_float)
    seconds = (minutes_float - minutes) * 60

    return abs(degrees), minutes, round(seconds, 2)

def loc_fn():
   print('loc')
   while True:
       inp = str(input('Enter a ZIP Code to lookup: '))
       if inp.lower() == 'end':
            break

       if len(inp) ==5 and inp.isdigit():
           print(f'Вы ввели {inp}')

           for line in ALL_DATA: # прошли по всем строкам данных
                if inp == line[0]: # если введеное равно значению первого индекса

                    latitude_dms = decimal_to_dms(float(line[1]))
                    longitude_dms = decimal_to_dms(float(line[2]))
                    lat_deg, lat_min, lat_sec = latitude_dms # распаковка кортежа для печати
                    lon_deg, lon_min, lon_sec = longitude_dms

                    print(
                        f'ZIP Code {inp} is in {line[3]}, {line[4]}, {line[5]},\n'
                        f'coordinates '
                        f'({lat_deg:03d}° {lat_min}\' {lat_sec}" N, '
                        f'{lon_deg:03d}° {lon_min}\' {lon_sec}" W)'
                         )
                    break
           else:
               print('Не найдено!')
       else:
           print('Ошибка ввода')

def zip_fn():
    print('zip')


    while True:
        list_cs = []
        inp_city = input('Enter a city name to lookup: ')
        print(inp_city)

        if inp_city.lower() == 'end':
            break

        if not inp_city.replace(' ', '').isalpha():
            print('Ошибка ввода названия города')
            continue

        inp_city = inp_city.lower().title()
        list_cs.append(inp_city)


        while True:
            inp_state = input('Enter the state name to lookup: ')
            print(inp_state)

            if not (inp_state.isalpha() and len(inp_state) == 2):
                print('Ошибка ввода названия штата')
                continue

            inp_state = inp_state.upper()
            list_cs.append(inp_state)
            break

        zip_list = []
        for line in ALL_DATA:
            if len(line)>=4:
                if (line[3]==list_cs[0]) and (line[4]==list_cs[1]):
                    zip_result=line[0]
                    zip_list.append(zip_result)

        if len(zip_list)>0:
            zip_str = ", ".join(str(item) for item in zip_list)
            print(f'The following ZIP Code(s) found for {inp_city}, {inp_state}: {zip_str}')
        else:
            print('Do not found ZIP Code')

        return zip_list

def hv_dist_miles(lat1, lon1, lat2, lon2): #определение расстояния меджу точками
    R = 3958.8 # Средний радиус Земли в милях

    phi1 = math.radians(lat1) # Перевод координат из градусов в радианы
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Формула гаверсинусов
    a = (math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Кратчайшее расстояние
    distance = R * c
    return distance

def dist_fn():
    print('dist')
    while True:
        zip_first = str(input('Enter the first ZIP Code: '))
        print(zip_first)

        if zip_first.lower() == 'end':
            break

        if not (zip_first.isdigit() and len(zip_first) == 5):
            print('Check input first zip code (5 digit)')
            continue

        while True:
            zip_second = str(input('Enter the second ZIP Code: '))
            print(zip_second)

            if zip_second.lower() == 'end':
                break

            if not (zip_second.isdigit() and len(zip_second) == 5):
                print('Check input second zip code (5 digit)')
                continue
            break

        zip_list = []

        found1 = False
        for line in ALL_DATA:
            if zip_first == line[0] and len(line)>=2:
                zip_list.append(line[1])
                zip_list.append(line[2])
                found1 = True
                break

        found2 = False
        for line in ALL_DATA:
            if zip_second == line[0] and len(line)>=2:
                zip_list.append(line[1])
                zip_list.append(line[2])
                found2 = True
                break

        if not found1:
            print('Do not found first coordinate')

        if not  found2:
            print('Do not found second coordinate')


        print(zip_list, type(zip_list[0]))
        dist_result = hv_dist_miles(zip_list[0], zip_list[1], zip_list[2], zip_list[3])

        print(f'The distance between {zip_first} and {zip_second} is {dist_result:.2f} miles')


#a=dist_fn()
#print(a)