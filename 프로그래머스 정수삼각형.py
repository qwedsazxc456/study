def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(0,i+1):
            if j == 0 :
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else :
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])          
    answer = max(triangle[len(triangle)-1])
    return answer