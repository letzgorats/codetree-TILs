n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(m):

        if 0<= i+1 < n and 0<= j+1 < m:
            answer = max(answer,board[i][j] + board[i+1][j] + board[i][j+1])

        if 0<= i+1 < n and 0<= j-1 < m and 0<= j+1 < m:
            answer = max(answer,board[i][j-1] + board[i][j] + board[i+1][j])

        if 0<= i-1 < n and 0<= j-1 < m:
            answer = max(answer,board[i-1][j] + board[i][j] + board[i][j-1])
        
        if 0<= i-1 < n and 0<= j+1 < m:
            answer = max(answer,board[i-1][j] + board[i][j] + board[i][j+1])
        
        if 0<= j+1 < m and 0<= j+2 < m:
            answer = max(answer,board[i][j+1] + board[i][j] + board[i][j+2])

        if 0<= i+1 < n and 0<=i+2 < n:
            answer = max(answer,board[i][j] + board[i+1][j] + board[i+2][j]) 


print(answer)