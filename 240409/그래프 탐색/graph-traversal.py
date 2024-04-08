n, m = map(int,input().split())

graph = [[] for _ in range(n+1) ]
# print(graph)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

def dfs(start):

    for v in graph[start]:
        if not visited[v]:
            visited[v] = True
            dfs(v)

visited = [False for _ in range(n+1)]
dfs(1)

cnt = 0
for v in visited:
    if v:
        cnt += 1

print(cnt-1)