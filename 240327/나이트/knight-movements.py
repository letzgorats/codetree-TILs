from collections import deque

n = int(input())

position = list(map(int,input().split()))
r1,c1 = position[0], position[1]
r2,c2 = position[2], position[3]


def bfs(i,j):

    deq = deque([(i,j,0)])
    visited = [[False] * n for _ in range(n)]
    dirr = [-1,-2,-2,-1,1,2,2,1]
    dirc = [-2,-1,1,2,2,1,-1,-2]

    while deq:

        r, c,cnt= deq.popleft()

        if r == r2 and c == c2:
            return cnt

        for d in range(8):
            nr, nc = r + dirr[d], c + dirc[d]
            if 0<= nr < n and 0<= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                deq.append((nr,nc,cnt+1))

    return -1

print(bfs(r1,c1))