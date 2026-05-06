# function 2
def transpose_matrix(m):
    n = len(m)
    return [[m[j][i] for j in range(n)] for i in range(n)]

# function 3
import random
def make_fill_matrix(n):
    a = [[random.randrange(1, n * n * 10) for _ in range(n)] for _ in range(n)]
    return a

# function 4
def print_matrix(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            print(f"{m[i][j]:3d}", end = " ")
        print()
    print()

# result
n = int(input())

if 1 < n and n <= 5:
    m = make_fill_matrix(n)

    print("Original Matrix")
    print_matrix(m)
    print("Transposed Matrix")
    print_matrix(transpose_matrix(m))
else:
    print("Input Error")
