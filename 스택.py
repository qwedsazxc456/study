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

# 9012

n = int(input())
b=[]
for i in range(n):
    a=input()
    for j in a:
        if j == '(':
            b.append(1)
        else:
            if b:
                b.pop()
            else:
                b.append(0)
                break
    if not b:
        print('YES')
    else:
        print('NO')
    b=[]
    
# 4949

while True:
    a=[]
    b=True
    s=input()
    if s=='.':
        break
    for i in s:
        if i =='(' or i =='[':
            a.append(i)
        elif i ==')':
            if not a :
                b=False
                break
            elif a[-1]=='(':
                a.pop()
            else:
                b=False
                break
        elif i == ']':
            if not a:
                b=False
                break
            elif a[-1]=='[':
                a.pop()
            else:
                b=False
                break
    if b==True and not a:
        print('yes')
    else:
        print('no')

# 1874

n=int(input())
a=[]
b=[0]
c=[]
for _ in range(n):
    a.append(int(input()))
a.reverse()
i=1
while a:
    if b[-1]==a[-1]:
        a.pop()
        b.pop()
        c.append('-')
    else:
        b.append(i)
        c.append('+')
        i += 1
    if i == n+2:
        break
if a:
    print('NO')
else:
    for i in c:
        print(i)

# 17298

n = int(input())
a = list(map(int, input().split()))
nge=[-1]*n
stack=[]
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        p=stack.pop()
        nge[p]=a[i]
    stack.append(i)
print(*nge)