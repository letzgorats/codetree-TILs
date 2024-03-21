n, m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

def dig_gold(row,col):
    k = 1
    tmp = 0 
    # print(row,col)
    while True:
        cost = k * k + (k+1) * (k+1)
        gold = 0 
        for i in range(-k,k+1):
            for j in range(-k,k+1):
                if abs(i)+abs(j) <= k:
                    if 0<= row+i < n and 0<= col+j < n:  
                        if board[row+i][col+j] == 1:
                            gold += 1

            # print(gold)
        # print(gold)
        if cost <= gold * m:
            tmp = max(tmp,gold)
        if k > n+1 :
            break
        k += 1

    return tmp

answer = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            answer = 1
            break

for i in range(n):
    for j in range(n):
        answer = max(answer,dig_gold(i,j))

print(answer)



 # if (i == (-k) and j == 0) or (i== k and j == 0):
                #     if 0<= row+i < n and 0<= col+j < n:  
                #         # print(row+i,col+j)
                #         if board[row+i][col] == 1:
                #             gold += 1
                # elif (i == 0 and j == -k) or (i == 0 and j==k):
                #     if 0<= row+i < n and 0<= col+j < n:  
                #         # print(row+i,col+j)
                #         if board[row][col+j] == 1:
                #             gold += 1
                # elif -k+1 <= i <= k-1 and -k+1 <= j <= k-1 :
                #     if 0<= row+i < n and 0<= col+j < n:
                #         # print(row+i,col+j)
                #         if board[row+i][col+j] == 1:
                #             gold += 1