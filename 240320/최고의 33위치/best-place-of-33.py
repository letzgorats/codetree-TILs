n = int(input())

board = []

for _ in range(n):
    row = list(map(int,input().split()))
    board.append(row)

def find_coin(row,col):

    money = 0
    for i in range(row,row+3):
        for j in range(col,col+3):
            if board[i][j] == 1:
                money += board[i][j]

    return money

answer = 0

for i in range(n):
    for j in range(n):
        if 0 <= i + 2 < n and 0<= j+2 < n:
            answer = max(find_coin(i,j),answer)

print(answer)