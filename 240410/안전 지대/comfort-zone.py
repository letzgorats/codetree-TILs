n, m = map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(int,input().split())))


def dfs(r,c,k):

    if not (0<= r < n and 0<= c < m) or visited[r][c] or board[r][c] <= k:
        return 

    visited[r][c] = True

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        dfs(nr,nc,k)


area = 0
max_area = 0
min_k = 100

for k in range(1, max(map(max, board)) + 1):

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    visited = [[False] * m for _ in range(n)]
    area = 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] > k and not visited[i][j]:
                dfs(i,j,k)
                area += 1
                
    if area > max_area:
        max_area = area
        min_k = k
    elif area == max_area:
        min_k = min(min_k,k)
        break

print(min_k,max_area)