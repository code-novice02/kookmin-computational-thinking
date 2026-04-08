num = int(input())

for _ in range(num):
    all_par = input()
    ps = []
    is_vps = "YES"
    for par in all_par:
        if par == "(":
            ps.append(par)
        else:
            if len(ps) == 0 or ps[len(ps) - 1] != "(":
                is_vps = "NO"
                break
            elif ps[len(ps) - 1] == "(":
                ps.pop()
    if len(ps) != 0:
        is_vps = "NO"
    print(is_vps)
