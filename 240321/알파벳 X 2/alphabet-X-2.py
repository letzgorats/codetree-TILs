alphabets = input().strip()

index = {}
cnt = 0 
first_appear = []

for i, a in enumerate(alphabets):

    if a not in index:
        first_appear.append(a)
        index[a] = [i]
    else:
        index[a].append(i)

count = 0
for i in range(len(first_appear)-1):
    for j in range(i+1,len(first_appear)):
        a_start, a_end = index[first_appear[i]]
        b_start, b_end = index[first_appear[i]]
        if a_start < b_start < a_end < b_end or b_start < a_start < b_end < a_end:
            count += 1

print(count)


# for i in list(set(index.values())):
#     if i != 1:

# print(len()-1)