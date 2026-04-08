num = int(input())
for i in range(num):
    mark = input()
    score = 0
    seq = 0
    for j in mark:
        if j == "O":
            seq += 1
            score += seq
        else:
            seq = 0
    print(score)
