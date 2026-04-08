arr = []
for i in range(9):
    x = int(input())
    arr.append(x)
m = max(arr)
print(m)
print(arr.index(m)+1)
