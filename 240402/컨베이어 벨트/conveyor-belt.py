n, t = map(int,input().split())
belt = list(map(int,input().split()))
belt.extend(list(map(int,input().split())))

temp = belt[-1]
for _ in range(t):
    for i in range(2*n-1,0,-1):
        belt[i] = belt[i-1]
    belt[0] = temp
    temp = belt[-1]

print(*belt[:n])
print(*belt[n:])