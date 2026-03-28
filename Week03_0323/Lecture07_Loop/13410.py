def reverseMt(n):
    reverse_n = int(str(n)[::-1])
    return reverse_n

n, k = map(int, input().split())
mt = []
for i in range(k):
    mt.append(n * (i + 1))
mt_len = len(mt)
for i in range(mt_len):
    mt[i] = reverseMt(mt[i])
print(max(mt))
