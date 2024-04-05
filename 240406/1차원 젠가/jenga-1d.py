n = int(input())

building = []
for _ in range(n):
        # x = list(map(int,input()))
        x = int(input())
        building.append(x)
# print(building)
s1, e1 = map(int,input().split())

building = building[:s1-1] + building[e1:]
# print(building)

s2, e2 = map(int,input().split())
building = building[:s2-1] + building[e2:]
# print(building)

print(len(building))
for i in range(len(building)): 
    print(building[i])