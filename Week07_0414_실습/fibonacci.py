cnt = 0
def fibonacci(n):
    global cnt
    cnt += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("N >> "))
print(f"{n}번째 피보나치 수: {fibonacci(n)}")
print(f"총 연산 횟수: {cnt}")
