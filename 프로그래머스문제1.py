# 신규 아이디 추천

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for i in new_id:
        if i not in '~!@#$%^&*()=+[{]}:?,<>/':
            answer += i
    while '..' in new_id:
        answer=answer.replace('..','.')
    if answer[0] == '.'  and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[0:-1]
    if len(answer) == 0:
        answer='a'
    if len(answer) > 15:
        answer = answer[0:15]
        if answer[-1] == '.':
            answer = answer[0:14]
    if len(answer) == 1:
        answer = answer*3
    if len(answer) == 2:
        answer = answer+answer[1]
    
    return answer

# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    c_0=0
    c=0
    for i in lottos:
        if i == 0:
            c_0 += 1
        elif i in win_nums:
            c += 1       
    r=[6,6,5,4,3,2,1]
    
    answer = [r[c_0+c],r[c]]
    return answer

# 숫자 문자열과 영단어

def solution(s):
    s=s.replace('zero','0')
    s=s.replace('one','1')
    s=s.replace('two','2')
    s=s.replace('three','3')
    s=s.replace('four','4')
    s=s.replace('five','5')
    s=s.replace('six','6')
    s=s.replace('seven','7')
    s=s.replace('eight','8')
    s=s.replace('nine','9')            
    answer=int(s)
    return answer

# 크레인 인형뽑기 게임

def solution(board, moves):
    b=[]
    c=0
    for i in moves:
        i -= 1
        for j in range(len(board)):
            if board[j][i] != 0:
                b.append(board[j][i])
                if len(b)>1 and b[-2]==board[j][i]:
                    b.pop()
                    b.pop()
                    c += 1
                board[j][i]=0
                break  
                
    answer = c
    return answer

