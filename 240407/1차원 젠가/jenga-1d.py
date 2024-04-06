n = int(input())

wall = []
for _ in range(n):
    x = int(input())
    wall.append(x)

end_of_array = n 

for i in range(2):

    s, e = map(int,input().split())

    temp = []

    for j in range(end_of_array):
        if j < s-1 or j > e-1:
            temp.append(wall[j])
    
    end_of_array = len(temp)
    for j in range(end_of_array):
        wall[j] = temp[j]

print(end_of_array)
for i in range(end_of_array):
    print(wall[i])