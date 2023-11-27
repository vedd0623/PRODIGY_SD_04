def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_location(board)

    if row is None and col is None:
        return True

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def get_user_input():
    print("Enter the Sudoku puzzle, column by column. Use '0' for empty cells.")
    puzzle = [[0] * 9 for _ in range(9)]

    for j in range(9):
        for i in range(9):
            while True:
                try:
                    value = int(input(f"Enter the value for column {j + 1}, row {i + 1}: "))
                    if 0 <= value <= 9:
                        puzzle[i][j] = value
                        break
                    else:
                        print("Please enter a number between 0 and 9.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

    return puzzle

if __name__ == "__main__":
    sudoku_board = get_user_input()

    print("\nSudoku Puzzle:")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku:")
        print_board(sudoku_board)
    else:
        print("\nNo solution exists.")
