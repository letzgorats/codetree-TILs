n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]


def case1(i,j):

    return board[i][j] + board[i+1][j] + board[i][j+1]

def case2(i,j):

    return board[i][j-1] + board[i][j] + board[i+1][j]

def case3(i,j):

    return board[i-1][j] + board[i][j] + board[i][j-1]

def case4(i,j):

    return board[i-1][j] + board[i][j] + board[i][j+1]

def case5(i,j):

    return board[i][j+1] + board[i][j] + board[i][j+2]

def case6(i,j):

    return board[i][j] + board[i+1][j] + board[i+2][j]


answer = 0

for i in range(n):
    for j in range(m):

        if 0<= i+1 < n and 0<= j+1 < m:
            answer = max(answer,case1(i,j))

        if 0<= i+1 < n and 0<= j-1 < m:
            answer = max(answer,case2(i,j))

        if 0<= i-1 < n and 0<= j-1 < m:
            answer = max(answer,case3(i,j))
        
        if 0<= i-1 < n and 0<= j+1 < m:
            answer = max(answer,case3(i,j))
        
        if 0<= j+1 < m and 0<= j+2 < m:
            answer = max(answer,case5(i,j))

        if 0<= i+1 < n and 0<=i+2 < n:
            answer = max(answer,case6(i,j)) 


print(answer)