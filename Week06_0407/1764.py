listen, watch = map(int, input().split())

no_listen = set()
no_watch = set()

for _ in range(listen):
    no_listen.add(input())
for _ in range(watch):
    no_watch.add(input())

unknown = sorted(list(no_listen & no_watch))
print(len(unknown))
for i in unknown:
    print(i)
