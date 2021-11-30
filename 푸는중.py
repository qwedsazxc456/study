n,m,v=map(int,input().split())
graph=[]
for _ in range(m):
    a,b=map(int, input().split())
    graph.append([a,b])
graph.sort()
visited=[False]*n
def dfs(graph,visited,v):
    visited[v-1]=True
    print(v,end=' ')
    for i in graph:
        if i[1]==v and not visited[i[0]-1]:
            dfs(graph,visited,i[0])
        if i[0]==v and not visited[i[1]-1]:
            dfs(graph,visited,i[1])
            
dfs(graph,visited,v)
print()
from collections import deque

visited=[False]*n
def bfs(graph,visited,v):
    que=deque([v])
    visited[v-1]=True
    while que:
        a=que.popleft()
        print(a, end=' ')
        for i in graph:
            if i[1]==a and not visited[i[0]-1]:
                que.append(i[0])
                visited[i[0]-1]=True
            if i[0]==a and not visited[i[1]-1]:
                que.append(i[1])
                visited[i[1]-1]=True

bfs(graph,visited,v)