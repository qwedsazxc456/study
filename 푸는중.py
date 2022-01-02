from collections import deque
t=int(input())
for _ in range(t):
    v,e=map(int, input().split())
    g=[[] for _ in range(v+1)]
    bi=[[] for _ in range(v+1)]
    for _ in range(e):
        a,b=map(int, input().split())
        g[a].append(b)
        g[b].append(a)
def bfs(s):
    bi[s]=1
    
    
    