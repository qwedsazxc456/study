from collections import deque
n,m = map(int, input().split())
mat=[[] for _ in range(n)]
for i in range(n):
    for j in input():
        mat[i].append(int(j))
q=deque([[0,0,0]])
visit=[[[False]*2 for _ in range(m)] for _ in range(n)]
visit[0][0][0] = True
dist=[[0]*m for _ in range(n)]
dist[0][0]=1
last_dis=[]
while q:
    r,c,b = q.popleft()
    if r == n-1 and c == m-1:
        last_dis.append(dist[r][c])
    dr = 0,0,-1,1
    dc = -1,1,0,0
    for i in range(4):
        if -1<r+dr[i]<n and -1<c+dc[i]<m and not visit[r+dr[i]][c+dc[i]][b]:
            if b == 0 and mat[r+dr[i]][c+dc[i]] == 1:
                visit[r+dr[i]][c+dc[i]][0] = True
                q.append([r+dr[i],c+dc[i],1])
                dist[r+dr[i]][c+dc[i]] = dist[r][c]+1
            elif mat[r+dr[i]][c+dc[i]] == 0:
                visit[r+dr[i]][c+dc[i]][b] = True
                q.append([r+dr[i],c+dc[i],b])
                dist[r+dr[i]][c+dc[i]] = dist[r][c]+1
                
if dist[n-1][m-1] == 0:
    print(-1)
else:
    print(min(last_dis))