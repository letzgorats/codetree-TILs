n, t = map(int,input().split())
first = list(map(int,input().split()))
second = list(map(int,input().split()))
third = list(map(int,input().split()))

for _ in range(t):

    temp1 = first[-1]
    temp2 = second[-1]
    temp3 = third[-1]

    for i in range(n-1,0,-1):
        first[i] = first[i-1]
    first[0] = temp3

    for i in range(n-1,0,-1):
        second[i] = second[i-1]
    second[0] = temp1

    for i in range(n-1,0,-1):
        third[i] = third[i-1]
    third[0] = temp2

print(*first)
print(*second)
print(*third)