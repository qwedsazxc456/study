# 1260

n,m,v = map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

# dfs

visited=[False]*(n+1)
def dfs(v):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# bfs

from collections import deque

visited_2=[False]*(n+1)
def bfs(v):
    que=deque([v])
    visited_2[v]=True
    while que:
        l = que.popleft()
        print(l, end=' ')
        for i in graph[l]:
            if not visited_2[i]:
                que.append(i)
                visited_2[i]=True
    
        
dfs(v)
print()
bfs(v)

# 2606