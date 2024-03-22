k, n = map(int,input().split())

answer = []
cnt = 0

def backtracking(cnt):
    # print(answer)

    if cnt == n:
        for i in answer:
            print(i,end=" ")
        print()
        return 
    
    for i in range(1,k+1):
        answer.append(i)
        backtracking(cnt+1)
        answer.pop()
    
backtracking(cnt)