import random
import copy

def is_safe(board, row, col, num):
    # Check row and column
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    # Check 3x3 box
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_safe(board, i, j, num):
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def fill_grid(board):
    nums = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                random.shuffle(nums)
                for num in nums:
                    if is_safe(board, i, j, num):
                        board[i][j] = num
                        if fill_grid(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def generate_puzzle(removal_count=40):
    board = [[0] * 9 for _ in range(9)]
    fill_grid(board)
    full_board = copy.deepcopy(board)

    count = 0
    while count < removal_count:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            count += 1

    return board, full_board  # Puzzle, and the full solution (optional)

if __name__ == "__main__":
    puzzle, solution = generate_puzzle()
    for row in puzzle:
        print(row)
