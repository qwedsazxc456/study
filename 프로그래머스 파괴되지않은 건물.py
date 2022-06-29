def solution(board, skill):
    mat = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for i in skill:
        if i[0] == 1:
            mat[i[1]][i[2]] -= i[5]
            mat[i[1]][i[4]+1] += i[5]
            mat[i[3]+1][i[2]] += i[5]
            mat[i[3]+1][i[4]+1] -= i[5]
        else:
            mat[i[1]][i[2]] += i[5]
            mat[i[1]][i[4]+1] -= i[5]
            mat[i[3]+1][i[2]] -= i[5]
            mat[i[3]+1][i[4]+1] += i[5]

    for i in range(len(board)+1):
        for j in range(1,len(board[0])+1):
            mat[i][j] += mat[i][j-1]
    for i in range(len(board[0])+1):
        for j in range(1,len(board)+1):
            mat[j][i] += mat[j-1][i]
    cnt=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + mat[i][j] >=1:
                cnt += 1     
    answer = cnt
    return answer