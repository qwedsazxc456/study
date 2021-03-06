# 2048 문제

def f(a,b):
    for i in range(len(a)):
        while 0 in a[i]:
            a[i].remove(0)
        for j in range(len(a[i])-1):
            if a[i][j]==a[i][j+1]:
                a[i][j] *=2
                a[i][j+1] =0
        while 0 in a[i]:
            a[i].remove(0)
        for j in range(len(a[i])):
            b[i][j] = a[i][j]
def re(a):
    for i in a:
        i.reverse()
def trans(a):
    for i in range(n):
        for j in range(n):
            a_t[j][i] = a[i][j]
    

T = int(input())
for test_case in range(1, T + 1):
    print(f'#{test_case}')
    n,s= input().split()
    n = int(n)
    a=[]
    for _ in range(n):
        a.append(list(map(int, input().split())))
    a_t=[[0]*n for _ in range(n)]
    b=[[0]*n for _ in range(n)]
    
    if s=='left':
        f(a,b)
        for i in range(n):
            for j in range(n):
                print(b[i][j],end=' ')
            print()
    elif s =='right':
        re(a)
        f(a,b)
        for i in range(n):
            for j in range(n):
                print(b[i][n-1-j],end=' ')
            print()
    elif s=='up':
        trans(a)
        f(a_t,b)
        for i in range(n):
            for j in range(n):
                print(b[j][i], end=' ')
            print()       
    elif s =='down':
        trans(a)
        re(a)
        f(a_t,b)
        for i in range(n):
            for j in range(n):
                print(b[j][n-1-i],end=' ')
            print()
            
# 4112

t=int(input())
for i in range(1,t+1):
    r1,r2 = map(int, input().split())
    n=0
    while min(r1,r2) > n*(n+1)/2:
        n += 1
    a,b=n,min(r1,r2)-(n*(n-1)//2)
    while max(r1,r2) > n*(n+1)/2:
        n += 1
    c,d=n,max(r1,r2)-(n*(n-1)//2)
    print(f'#{i}',max(c-a,d-b)) if b < d else print(f'#{i}',c-a+b-d)
    
# 1208

for i in range(10):
    d = int(input())
    h = list(map(int, input().split()))
    for _ in range(d):
        h[h.index(max(h))] -= 1
        h[h.index(min(h))] += 1
    print(f'#{i+1} {max(h)-min(h)}')
    
# 1206

for i in range(10):
    l = int(input())
    b = list(map(int, input().split()))
    s=0
    for j in range(2,l-2):
        if b[j] - max(b[j-2],b[j-1],b[j+1],b[j+2]) > 0: 
            s += b[j] - max(b[j-2],b[j-1],b[j+1],b[j+2])
    print(f'#{i+1} {s}')