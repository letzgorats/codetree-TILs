from collections import deque

n = int(input())
lines = []
for _ in range(n):
    a, b = map(int,input().split())
    lines.append((a,b))


lines = sorted(lines,key= lambda x : x[1])
# print(lines)
max_count = 0

def backtracking(lines, index, last_end,count):

    if len(lines) == index:
        return count
        
    # 선분 선택하지 않는 경우
    not_chosen = backtracking(lines,index+1,last_end,count)
    # 선분을 선택하는 경우
    if lines[index][0] > last_end:
        chosen = backtracking(lines,index+1,lines[index][1],count+1)
    else:
        chosen = count

    return max(chosen,not_chosen)

max_count = backtracking(lines,0,-1,0)
print(max_count)