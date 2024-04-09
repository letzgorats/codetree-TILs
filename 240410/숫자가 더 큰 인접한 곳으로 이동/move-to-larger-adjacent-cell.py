from collections import deque

n, r, c = map(int,input().split())
r -= 1
c -= 1
board = []

for _ in range(n):
    board.append(list(map(int,input().split())))


def bfs(r,c):

    queue = deque([(r,c)])

    while queue:

        r,c = queue.popleft()
        print(board[r][c],end=" ")

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0<= nr < n and 0<= nc < n and not visited[nr][nc] and board[nr][nc] > board[r][c]:
                visited[nr][nc] = True
                queue.append((nr,nc))
                break
        

dr = [-1,1,0,0]
dc = [0,0,-1,1]
visited = [[False] * n for _ in range(n)]
bfs(r,c)