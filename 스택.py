# 10828

import sys
input=sys.stdin.readline
n = int(input())
a=[]
def stack(x):
    if x == 'pop':
        if a==[]:
            print(-1)
        else:
            p=a.pop()
            print(p)
    elif x == 'top':
        if a==[]:
            print(-1)
        else:
            print(a[-1])
    elif x == 'size':
        print(len(a))
    elif x == 'empty':
        if a==[]:
            print(1)
        else:
            print(0)
    else:
        push,n = x.split()
        a.append(n)
for _ in range(n):
    x = input().strip()
    stack(x)
    
# 10773

k = int(input())
a=[]
for _ in range(k):
    n = int(input())
    if n != 0:
        a.append(n)
    else:
        a.pop()
print(sum(a))

