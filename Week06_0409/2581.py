m = int(input())
n = int(input())
prime = []
for i in range(m, n + 1):
    if i == 1:
        continue
    is_prime = True
    for j in range(2, int(i**(0.5) + 1)):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)
if len(prime) > 0:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)
