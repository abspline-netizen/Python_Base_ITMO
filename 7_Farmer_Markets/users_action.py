import csv
from reader_csv_dict import short_market_list


# Запись заголовков в файл
filename = "users_data_file.csv"

# Создаём файл только если его нет
try:
    with open(filename, "r", encoding="utf-8") as fh:
        pass
except FileNotFoundError:
    with open(filename, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
        writer.writerow(["FMID","Market_name","Имя пользователя", "Отзыв о рынке", "Рейтинг рынка"])


def user_action(fmid):
    user_name = input("Ведите имя пользователя: ")
    feadback_m = input("Введите отзыв о рынке: ")
    grate_m = int(input("Поставьте оценку рынку от 1 до 5: "))

    market_name = None

    # Ищем рынок
    for item in short_market_list:
        if item[0] == fmid:
            market_name = item[1]
            break

    if market_name is None:
        print("Такого рынка не найдено")
        return None

    # Добавление отзыва
    with open(filename, "a", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
        writer.writerow([fmid, market_name, user_name, feadback_m, grate_m])

    print("Отзыв сохранен")
    return user_name, feadback_m, grate_m


if __name__ == "__main__":
    a = user_action('1000709')



