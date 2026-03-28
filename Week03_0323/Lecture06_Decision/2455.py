p_on = [0 for i in range(4)]
for i in range(4):
    off, on = map(int, input().split())
    if i == 0:
        p_on[0] += on
    else:
        p_on[i] = p_on[i - 1] - off + on
print(max(p_on))
