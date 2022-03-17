# 가장 짧은 경로를 찾는 알고리즘
# 각 지점은 그래프에서 노드로 표현
# 도로는 간선으로 표현

# 다익스트라 최단 경로 알고리즘
# 특정한 노드에서 출발하여 다른 모든 노드로 가능 최단 경로
# 음의 간선이 없을 때 정상적으로 동작
# 그리디 알고리즘으로 분류
# - 매 상황에서 가장 비용이 적은 노드를 선택

# 1. 출발 노드를 설정
# 2. 최단 거리 테이블을 초기화
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
# 5. 3,4번 반복

# 알고리즘 동작 과정에서 최단 거리 테이블은 각 노드에 대한 현재까지의 최단 거리 정보 가지고 있다
# 처리 과정에서 더 짧은 경로를 찾으면 갱신

# 그리디 - 매 상황에서 방문하지 않은 가장 비용이 적은 노드를 선택
# 단계를 거치며 한 번 처리된 노도의 최단 거리는 고정
# - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해
# 다익스트라 알고리즘을 수행한 뒤에 테이블에 각노드까지의 최단 거리 정보가 저장
# -완벽한 형태의 최단 경로를 구하려면 소스코드에 추가적인 기능 더 넣어야 함

from cmath import cos
from dis import dis
from math import dist
import sys
input=sys.stdin.readline
inf=int(1e9)

# 노드의 개수, 간선의 개수 입력
n,m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 리스트
graph = [[] for _ in range(n+1)]
# 방믄 리스트
visited = [False] * (n+1)
# 최단 거리 테이블 초기화
distance = [inf]*(n+1)

# 모든 간선 정보를 입력
for _ in range(m):
    a,b,c, = map(int, input().split()) # a노드에 b노드 가는비용 c
    graph[a].append((b,c))
    
# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = inf
    index = 0 # 최단 거리 노드 인덱스
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now]+j[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스타라 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, infinity 출력
    if distance[i] == inf:
        print('infinity')
    #도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])
        
# 우선순위 큐 (Priority Queue)
# 힙(Heap)
# 우선순위 큐를 구현하기 위해 사용하는 자료구조
# 최소 힙과 최대 힙
# 다양한 알고리즘에서 사용

import heapq

# 오름차순 힙 정렬(Heap sort)
def heapsort(iterable):
    h=[]
    result=[]
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# 내림차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h=[]
    result=[]
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

# 다익스트라 알고리즘 개선
# 방문하지 않은 노드 중에서 가장 짧은 노드를 선택하기 위해 힙 자료구조 이용

# 다익스트라 알고리즘 개선된 방법

import heapq

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now]:
            cost = dist +i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
                
                
# 1753

import heapq
import sys
input=sys.stdin.readline

V, E = map(int, input().split())
k = int(input())
graph=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int, input().split())
    graph[u].append([v,w])
inf = int(1e9)
distance = [inf]*(V+1)
q=[]

distance[k] = 0

heapq.heappush(q, (0,k))
while q:
    dis,now = heapq.heappop(q)
    if distance[now] < dis:
        continue
    for i in graph[now]:
        if dis + i[1] < distance[i[0]]:
            distance[i[0]] = dis+i[1]
            heapq.heappush(q, (dis+i[1],i[0]))
            
for i in range(1,V+1):
    print('INF' if distance[i]==inf else distance[i])
    

# 플로이드 워셜 알고리즘

# 단계별로 거쳐 가는 노드를 기준으로 알고리즘을 수행
# 매 단계마다 방문하지 않은 노드 중에 최단 거리 노드 찾는 과정 필요하지 않음
# 2차원 테이블 최단 거리 정보 저장
# 다이나믹 프로그래밍 유형

# 각 단계마다 특정한 노드 k를 거쳐 가능 경우를 확인

inf = int(1e9)

n = int(input())
m = int(input())

graph = [[inf]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b :
            graph[a][b] = 0
            
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c
    
for k in  range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == inf:
            print('inf', end=' ')
        else:
            print(graph[a][b] , end=' ')
    print()
    
# 11404

n = int(input())
m = int(input())
inf = int(1e9)
graph = [[inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    if c < graph[a][b] :
        graph[a][b] = c

for i in range(1,n+1):
    graph[i][i] = 0
        
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == inf:
            print(0 , end=' ')
        else:
            print(graph[i][j], end=' ')
    print()