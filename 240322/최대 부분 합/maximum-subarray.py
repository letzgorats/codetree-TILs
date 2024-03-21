# 7
# 1 -2 4 5 -6 7 -2   

n = int(input())
numbers = list(map(int,input().split()))

# Kadane 알고리즘
max_so_far = numbers[0]
max_ending_here = numbers[0]

for x in numbers[1:]:
    max_ending_here = max(x,max_ending_here+x)
    # print(max_ending_here)
    max_so_far = max(max_so_far,max_ending_here)
    # print(max_so_far)

print(max_so_far)

# prefix suffix 알고리즘