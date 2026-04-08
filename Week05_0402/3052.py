a = []
for i in range(10):
    a.append(int(input()))
    
b = []
for i in range(10):
    b.append(a[i] % 42)
b = list(set(b))

print(len(b))
