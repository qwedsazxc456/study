# 오픈채팅방

def solution(record):
    d={}
    answer = []
    for i in record:
        if len(i.split()) == 3:
            a,b,c=i.split()
            d[b]=c
    for i in record:
        if i[:5] == 'Leave':
            a,b = i.split()
            answer.append('%s님이 나갔습니다.'%d[b])
            
        if i[:5] == 'Enter':
            a,b,c = i.split()
            answer.append('%s님이 들어왔습니다.'%d[b])     
    
    return answer

# 멀쩡한 사각형

from math import ceil,gcd
def solution(w,h):
    g=gcd(w,h)
    answer = 0
    m,M=min(w,h),max(w,h)
    for i in range(m//g):
        a,b = i*M/m, (i+1)*M/m
        answer += ceil(b)-int(a)
    answer = w*h-answer*g
    return answer

# 짝지어 제거하기

def solution(s):
    a=[]
    for i in s:
        if not a:
            a.append(i)
        else:
            if i == a[-1]:
                a.pop()
            else:
                a.append(i)
    if not a:
        return 1
    else:
        return 0