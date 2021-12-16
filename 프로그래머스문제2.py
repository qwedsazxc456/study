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
    
# 문자열 압축하기

def solution(s):
    c=1
    l=len(s)
    t=0
    for i in range(1,len(s)//2+1):
        for j in range(0,len(s)-i,i):
            if s[j:j+i]!=s[j+i:j+2*i]:
                if c != 1:
                    t += len(str(c))
                c=1
                t += i
                if j+2*i>=len(s):
                    t += len(s[j+i:len(s)])
            else:
                c += 1
                if j == len(s)-2*i:
                    t += len(str(c))
                    t += i
                    c=1                           
        if t < l:
            l=t
        t=0
    return l

# 타겟넘버

from collections import deque
def solution(numbers, target):
    a=deque([0])
    for i in range(len(numbers)):
        for _ in range(2**i):
            p=a.popleft()
            a.append(p+numbers[i])
            a.append(p-numbers[i])
    c=0
    for i in a:
        if i == target:
            c += 1
    return c

# 메뉴 리뉴얼

from itertools import combinations as comb
from collections import Counter as count
def solution(orders, course):
    answer = []
    for i in course:
        a=[]
        for j in orders:
            li=list(comb(j,i))
            for l in li:
                li_2=[]
                for t in l:
                    li_2.append(t)
                li_2.sort()
                s=''.join(li_2)
                a.append(s)
        c=count(a)
        if c:
            M=max(c.values())
            if M > 1:
                for k in c:
                    if c[k] == M:
                        answer.append(k)

    answer.sort()       
    return answer

# 더 맵게

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    c=0
    while scoville[0]<K:        
        f=heapq.heappop(scoville)
        s=heapq.heappop(scoville)
        heapq.heappush(scoville,f+2*s)  
        c+=1
        if len(scoville) ==1 and scoville[0]<K:
            return -1
    
    return c

