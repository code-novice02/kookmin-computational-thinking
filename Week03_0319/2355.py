import math

a, b = map(int, input().split(' '))
print(int((a + b) * (abs(a - b) + 1) / 2))
