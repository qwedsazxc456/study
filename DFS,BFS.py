# 스택 자료구조
# 선입후출
# 리스트 자료 사용
# O(1)
# append , pop

# 큐
# 선입선출

# 재귀함수
# 최대 깊이 제한이 있다
# 스택의 자료형태처럼

# DFS(Depth-First Search)
# 스택 자료구조 이용

graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
# 0번부터 인접한 노드의 번호

visited=[False]*9

def dfs(graph, v, visited):
    visited[v]=True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
            
dfs(graph, 1, visited)

# BFS(Breadth_First Search)
# 너비 우선 탐색, 가까운 노드부터 우선적으로 탐색
# 큐 자료구조 이용

from collections import deque

def bfs(graph, start, visited):
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

# deque 양방향 큐
# appendleft, popleft 등
# 속도가 빠르다 O(1)
               
bfs(graph,1,visited)

