import math
from Drowning_2_2_into import load_test_data
from Drowning_2_2_main import calculation




def tolerance (var, etalon): #допустимое отклонение
    if abs(var - etalon) <= etalon * 0.01:
        print(f"\t \t Тест пройден успешно. Тестовое время/эталонное время = {var: .2f} / {etalon} ")
    else:
        print(f"\t Тест не пройден. Тестовое время/эталонное время = {var: .2f} / {etalon} ")

#etalons value
timeResque_e = 39.9



datasets = load_test_data()

for i, data in enumerate(datasets, 1):
    result = calculation(*data)   # данные передаются в функцию
    print(f"Набор {i}: время = {result:.2f}")
    tolerance(result, timeResque_e)

