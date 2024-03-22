from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c):

    dq = deque([])
    dq.append((r,c))

    visited = [[False] * m for _ in range(n)]
    visited[r][c] = True
    while dq:

        r,c = dq.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<= nr < n and 0 <= nc < m and board[nr][nc] == 1:
                if not visited[nr][nc]:
                    dq.append((nr,nc))
                    visited[nr][nc] = True
        
    if (r,c) == (n-1,m-1):
        print(1)
    else:
        print(0)





n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
bfs(0,0)