import copy

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

r,c = map(int,input().split())
r -= 1
c -= 1

x = board[r][c]

temp = copy.deepcopy(board)

for i in range(r-(x-1),r+(x-1)+1):
    if 0<= i < n :
        temp[i][c] = 0 

for j in range(c-(x-1),c+(x-1)+1):
    if 0<= j < n :
        temp[r][j] = 0


answer = [[0] * n for _ in range(n)]

for j in range(0,n):
    k = n-1
    for i in range(n-1,-1,-1):
        if temp[i][j] != 0:
            answer[k][j] = board[i][j]
            k -= 1

for i in range(n):
    for j in range(n):
        print(answer[i][j],end=" ")
    print()       

# 1 2 0 3 
# 3 0 0 0 
# 3 1 0 2 
# 4 5 4 4 

# 1 2 4 3
# 3 2 2 3
# 3 1 6 2
# 4 5 4 4

# 1000
# 3203 
# 3102 
# 4544