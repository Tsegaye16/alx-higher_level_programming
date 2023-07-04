#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at the given position without attacking other queens

    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check the upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col):
    # Recursive function to solve the N queens problem using backtracking

    if col >= N:
        # All queens have been placed, print the solution
        print_solution(board)
        return

    for i in range(N):
        if is_safe(board, i, col):
            # Place a queen at the current position
            board[i][col] = 'Q'

            # Recur for the next column
            solve_nqueens(board, col + 1)

            # Backtrack and remove the queen from the current position
            board[i][col] = '.'

def print_solution(board):
    # Print the board configuration
    for row in board:
        print(' '.join(row))
    print()

if __name__ == '__main__':
    # Check the number of arguments
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    # Check if N is valid
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    # Initialize an empty chessboard
    board = [['.' for _ in range(N)] for _ in range(N)]

    # Solve the N queens problem
    solve_nqueens(board, 0)

