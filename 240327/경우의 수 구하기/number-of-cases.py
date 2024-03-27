n = int(input())
group = {}

for _ in range(n):
    content , g = input().strip().split()
    
    if g in group:
        group[g] += 1
    else:
        group[g] = 1

answer = 1
# print(group)

# (아무것도 선택 안하는 것 포함한 경우의 수) 다 곱하고, 서로 아무것도 선택안한 것 1가지 빼기
for k in group.keys():
    answer *= (group[k]+1)

print(answer-1)