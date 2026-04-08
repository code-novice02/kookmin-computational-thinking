num = int(input())

for i in range(num):
    count = 0
    score = list(map(int, input().split()))
    total = sum(score[1:])
    avr = total / score[0]
    for j in range(1, score[0] + 1):
        if (score[j] > avr): count += 1
    print(f"{round(count / score[0] * 100, 3)}%")
