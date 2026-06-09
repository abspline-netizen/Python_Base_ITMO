import math

max_product = []

test_cases=int(input())
for count in range(test_cases):
    num_digit=int(input())
    array=input()

    #print(test_cases)
    #print(num_digit)
    
    array = array.split()
    array = list(map(int, array))
    #print(array)
    #находим минимальный элемент списка
    min_item = min(array)
    index_min = array.index(min_item)
    #заменяем минимальный элемент по индексу
    array[index_min] = min_item+1
    #print(f'{array} минимальный элемент увеличен на 1')
    result = math.prod(array)
    #print(min_item, index_min)
    max_product.append(result)
#print('Максимальные произведения:')
for item in max_product:
    print (item)
            
        
    
    

    