n = int(input())
board = []

for i in range(n):
    board.append(list(map(int,input().split())))


dp = [[0] * n for _ in range(n)]

dp[0][0] = board[0][0]

for i in range(n):
    for j in range(n):

        # 오른쪽으로 이동
        if j > 0 :
            dp[i][j] = max(dp[i][j],dp[i][j-1] + board[i][j])
        
        # 아래쪽으로 이동
        if i > 0 :
            dp[i][j] = max(dp[i][j],dp[i-1][j] + board[i][j])

print(dp[n-1][n-1])