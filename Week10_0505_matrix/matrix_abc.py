# function 1
def multi_matrix(a, b):
    n = len(a)
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

def sum_matrix(a, b):
    n = len(a)
    for i in range(n):
        for j in range(n):
            a[i][j] += b[i][j]
    return a

def multi_sum(a, b, c):
    return sum_matrix(multi_matrix(a, b), c)

# function 3
import random
def make_fill_matrix(n):
    a = [[random.randrange(1, n * n * 10) for _ in range(n)] for _ in range(n)]
    return a

# function 4
def print_matrix(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            print(f"{a[i][j]:6d}", end = " ")
        print()
    print()


# result
n = int(input())

if 1 < n and n <= 5:
    a = make_fill_matrix(n)
    b = make_fill_matrix(n)
    c = make_fill_matrix(n)

    print("A")
    print_matrix(a)       
    print("B")
    print_matrix(b)
    print("C")
    print_matrix(c)
    print("A * B + C")
    print_matrix(multi_sum(a, b, c))
else:
    print("Input Error")
