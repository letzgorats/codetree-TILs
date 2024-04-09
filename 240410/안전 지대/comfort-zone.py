n, m = map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(int,input().split())))


def dfs(r,c):

    visited[r][c] = True

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] > k and not visited[nr][nc]:
            dfs(nr,nc)


k = 1
area = 0
max_area = 0
pre = max_area

while area >= max_area:

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    
    visited = [[False] * m for _ in range(n)]
    area = 0
    
    for i in range(n):
        for j in range(m):
            if board[i][j] > k and not visited[i][j]:
                dfs(i,j)
                area += 1

    # print(area)
    max_area = max(area,max_area)
    if area < max_area:
        break
        
    k += 1

print(k-1,max_area)