def solution(n,computers):
    visit=[False]*n
    cnt = 0  
    def dfs(i, computers, visit):
        visit[i] = True
        for j in range(n):
            if i != j and computers[i][j] == 1 and visit[j] == False:
                dfs(j,computers,visit)
    while bool(False in visit) == True:
        for i in range(n):
            if visit[i] == False:
                cnt += 1
                dfs(i, computers, visit)

    return cnt