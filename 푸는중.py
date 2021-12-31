from collections import deque
n,m = map(int, input().split())
a=[]
for _ in range(n):
    a.append(list(map(int, input())))
def bfs():
    a[0][0]=1
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    q=deque([[0,0,0]])
    while q:
        x,y,c=q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if -1<nx<n and -1<ny<m:
                if a[nx][ny] ==0:
                    a[nx][ny]=a[x][y]+1
                    q.append([nx,ny,c])
                if c == 0 and a[nx][ny]==1:
                    a[nx][ny]=a[x][y]+1
                    q.append([nx,ny,1])
    if a[n-1][m-1] != 0:
        return a[n-1][m-1]
    return -1

print(bfs())