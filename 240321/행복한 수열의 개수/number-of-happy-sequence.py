n, m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
# print(board)

if m == 1:
    print(2*n)
else:
    answer = 0
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt += 1
            if cnt == m:
                answer += 1
                break
    # print(answer)
    for j in range(n):
        cnt = 1
        for i in range(n-1):
            if board[i][j] == board[i+1][j]:
                cnt += 1
            if cnt == m:
                answer += 1
                break

    print(answer)