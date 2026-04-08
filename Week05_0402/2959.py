steps = list(map(int, input().split()))
for i in range(len(steps) - 1):
    for j in range(i + 1, len(steps)):
        if steps[i] > steps[j]:
            temp = steps[i]
            steps[i] = steps[j]
            steps[j] = temp
print(steps[0] * steps[2])
