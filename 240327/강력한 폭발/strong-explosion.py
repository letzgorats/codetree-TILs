from collections import deque
import copy

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))


def check_area():

    area = 0
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                area += 1
    return area

def handle_bomb(count, i, action):

    r, c = bombs[count][0], bombs[count][1]

    if i == 0 : # 위 아래 두개 초토화
        dirs = ((-2,0),(-1,0),(1,0),(2,0))
    elif i == 1: # 십자가 모양 초토화
        dirs = ((-1,0),(1,0),(0,-1),(0,1))
    else:   # 대각선 모양 초토화
        dirs = ((-1,-1),(-1,1),(1,-1),(1,1))
    
    # action이 "do" 이면 +1 , "undo"이면 -1

    if action == "do":
        factor = 1
    else: 
        factor = -1
    
    for d in range(4):
        nr,nc = r + dirs[d][0], c + dirs[d][1]
        if 0<= nr < n and 0<= nc < n:
            board[nr][nc] += factor

def dfs(count):

    global max_area

    if count == total_count:
        max_area = max(max_area,check_area())
        return 

    for i in range(3):

        # count 번 폭탄자리에 {i번 조합} 지역 초토화
        handle_bomb(count,i,"do")
        dfs(count+1)
        handle_bomb(count,i,"undo")

max_area = 0
bombs = deque([])
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            bombs.append((i,j))

total_count = len(bombs)

dfs(0)
print(max_area)