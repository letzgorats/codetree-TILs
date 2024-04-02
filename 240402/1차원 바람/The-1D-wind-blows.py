from collections import deque
n, m, q = map(int,input().split())

board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

wind = deque([])
for _ in range(q):
    row, direction = input().split()
    wind.append((int(row),direction))

# print(board)
# print(wind)
dirs = {"L" : -1 , "R" : 1}

def move(direction,row):


    if direction == 1:
        temp = board[row][0]
        for c in range(m-1):
            board[row][c] = board[row][c+1]
        board[row][-1] = temp

    elif direction == -1:
        temp = board[row][-1]
        for c in range(m-1,0,-1):
            board[row][c] = board[row][c-1]
        board[row][0] = temp


while wind:

    r, d = wind.popleft()
    d = dirs[d]
    r = r-1
    tmpr = r
    tmpd = d
    
    move(d,r)

    while 0<= r-1:

        for c in range(m):
            if board[r][c] == board[r-1][c]:
                d = (-d)
                move(d,r-1)
                break
        r -= 1

    r = tmpr
    d = tmpd

    while r+1 < n:

        for c in range(m):
            if board[r][c] == board[r+1][c]:
                d = (-d)
                move(d,r+1)
                break
        r += 1


for i in range(n):
    for j in range(m):
        print(board[i][j],end=" ")
    print()