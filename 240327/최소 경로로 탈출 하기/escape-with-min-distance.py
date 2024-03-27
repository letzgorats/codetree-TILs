from collections import deque

n, m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

def bfs(r,c,count):

    deq = deque([(r,c,count)])
    # visited = [[False] * m for _ in range(n)]
    board[r][c] = 0 
    # visited[r][c] = True
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while deq:

        r, c, cnt = deq.popleft()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0<= nr < n and 0<= nc < m and board[nr][nc] == 1 :
            # and not visited[nr][nc]:
                # visited[nr][nc] = True
                deq.append((nr,nc,cnt+1))
                board[nr][nc] = 0

    if r == n-1 and c == m-1 :
        return cnt
    else:
        return -1


print(bfs(0,0,0))