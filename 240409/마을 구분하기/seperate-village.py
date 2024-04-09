import copy

n = int(input())
board = []

for _ in range(n):
    board.append(list(map(int,input().split())))


dr = [-1,1,0,0]
dc = [0,0,-1,1]
town = []


def dfs(r,c):

    global cnt
    board[r][c] = 0
    cnt += 1

    for d in range(4):

        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr < n and 0<= nc < n and board[nr][nc] == 1 :
            dfs(nr,nc)
    
    return cnt

temp = copy.deepcopy(board)
max_cnt = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt = 0
            town.append(max(dfs(i,j),max_cnt))

print(len(town))
for t in sorted(town):
    print(t)