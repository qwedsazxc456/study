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

n = int(input())
m = int(input())
v=[False]*(n+1)
g=[[] for _ in range(n+1)]
for _ in range(m):
    b,c=list(map(int, input().split()))
    g[b].append(c)
    g[c].append(b)
def bfs(g,v,s):
    v[s]=True
    for i in g[s]:
        if not v[i]:
            bfs(g,v,i)
bfs(g,v,1)
print(v.count(True)-1)

# 2667

n = int(input())
matrix=[]
g=[[] for _ in range(n**2+1)]
v=[False]*(n**2+1)

for _ in range(n):
    r=input()
    matrix.append(r)
    
for i in range(n):
    for j in range(n-1):
        if matrix[i][j] == '1' and matrix[i][j+1]== '1':
            g[i*n+j].append(i*n+j+1)
            g[i*n+j+1].append(i*n+j)

for j in range(n):
    for i in range(n-1):
        if matrix[i][j] == '1' and matrix[i+1][j]== '1':
            g[i*n+j].append((i+1)*n+j)
            g[(i+1)*n+j].append(i*n+j)

def bfs(g,v,s):
    v[s]=True
    for i in g[s]:
        if not v[i]:
            bfs(g,v,i)
a=[]
c=0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '1' and not v[i*n+j]:
            bfs(g,v,i*n+j)
            a.append(v.count(True)-sum(a))
            c += 1
a.sort()
print(c)
for i in a:
    print(i)
    
# 1012

t = int(input())
def bfs(r,c):
    a[c][r]=0
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(4):
        x=r+dx[i]
        y=c+dy[i]
        if -1<x<m and -1<y<n:
            if a[y][x] == 1:
                a[y][x] = 0
                bfs(x,y)                             
    
for _ in range(t):
    m,n,k=map(int, input().split())
    a=[[0 for _ in range(m)] for _ in range(n)]
    cnt=0
    for _ in range(k):
        r,c=map(int, input().split())
        a[c][r]=1
    for i in range(n):
        for j in range(m):
            if a[i][j] ==1:
                bfs(j,i)
                cnt += 1
    print(cnt)

