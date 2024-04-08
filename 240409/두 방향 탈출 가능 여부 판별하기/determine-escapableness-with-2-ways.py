import copy

n, m = map(int,input().split())
board = []

for i in range(n):
    board.append(list(map(int,input().split())))

# print(board)

answer = copy.deepcopy(board)
visited = [[False] * m for _ in range(n)]


def dfs(r,c):

    answer[r][c] = 2
    visited[r][c] = True

    if answer[-1][-1] == 2:
        return 1

    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0<= nc < m and not visited[nr][nc] and answer[nr][nc] == 1:
            dfs(nr,nc) 
            answer[r][c] = 1


dr = [1,0]
dc = [0,1]
dfs(0,0)

if answer[-1][-1] == 2:
    print(1)
else:
    print(0)