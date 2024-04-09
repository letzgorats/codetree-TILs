k, n = map(int,input().split())

def backtracking(path, last, count, n, k):

    if len(path) == n:
        for p in path:
            print(p,end=" ")
        print()
        return 
    
    for next_num in range(1,k+1):
        if next_num == last and count == 2: # 연속 3회 조건 체크
            continue
        if next_num == last:
            backtracking(path + [next_num], next_num, count+1, n, k)
        else:
            backtracking(path + [next_num], next_num, 1, n, k)


backtracking([],0,0,n,k)