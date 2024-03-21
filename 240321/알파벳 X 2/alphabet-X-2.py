alphabets = input().strip()

index = {}
cnt = 0 
first_appear = []

for i, a in enumerate(alphabets):

    if a not in first_appear:
        first_appear.append(a)
        index[a] = i
    else:
        tmp = i - index[a]
        index[a] = tmp

# print(index)
print(len(list(set(index.values())))-1)