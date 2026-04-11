import sys

inputs = sys.stdin.readline().split()
able = int(inputs[0])
list_length = int(inputs[1])
order = {}
for i in range(list_length):
    stu_id = sys.stdin.readline().strip()
    order[stu_id] = i
order = sorted(order.items(), key = lambda x: x[1])

final = min(len(order), able)
for i in range(final):
    print(order[i][0])
