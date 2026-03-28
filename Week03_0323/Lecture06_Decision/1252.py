a, b = map(int, input().split())
result = a + b
result = list(str(result))
result.insert(0, '0')
for i in range(len(result) - 1):
    if int(result[len(result) - i - 1]) > 1:
        result[len(result) - i - 1] = int(result[len(result) - i - 1]) - 2
        result[len(result) - i - 2] = int(result[len(result) - i - 2]) + 1
start = False
for i in result:
    if start:
        print(i, end = "")
    else:
        if i != '0':
            start = True
            print(i, end = "")
if not start:
    print('0')
