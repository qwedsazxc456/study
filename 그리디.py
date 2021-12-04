# 현재 상황에서 당장 좋은 것만 고르는 방법
# 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
# 정당성 분석 중요
# 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없음

# 11047

n,k = map(int, input().split())
coin=[]
for i in range(n):
    v=int(input())
    coin.append(v)

c=0
for i in coin[::-1]:
    c += k//i
    k %= i
    
print(c)   
        
# 1931

import sys
imput=sys.stdin.readline
n = int(input())
a=[]
for _ in range(n):
    s,e = map(int, input().split())
    a.append([s,e])
a.sort(key=lambda x:(x[1],x[0]))
c=1
end=a[0][1]
for i in range(1,n):
    if end <= a[i][0]:
        end = a[i][1]
        c += 1
print(c) 

# 11399

n = int(input())
a=list(map(int, input().split()))
a.sort()
s=0
for i in range(n):
    s += a[i]*(n-i)
print(s)   

# 1541

