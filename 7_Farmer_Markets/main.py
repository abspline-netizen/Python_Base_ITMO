from reader_csv_dict import displ_fn
from seacher import zip_fn, city_st_fn, fmid_to_coord, coord_to_market
from reader_csv_dict import short_market_list


def main():
    while True:

        user_typing = input(f"  Доступные команды:\n"
                            f"list - список всех рынков \n"
                            f"find - найти рынок по городу и штату \n"
                            f"end - выход из программы \n"
                            f"===================================== \n"
                            f"Выполните ввод команды =>: ")

        if not (user_typing=='list' or user_typing=='find'  or user_typing=='end'):
            print('Ошибка. Введена неизвестная команда')
            print()
            continue

        if user_typing == 'list':

            current_page = 0
            divider=10

            current_page = displ_fn(current_page, divider, "n")
            print(f"Это страница номер: {current_page}")
            print(f'Количество строк в одной странице: {divider} ')

            while True:
                user_typing2 = input(f" Команда list. Просмотр информации о фермерских рынках.\n"
                                f"===================================== \n"
                                f"Доступны следующие действия: \n"
                                f"n or next - следующая страница \n"
                                f"p or prev - предыдущая страница \n"
                                f"s or start - первая страница \n"
                                f"l or last - последняя страница \n"
                                f"d or divid - количество строк в одной странице (по умолчанию 10) \n"
                                f"t or to - перейти на страницу \n"                                
                                f"end - выход из команды list \n"
                                f"===================================== \n"
                                f"Выполните ввод команды =>: ")


                if user_typing2 in ("n", "next"):
                    click = 'n'
                    current_page = displ_fn(current_page, divider, click)
                    print(f"Текущая страница: {current_page}")

                elif user_typing2 in ("p", "prev"):
                    click = 'p'
                    current_page = displ_fn(current_page, divider, click)
                    print(f"Текущая страница: {current_page}")

                elif user_typing2 in ("s", "start"):
                    click = 's'
                    current_page = displ_fn(current_page, divider, click)
                    print(f"Это первая страница: {current_page}")

                elif user_typing2 in ("l", "last"):
                    click = 'l'
                    current_page = displ_fn(current_page, divider, click)
                    print(f"Это последняя страница: {current_page}")

                elif user_typing2 in ("d", "divid"):
                    try:
                        divider = int(input("Введите количество строк на странице: "))
                        print(f"Установлено {divider} строк на странице")
                        current_page = displ_fn(current_page, divider, "n")
                    except ValueError:
                        print("Ошибка: введите число")

                elif user_typing2 in ("t", "to"):
                    try:
                        page = int(input("Введите номер страницы: "))
                        current_page = page-1 #n прибавляет 1 далее
                        current_page = displ_fn(current_page, divider, "n")
                        print(f"Переход на страницу {current_page}")
                    except ValueError:
                        print("Ошибка: введите число")

                elif user_typing2 == 'end':
                    print('Выход из команды list')
                    break  # Выход из внутреннего цикла, возврат в главное меню

                else:
                    print('Ошибка. Введена неизвестная команда')
                    print()


        elif user_typing == 'find':
            print('find')

            if user_typing == 'find':

                while True:
                    user_typing3 = input(f" Команда find. Поиск информации о фермерских рынках.\n"
                                f"Доступны следующие действия: \n"
                                f"z or zip - поиск по zip коду \n"
                                f"c or city - поиск по городу и штату \n"                                                          
                                f"end - выход из команды list \n"
                                f"===================================== \n"
                                f"Выполните ввод команды =>: ")

                    if user_typing3 in ("z", "zip"):

                        zip_res = zip_fn()
                        print(f"Результаты поиска: {zip_res}")

                    if user_typing3 in ("c", "city"):
                        print(f'Для отладки: {short_market_list[5]}')
                        print(f'Для отладки: {short_market_list[12]}')
                        print(f'Для отладки: {short_market_list[20]}')
                        city_result = city_st_fn()
                        print(f"Результаты поиска: {city_result}")

                    else:
                        print('Ошибка. Введена неизвестная команда')
                        print()



        elif user_typing == 'end':
            print('end')
            print('Работа программы завершена')
            return 0

        else:
            print('Please enter a valid input')
            print('use "end" for exit')

while True:
    result = main()
    if result == 0:
        break