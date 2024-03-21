n = int(input())
numbers = list(map(int,input().split()))

prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + numbers[i]

print(prefix_sum[-1])