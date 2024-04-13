import copy

# 격자의 크기 : n
# 구슬의 개수 : m
# 시간 : t
n, m, t = map(int,input().split())

board = []
marble_board = [[0] * n for _ in range(n)]
marble_list = []

for _ in range(n):
    board.append(list(map(int,input().split())))

for i in range(m):
    r, c = map(int,input().split())
    marble_list.append([r-1,c-1])
    marble_board[r-1][c-1] = 1

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def move_marble(r,c):

    candi = []
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0<= nc < n:
            candi.append((nr,nc,board[nr][nc]))
    
    max_val = 0
    target_r, target_c = 0,0
    while candi:

        r, c, val = candi.pop(0)
        if max_val < val:
            max_val = val
            target_r, target_c = r, c
    return (target_r, target_c)
        

for time in range(t):

    while marble_list:

        marble_r,marble_c = marble_list.pop(0)
        marble_board[marble_r][marble_c] -= 1

        (move_to_r, move_to_c) = move_marble(marble_r,marble_c)

        marble_board[move_to_r][move_to_c] += 1


    for i in range(n):
        for j in range(n):
            if marble_board[i][j] >= 2:
                marble_board[i][j] = 0
            elif marble_board[i][j] == 1:
                marble_list.append([i,j])
    

answer = 0    
for i in range(n):
    for j in range(n):
        if marble_board[i][j] == 1:
            answer += 1

print(answer)