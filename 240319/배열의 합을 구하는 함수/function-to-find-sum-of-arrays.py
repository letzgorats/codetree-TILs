import sys 
input = sys.stdin.readline

n = int(input())
board = []
total = 0

for i in range(n):
    total = 0
    
    row = list(map(int,input().split()))
    total += sum(row)
    row.append(total)
    board.append(row)

last = []

for j in range(n+1):
    total = 0
    for i in range(n):
        total += board[i][j]
    last.append(total)
board.append(last)

for i in range(n+1):
    for j in range(n+1):
        print(board[i][j],end=" ")
    print()