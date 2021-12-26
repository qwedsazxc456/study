# 18258

import sys
from collections import deque

input=sys.stdin.readline
n = int(input())
a=deque()
def que(x):
    if x == 'pop':
        if not a:
            print(-1)
        else:
            p=a.popleft()
            print(p)
    elif x == 'front':
        if not a:
            print(-1)
        else:
            print(a[0])
    elif x == 'back':
        if not a:
            print(-1)
        else:
            print(a[-1])
    elif x == 'size':
        print(len(a))
    elif x == 'empty':
        if not a:
            print(1)
        else:
            print(0)
    else:
        push,n = x.split()
        a.append(n)
for _ in range(n):
    x = input().strip()
    que(x)

# 2164

from collections import deque

n=int(input())
a=deque([i for i in range(n,0,-1)])
while len(a) > 1:
    a.pop()
    p=a.pop()
    a.appendleft(p)
print(a[0])

# 11866

n,k=map(int, input().split())
l=k-1
a=[i for i in range(1,n+1)]
b=[]
while a:
    p=a.pop(k-1)
    b.append(str(p))
    k += l
    if k > len(a) and a:
        k=k%len(a)
        if k == 0:
            k=len(a)
print('<',end='')
for i in b[:-1]:
    print(i,', ',end='',sep='')
print(b[-1],end='')
print('>')

# 1966

from collections import deque
t = int(input())
for i in range(t):
    n,m=map(int, input().split())
    a=deque(list(map(int, input().split())))
    b=deque([i for i in range(n)])
    c=0
    r=-1
    while r != m:
        if a[0]==max(a):
            c += 1
            a.popleft()
            r=b.popleft()
        else:
            p=a.popleft()
            q=b.popleft()
            a.append(p)
            b.append(q)
    print(c)
    
# 5430

from collections import deque
import sys
input=sys.stdin.readline

t = int(input())
for _ in range(t):
    f=input().rstrip()
    n=int(input())
    a=input().rstrip()
    if a=='[]':
        a=[]
    else:
        a=deque(a[1:-1].split(','))
    e=0
    r=0
    for i in f:
        if i == 'R':
            r += 1
        else:
            if not a:
                print('error')
                e=1
                break
            elif r%2 == 0:
                a.popleft()
            else:
                a.pop()
    if e == 0:
        if r % 2 == 0:
            print('['+','.join(a)+']')
        else:
            a.reverse()
            print('['+','.join(a)+']')
            
