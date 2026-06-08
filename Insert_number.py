test_cases = int(input())

for item in range(test_cases):
    n, d = map(int, input().split())
    num = str(input())
    
    print(n, d)
    print(num)
    
    list_int =[int(value_str) for value_str in num ]
    
    #print(list_int)
    
    for ind in range(len(list_int)):# если d больше значения из списка, вставить по этому индексу
        if d>list_int[ind]:
            list_int.insert(ind, d)
            break
    else:
        list_int.append(d) # если if не выполнился, вставить в конце списка
    
    #print(list_int)
    
    list_str = [str(value_int) for value_int in  list_int]
    #print(list_str)
    
    result = "".join(list_str)
    print(result)
    
  