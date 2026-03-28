def starPattern(n):
    if n == 1:
        return "*"
    pattern = []
    for i in range(n):
        f_line = "* " * ((n + 1) // 2)
        s_line = " *" * (n // 2)
        pattern.append(f_line)
        pattern.append(s_line)
    return pattern

n = int(input())
pattern = starPattern(n)

for i in pattern:
    print(i)
