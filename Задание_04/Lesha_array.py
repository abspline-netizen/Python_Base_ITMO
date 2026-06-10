n = int(input())
array = list(map(int, input().split()))

if sum(array) != 0:
    print("YES")
    print(1)
    print(1, n)
else:
    pref_sum = 0
    found_cut = False

    for item in range(n - 1):
        pref_sum += array[item]

        if pref_sum != 0:
            print("YES")
            print(2)
            print(1, item + 1)
            print(item + 2, n)
            found_cut = True
            break

    if not found_cut:
        print("NO")

