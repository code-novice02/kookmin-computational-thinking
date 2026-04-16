# Peer: 20232041백한별, 20212647이승준

# 현재 Code:
'''
is_valid(board, row, col, num)
solve_sudoku(board)
print_sudoku(board)

argument fixed
'''
# 만약 argument 변경시
'''
solve_sudoku(board)의 is_empty 항목 함수로 분리
  -> 매 호출마다 발생하는 O(N^2) 복잡도 최적화 가능
    -> solve_sudoku의 empty 탐색: O(1)로 감소.
        (미리 구한 empty_idx 탐색)
  OR
  -> empty_idx global 선언 +
     solve_sudoku(board) 내부 find_empty 구현 +
     empty_idx의 index_number, argument로 추가

'''

def is_valid(board, row, col, num):
    # row
    for i in range(9):
        if num == board[row][i]:
            return False
    # col
    for i in range(9):
        if num == board[i][col]:
            return False
    # 3*3 matrix
    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if num == board[i][j]:
                return False
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            # is_empty
            if board[i][j] != 0:
                if i == 8 and j == 8:
                    return True
                else:
                    continue
            else:
                for n in range(1, 10):
                    if is_valid(board, i, j, n):
                        board[i][j] = n
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False

def print_sudoku(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = " ")
        print()


puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if solve_sudoku(puzzle):
    print_sudoku(puzzle)
else:
    print("해답이 없습니다")
