def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

n = int(input("input N: "))
m = int(input("input M: "))
print(f"{n}과 {m}의 최대 공약수는 {gcd(n, m)}입니다.")
