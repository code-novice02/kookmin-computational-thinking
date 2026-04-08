num = int(input())

dots = list(map(int, input().split(" ")))
dots.sort()
distance_sum = 0

for i in range(num):
    distance_sum += (dots[i] * i) - ((num - 1 - i) * dots[i])

print(distance_sum * 2)
