num = int(input())
comp = set()
for _ in range(num):
    name, status = input().split()
    if status == "enter":
        comp.add(name)
    else:
        comp.discard(name)

comp = sorted(list(comp), reverse=True)
for i in comp:
    print(i)
