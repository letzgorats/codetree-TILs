n  = int(input())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())))


def dfs(r,c):

    global area 

    stack = [(r,c)]
    
    while stack:
        r,c = stack.pop()
        if r < 0 or r >=n or c < 0 or c >=n or visited[r][c] or board[r][c] != now:
            continue

        visited[r][c] = True
        stack.extend([(r-1,c),(r+1,c),(r,c-1),(r,c+1)])
        area += 1



visited = [[False] * n for _ in range(n)]
now = -1
block = 0
max_area = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            area = 0 
            now = board[i][j]
            dfs(i,j)
            max_area = max(area,max_area)
            if area >= 4:
                block += 1
        

print(block,max_area)