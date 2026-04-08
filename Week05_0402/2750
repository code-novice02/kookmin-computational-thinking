num = int(input())
arr = []
for _ in range(num):
    arr.append(int(input()))

for i in range(num - 1):
    for j in range(i, num):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
for i in arr:
    print(i)
