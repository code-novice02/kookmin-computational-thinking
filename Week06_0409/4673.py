# 9972 -> 9999
# 9963 -> 10000
cnt = [0] * 9999
start = 1

while(start < 10000):
    num = start
    k_num = num 
    while(num >= 1):
        k_num += num % 10
        num = int(num / 10)
    if k_num < 10000:
        cnt[k_num - 1] += 1
    start += 1

for i in range(len(cnt)):
    if cnt[i] == 0:
        print(i + 1)
