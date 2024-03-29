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
    visited = [[False] * n for _ in range(n)]
    queue = deque([(r,c)])
    visited[r][c] = True

    cnt = 1
    while queue:

        r,c = queue.popleft()
        # visited[r][c] = True
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and board[nr][nc] == 0:
                visited[nr][nc] = True
                queue.append((nr,nc))
                cnt += 1
    
    answer += cnt

print(answer)