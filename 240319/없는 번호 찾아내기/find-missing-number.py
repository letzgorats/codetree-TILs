import sys
input = sys.stdin.readline

numbers = [0] * 31

for i in range(28):

    numbers[int(input())] += 1
    
for i in range(1,len(numbers)):
    
    if numbers[i] == 0:
        print(i)