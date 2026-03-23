h, m = map(int, input().split())
c = int(input())

t = h*60+m + (c//60)*60+c%60

print((t//60)%24, t%60)
