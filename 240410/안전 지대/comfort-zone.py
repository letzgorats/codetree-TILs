n, m = map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(int,input().split())))


def dfs(r,c,k):

    stack = [(r, c)]
    while stack:
        r, c = stack.pop()
        if r < 0 or r >= n or c < 0 or c >= m or visited[r][c] or board[r][c] <= k:
            continue
        visited[r][c] = True
        stack.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])


max_area = 0
min_k = 100

for k in range(1, max(map(max, board)) + 1):

    # dr = [-1,1,0,0]
    # dc = [0,0,-1,1]
    
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

print(min_k,max_area)