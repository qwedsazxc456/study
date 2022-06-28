'''
음수 간선에 관하여 분류
1.모든 간선이 양수인 경우
2. 음수 간선이 있는 경우
    1) 음수 간선 순환은 없는 경우
    2) 음수 간선 순환이 있는 경우
벨만 포드의 시간 복잡도는 O(VE)로 다익스트라에 비해 느리다 (V:정점의 개수, E:간선의 개수)

벨만 포드 알고리즘
1.출발 노드를 설정
2. 최단 거리 테이블 초기화
3. 다음 과정을 n-1번 반복
    1) 전체 간선 E개를 하나씩 확인
    2) 각 간선을 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
3번의 과정을 한 번 더 수행
    최단 거리 테이블이 갱신된다면 음수 간선 순환이 존재
    
다익스트라
매번 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
음수 간선이 없다면 최적의 해

벨만 포드 알고리즘
매번 모든 간선을 전부 확인
    다익스트라 알고리즘에서의 최적의 해를 항상 포함
다익스타라 알고리즘에 비해 시간이 오래 걸리지만 음수 간선 순환을 탐지
'''

import sys
input = sys.stdin.readline
inf = int(1e9)

def bf(start):
    # 시작 노드 초기화
    dist[start] = 0
    # 전체 n번의 라운드를 반복
    for i in range(n):
        # 매 반복마다 '모든 간선'을 확인하며
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != inf and dist[next_node] > dist[cur]+cost:
                dist[next_node] = dist[cur] +cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n-1:
                    return True
    return False

# 노드의 개수 , 간선의 개수를 입력받기\
n,m = map(int, input().split())
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [inf] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b,c, = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append((a,b,c))
    
# 벨만 포드 알고리즘 수행
negative_cycle = bf(1) # 1번 노드가 시작 노드

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2,n+1):
        # 도달할 수 없는 경우 , -1 출력
        if dist[i] == inf:
            print('-1')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(dist[i])
            
# 백준 11657

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            time = edges[j][2]
            if dist[cur]+time < dist[next_node] and dist[cur] != inf:
                dist[next_node] = dist[cur]+time
                if i == n-1:
                    return True
    return False

n,m = map(int, input().split())
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))
inf = 1e4*(n-1)+1
dist = [inf]*(n+1)

if bf(1):
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i] == inf:
            print(-1)
        else:
            print(dist[i])   
