# input: 110 -> output: 99 >> count ~ tens' digit
num = int(input())
cnt = 0
if num == 1:
    print(1)
else:
    for i in range(1, num + 1):
        if i < 100:
            cnt += 1
        else:
            n = i
            dec = []
            while(n >= 1):
                dec.append(n % 10)
                n = n // 10
            gap = dec[1] - dec[0]
            is_seq = True
            for j in range(1, len(dec) - 1):
                if gap != dec[j + 1] - dec[j]:
                    is_seq = False
            if is_seq:
                cnt += 1
    print(cnt)
