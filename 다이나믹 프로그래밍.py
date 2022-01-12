# 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
# 이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록
# 일반적으로 두 가지 방식(탑다운과 보텀업)으로 구성
# 동적 계획법

# 자료 구조에서 동적 할당은 프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당
# 다이나믹 프로그래밍에서 '다이나믹'은 별 의미 없는 단어

# 최적 부분 구조(Optimal substructure)
# -큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결

# 중복되는 부분 문제(Overlapping Subproblem)
# -동일한 작은 문제를 반복적으로 해결

# 메모이제이션(Memoization)
# 한 번 계산한 결과를 메모리 공간에 메모
# 같은 문제를 다시 호출하면 메모했던 결과를 그대로
# 값을 기록해 놓는다는 점에서 캐싱(Cashing)

# 탑다운 방식은 하향식 / 보텀업 방식은 상향식
# 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식
# - 결과 저장용 리스트는 DP 테이블이라고 부릅니다.
# 메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념
# - 메모이제이션은 다이나믹 프로그래밍에 국한된 개념이 아님
# - 한 번 계산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있음

# 피보나치(탑다운)

d=[0]*100
def fibo(x):
    if x ==1 or x ==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]

print(fibo(99))

# 피보나치(보텀업)

d=[0]*100
d[1]=1
d[2]=1
n=99

for i in range(3, n+1):
    d[i]=d[i-1]+d[i-2]

print(d[n])

# 1003

t = int(input())
for i in range(t):
    n=int(input())
    a=[0]*(n+2)
    a[0],a[1]=1,0
    for j in range(2,n+2):
        a[j] = a[j-1] + a[j-2]
    if n != 0:
        print(a[n],a[n+1])
    else:
        print(1,0)
        
# 12865

n,k = map(int, input().split())
a=[[0 for _ in range(k+3)] for _ in range(n+1)]
for i in range(1,n+1):
    a[i][0],a[i][1]=map(int, input().split())
for i in range(3,k+3):
    for j in range(1,n+1):
        if i-2<a[j][0]:
            a[j][i] = a[j-1][i]
        else:
            a[j][i] = max(a[j-1][i], a[j-1][i-a[j][0]]+a[j][1])

print(a[n][k+2])

# 9184

w=[[[1]*21 for _ in range(21)] for _ in range(21)]
while True:
    a,b,c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        print('w(%d, %d, %d)'%(a,b,c), '=', 1)
    elif a > 20 or b > 20 or c > 20:
        print('w(%d, %d, %d)'%(a,b,c), '=', 1048576)
    else:
        for i in range(1,a+1):
            for j in range(1,b+1):
                for k in range(1,c+1):
                    if i<j<k:
                        w[i][j][k] =  w[i][j][k-1] + w[i][j-1][k-1] - w[i][j-1][k]
                    else:
                        w[i][j][k] = w[i-1][j][k] + w[i-1][j-1][k] + w[i-1][j][k-1] - w[i-1][j-1][k-1]
        print('w(%d, %d, %d)'%(a,b,c), '=', w[a][b][c])
        
# 1904

n=int(input())
if n ==1 :
    print(1)
elif n ==2 :
    print(2)
else:
    a,b=1,2
    for _ in range(n-2):
        a,b=b%15746,(a+b)%15746
    print(b)
    
# 9467

a=[1,1,1,2,2]+[0 for _ in range(95)]
t=int(input())
for i in range(95):
    a[i+5] = a[i]+a[i+4]
for _ in range(t):
    n = int(input())
    print(a[n-1])
    
# 1149

n = int(input())
a=[]
for _ in range(n):
    a.append(list(map(int, input().split())))
for i in range(1,n):
    a[i][0]+=min(a[i-1][1],a[i-1][2])
    a[i][1]+=min(a[i-1][0],a[i-1][2])
    a[i][2]+=min(a[i-1][1],a[i-1][0])
print(min(a[n-1]))

# 1932

import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(1,n):
    for j in range(len(a[i])):
        if j == 0:
            a[i][j] += a[i-1][j]
        elif j == len(a[i])-1:
            a[i][j] += a[i-1][j-1]
        else:
            a[i][j] += max(a[i-1][j-1],a[i-1][j])
print(max(a[n-1]))

