from collections import deque

n, k = map(int,input().split())
board = []

for _ in range(n):
    board.append(list(map(int,input().split())))

start_point = []
for _ in range(k):
    r, c = map(int,input().split())
    start_point.append((r-1,c-1))


dr = [-1,1,0,0]
dc = [0,0,-1,1]
answer = 0

for r,c in start_point:
    queue = deque([(r,c)])
    board[r][c] = 2
    while queue:

        r,c = queue.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                board[nr][nc] = 2
                queue.append((nr,nc))
                
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            answer += 1
    

print(answer)