h, m, s = map(int, input().split(' '))
oven = int(input())

s += oven % 60
oven  = oven // 60
if s > 59:
    m += s // 60
    s = s % 60

m += oven % 60
oven = oven // 60
if m > 59:
    h += m // 60
    m = m % 60

h += oven % 24
if h > 23:
    h -= 24

print(h, m, s)
