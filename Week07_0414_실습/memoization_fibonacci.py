cnt = 0
memo = {}
def fibonacci(n):
    global cnt
    cnt += 1
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
        print(memo)
    return memo[n]


n = int(input("N >> "))
print(f"{n}번째 피보나치 수: {fibonacci(n)}")
print(f"총 연산 횟수: {cnt}")
