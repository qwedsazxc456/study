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

# 2178

from collections import deque
n,m=map(int, input().split())
maze=[]
for _ in range(n):
    a=input()
    b=[]
    for i in a:
        b.append(int(i))
    maze.append(b)

def bfs(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    q=deque([[x,y]])
    while q:
        x,y=q.popleft()
        for i in range(4):
            x_2=x+dx[i]
            y_2=y+dy[i]
            if -1<x_2<m and -1<y_2<n:
                if maze[y_2][x_2] == 1:
                    maze[y_2][x_2] = maze[y][x]+1
                    q.append([x_2,y_2])
        
bfs(0,0)
print(maze[n-1][m-1])

# 7576

from collections import deque

m,n=map(int, input().split())
a=[]
for _ in range(n):
    a.append(list(map(int, input().split())))

def bfs(a,c):
    q=deque()
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                q.append([i,j])
    while q:
        c += 1
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if -1<nx<n and -1<ny<m:
                    if a[nx][ny] == 0:
                        q.append([nx,ny])
                        a[nx][ny] = 1
    for i in a:
        if 0 in i:
            return -1
            
    return c

print(bfs(a,-1))

# 7569

from collections import deque

m,n,h=map(int, input().split())
a=[]
b=[]
for _ in range(h):
    for _ in range(n):
       b.append(list(map(int, input().split())))
    a.append(b)
    b=[]

def bfs(a,c):
    dx=[1,-1,0,0,0,0]
    dy=[0,0,1,-1,0,0]
    dz=[0,0,0,0,1,-1]
    q=deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if a[i][j][k] ==1:
                    q.append([i,j,k])    
    while q:
        c += 1                           
        for _ in range(len(q)):
            z,x,y=q.popleft()
            for i in range(6):
                nx=x+dx[i]
                ny=y+dy[i]
                nz=z+dz[i]
                if -1<nx<n and -1<ny<m and -1<nz<h:
                    if a[nz][nx][ny] == 0:
                        a[nz][nx][ny] = 1
                        q.append([nz,nx,ny])
    for i in a:
        for j in i:
            if 0 in j:
                return -1
    
    return c-1

print(bfs(a,0))

# 1697

from collections import deque
n,k = map(int, input().split())
c=0
q=deque([n])
v=[False]*100001
while q:
    if k in q:
        print(c)
        break
    for _ in range(len(q)):
        p=q.popleft()
        if -1<p<100001 and not v[p]:
            v[p] = True
            q.append(p+1)
            q.append(p-1)
            q.append(2*p)
    c += 1
    
# 7562

from collections import deque
t=int(input())

m_1=[1,1,-1,-1,2,2,-2,-2]
m_2=[2,-2,2,-2,1,-1,1,-1]
for _ in range(t):
    i=int(input())    
    start_x,start_y=map(int, input().split())
    end_x,end_y=map(int, input().split())
    v=[[False]*i for _ in range(i)]
    q=deque([[start_x,start_y]])
    c=0
    while True:
        if [end_x,end_y] in q:
            print(c)
            break
        for _ in range(len(q)):
            x,y=q.popleft()
            for j in range(8):
                nx=x+m_1[j]
                ny=y+m_2[j]
                if -1<nx<i and -1<ny<i:
                    if not v[nx][ny]:
                        q.append([nx,ny])
                        v[nx][ny]=True
        c += 1