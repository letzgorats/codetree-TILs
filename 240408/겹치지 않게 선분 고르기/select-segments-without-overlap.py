from collections import deque

n = int(input())
lines = []
for _ in range(n):
    a, b = map(int,input().split())
    lines.append((a,b))


lines = sorted(lines,key= lambda x : x[1])
# print(lines)
max_count = [0]

def backtracking(lines, index, last_end,count,max_count):

    if len(lines) == index:
        max_count[0] = max(count, max_count[0])
        return 
        
    # 선분 선택하지 않는 경우
    backtracking(lines,index+1,last_end,count,max_count)
    # 선분을 선택하는 경우
    if lines[index][0] > last_end:
        backtracking(lines,index+1,lines[index][1],count+1,max_count)


backtracking(lines,0,-1,0,max_count)
print(*max_count)