n = int(input())
dot = 4
for i in range(n):
    if i == 0:
        dot = 2 * dot + 1
    else:
        side = pow(2, i)
        # inside + side - 1(□) + last side (┛)
        dot += pow(side, 2) + 2 * pow(side - 1, 2) + 2 * (side - 1)
        # outside
        dot += pow(2, i) * 4
print(dot)
