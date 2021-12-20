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