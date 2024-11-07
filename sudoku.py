def print_board(board):
    """Prints the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()

def find_empty_location(board):
    """Finds an empty location in the Sudoku board (represented by 0)."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col  # Return the first empty location
    return None  # No empty location found

def is_safe(board, row, col, num):
    """Checks if it's safe to place a number in the specified position."""
    # Check row
    if num in board[row]:
        return False

    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check 3x3 box
    box_row, box_col = row // 3, col // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    """Solves the Sudoku board using backtracking."""
    empty_location = find_empty_location(board)
    if not empty_location:
        return True  # Solved

    row, col = empty_location
    for num in range(1, 10):  # Try numbers 1 to 9
        if is_safe(board, row, col, num):
            board[row][col] = num  # Place the number

            if solve_sudoku(board):  # Recursively try to solve
                return True
            
            board[row][col] = 0  # Reset on backtrack

    return False  # Trigger backtrack

def main():
    """Main function to run the Sudoku solver."""
    # Example Sudoku board (0 represents empty cells)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("Original Sudoku Board:")
    print_board(board)

    if solve_sudoku(board):
        print("Solved Sudoku Board:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()