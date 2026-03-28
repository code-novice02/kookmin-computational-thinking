for _ in range(3):        
    arr = list(map(int, input().split(' ')))
    sum = 0
    for i in range(4):
        sum += arr[i]

    if sum == 3:
        print("A")
    elif sum == 2:
        print("B")
    elif sum == 1:
        print("C")
    elif sum == 0:
        print("D")
    elif sum == 4:
        print("E")
