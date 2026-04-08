num = int(input())
charge = []
right_sum = 0

for i in range(num):
    now = int(input())
    if now == 0:
        right_sum -= charge[len(charge) - 1]
        charge.pop()
    else:
        charge.append(now)
        right_sum += now
print(right_sum)
