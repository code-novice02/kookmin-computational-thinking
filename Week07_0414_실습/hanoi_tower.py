# times idea
'''
times[n] = 2 * times[n] + 1

~ n-1개 B로 이동: times[n - 1]
n번째 C로 이동: 1
~ n-1개 B에서 C로 이동: times[n - 1]
'''
# moving idea
'''
~ n-1 개 B로 이동: hanoi(n - 1, start, end, mid)
n번째 C로 이동: start -> end
~ n-1 개 B에서 C로 이동: hanoi(n - 1, mid, start, end)

hanoi(n, start, mid, end) =
    hanoi(n - 1, start, end, mid) +
    a -> c +
    hanoi(n - 1, mid, start, end)

base case:
    if n == 1:
        print("{start} -> {end}")
    else:
        hanoi(n - 1, start, end, mid)
        print(f"{start} -> {end})
        hanoi(n - 1, mid, start, end)
'''

cnt = {}
def hanoi_num(n):
    if n in cnt:
        return cnt[n]
    if n == 0:
        cnt[n] = 0
    elif n == 1:
        cnt[n] = 1
    else:
        cnt[n] = 2 * hanoi_num(n - 1) + 1
    return cnt[n]

def hanoi_moving(n, start, mid, end):
    if n == 1:
        print(f"\t{start} -> {end}")
    else:
        # n - 1개를 A -> B
        hanoi_moving(n - 1, start, end, mid)
        # n번째 A -> C
        print(f"\t{start} -> {end}")
        # n-1개를 B -> C
        hanoi_moving(n - 1, mid, start, end)

n = int(input("input floor: "))
print("hanoi moving:")
hanoi_moving(n, "A", "B", "C")
print(f"total moving: {hanoi_num(n)}")
