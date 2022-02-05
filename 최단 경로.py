# 다익스트라 최단경로
# 음의 간선이 없을 때 정상적으로 동작
# 그리디 알고리즘으로 분류
# 다이나믹으로 분류 되기도 한다

# 출발노드설정
# 최단 거리 테이블 초기화
# 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
# 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
# 3번4번 반복

# 단계를 거치며 한 번 처리된 노드의 최단 거리는 고정
# 테이블에 각 노드까지의 최단 거리 정보가 저장

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
graph = [[] for i in range(n+1)]
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

