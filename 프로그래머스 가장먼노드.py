def solution(n, edge):
    distance = [5e4]*(n+1)
    graph = [[] for i in range(n+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])          
    distance[1] = 0
    s = [(1,0)]
    while s:
        now, dis = s.pop(0)
        for i in graph[now]:
            if dis+1 < distance[i]:
                distance[i] = dis+1
                s.append((i , dis+1))
    while 5e4 in distance:
        distance.remove(5e4)
    answer = distance.count(max(distance))
    return answer