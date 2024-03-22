n = int(input())
global answer
answer = 0
candi = ['1','22','333','4444']

def backtracking(curNum,cnt):
    global answer
    if cnt == n :
        answer += 1
        return 
    elif cnt > n:
        return 
    for c in candi:
        backtracking(curNum+c,cnt+len(c))

backtracking("",0)
print(answer)