import sys

args = sys.argv

if len(args) > 2 or len(args) <= 1:
    # raise OverflowError("Usage: nqueens N")
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(args[-1])
except:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

print(N)

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()