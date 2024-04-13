def move(r,c):

    candi = []
    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0<= nc < n:
            candi.append((nr,nc,board[nr][nc]))
        
    max_val = 0
    target_r, target_c = 0, 0

    while candi:

        nr, nc, val = candi.pop(0) 
        if max_val < val:
            max_val = val
            target_r, target_c = nr, nc
    
    return (target_r,target_c)

# 격자의 크기 : n
# 턴의 수 : m

n, m = map(int,input().split())
board = []
dr = [-1,-1,-1,0,1,1,1,0]
dc = [-1,0,1,1,1,0,-1,-1]

for _ in range(n):
    board.append(list(map(int,input().split())))

for turn in range(m):

    for k in range(1,n**2+1):
        
        change = False
        for i in range(n):
            for j in range(n):
                if k == board[i][j]:
                    curr, curc = i, j
                    nextr, nextc = move(curr,curc)
                    board[curr][curc], board[nextr][nextc] = board[nextr][nextc], board[curr][curc]
                    change = True
                    break
            if change:
                break

for i in range(n):
    for j in range(n):
        print(board[i][j],end=" ")
    print()