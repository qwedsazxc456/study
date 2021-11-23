# Hello World!를 출력하시오.

print('Hello World!')

# 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.

print('강한친구 대한육군')
print('강한친구 대한육군')

# \    /\
#  )  ( ')
# (  /  )
#  \(__)|

print('\\    /\\')
print(' )  ( \')')
print('(  /  )')
print(' \\(__)|')

# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|

print('|\\_/|')
print('|q p|   /}')
print('( 0 )\"\"\"\\')
print('|"^"`    |')
print('||_/=\\\\__|')

# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
print(int(a)+int(b))

# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
print(int(a)-int(b))

# 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
print(int(a)*int(b))

# 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
print(int(a)/int(b))

# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

a,b=input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a)%int(b))

# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

a,b,c=input().split()
A=int(a)
B=int(b)
C=int(c)
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

# 

a=int(input())
b=input()
c=int(b[2])
d=int(b[1])
e=int(b[0])
b=int(b)
print(a*c, a*d,a*e,a*b,sep='\n')

# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

a,b=input().split()
a = int(a)
b = int(b)
if a<b:
    print('<')
elif a>b:
    print('>')
else:
    print('==')
    
# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

a = int(input())
if a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >= 70:
    print('C')
elif a >= 60:
    print('D')
else:
    print('F')
    
# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

a = int(input())
if a%4 ==0:
    if a%100 != 0:
        print(1)
    elif a%400 ==0:
        print(1)
    else:
        print(0)
else:
    print(0)
    
# 사분면 고르기

a = int(input())
b = int(input())

if a > 0:
    if b > 0:
        print(1)
    else:
        print(4)
else:
    if b > 0:
        print(2)
    else:
        print(3)
        
# 45분 앞서는 시간으로 바꾸는 것

h,m = input().split()
h = int(h)
m = int(m)
if m-45 <0:
    if h != 0:
        h -= 1
        m += 15
    else:
        h = 23
        m += 15
else:
    m -= 45
print(h,m)

# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.

a = int(input())
for i in range(1,10):
    print(a,'*',i,'=',a*i)
    
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

n = int(input())
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    print(a+b)
    
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
print(int((n*(n+1))/2))

# 빠른 A+B

import sys
n = int(sys.stdin.readline())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
    
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

n = int(input())
for i in range(n):
    print(i+1)
    
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

n = int(input())
for i in range(n):
    print(n-i)
    
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 

import sys
n = int(input())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d'%(i+1,a+b))
    
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. 

import sys
n = int(input())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d + %d = %d'%(i+1,a,b,a+b))

# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

n = int(input())
for i in range(n):
    print('*'*(i+1))
    
# 오른쪽을 기준으로 정렬한 별

n = int(input())
for i in range(n):
    print(' '*(n-i-1) , '*'*(i+1),sep='')
    
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

import sys
n,x = map(int, sys.stdin.readline().split())
a = sys.stdin.readline().split()
for i in range(n):
    if int(a[i]) < x:
        print(a[i], end=' ')
        
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력의 마지막에는 0 두 개가 들어온다.

import sys
while True:
    a,b = map(int, sys.stdin.readline().split())
    if a == 0 and b ==0:
        break
    else:
        print(a+b)
        
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# eof

import sys
while True:
    try:
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break
    
# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

n = int(input())
n2 = n
d = 0

while True:
    a = n//10
    b = n%10
    n = 10*b+(a+b)%10
    d += 1
    if n == n2:
        break
print(d)    

# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

n=int(input())
a = list(map(int, input().split()))
print(min(a),max(a))

# 9개의 서로 다른 자연수가 주어질 때,
# 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

a = []
for i in range(9):
    a.append(int(input()))
    
print(max(a))
print(a.index(max(a))+1)

# 세 개의 자연수 A, B, C가 주어질 때
# A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

a = int(input())
b = int(input())
c = int(input())
d = str(a*b*c)
e = 0
for i in range(10):
    for j in range(len(d)):
        if int(d[j]) == i:
           e += 1
    print(e)
    e=0
    
# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 
# 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.

a=[]
d=[]
for i in range(10):
    b = int(input())
    a.append(b)
for i in range(10):
    c = a[i]%42
    d.append(c)
print(len(set(d)))

# 모든 점수를 점수/M*100으로 고쳤다.
# 새로운 평균을 구하는 프로그램을 작성하시오.

a=int(input())
b=map(int, input().split())
b = list(b)
print(sum(b)/a*100/max(b))

# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

n = int(input())
b = 0
c = 0
for i in range(n):
    a = input()
    for j in range(len(a)):
       if a[j] == 'O':
            b += 1
            c += b
       else:
           b=0
    print(c)
    b=0
    c=0
    
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

n = int(input())
c = 0
for i in range(n):
    a = map(int, input().split())
    a = list(a)
    b = (sum(a)-a[0])/(len(a)-1)
    for j in range(1,len(a)):
        if a[j]>b:
            c += 1
    print('%.3f'%(c/(len(a)-1)*100),'%',sep='')
    c = 0
    
# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

def solve(a):
    return sum(a)

# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

def sn(a):
    a = str(a)
    b = 0
    for i in range(len(a)):
        b += int(a[i])
    c = int(a)+b
    return c

i=1
l=[]
while i <= 10000:
   l.append(sn(i))
   i += 1
   
for i in range(1,10001):
    if i not in l:
        print(i)
        
# N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

a = int(input())
b =0
if a < 100:
    print(a)
elif a<1000:
    for i in range(100,a+1):
        i = str(i)
        if int(i[1])-int(i[0])==int(i[2])-int(i[1]):
            b += 1
    print(99+b)
else: print(144)     

# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

a=input()
print(ord(a))      

# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

a = int(input())
b = list(map(int,input()))
print(sum(b))

# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오

S = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')
    
# 10250
n = int(input())
for i in range(n):
    h,w,n=map(int, input().split())
    f = n%h
    r = n//h+1
    if f == 0:
        r = r-1
        f = h
    print(f*100+r)    
    
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

a = int(input())
for i in range(a):
    b,c = input().split()
    b = int(b)
    for j in range(len(c)):
        print(c[j]*b,sep='',end='')
    print()
    
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

a = input().upper()
b = list(set(a))
c = []
d = 0
for i in b:
    c.append(a.count(i))
for i in c:
    if i == max(c):
        d += 1
if d > 1:
    print('?')
else:
    print(b[c.index(max(c))])
    
# 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

a=input().split()
print(len(a))
    
# 2908

a,b=input().split()
c=int(a[2]+a[1]+a[0])
d=int(b[2]+b[1]+b[0])
if c > d:
    print(c)
else:
    print(d)
    
# 5622
a = input()
b = []
for i in a:
    if i in 'ABC':
        b.append(3)
    elif i in 'DEF':
        b.append(4)
    elif i in 'GHI':
        b.append(5)
    elif i in 'JKL':
        b.append(6)
    elif i in 'MNO':
        b.append(7)
    elif i in 'PQRS':
        b.append(8)
    elif i in 'TUV':
        b.append(9)
    elif i in 'WXYZ':
        b.append(10)
print(sum(b))

# 2941

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
b = input()

for i in a:
    b = b.replace(i,'.')
print(len(b))

# 1712

a,b,c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)
    
# 2292

n=int(input())
a=0
while 3*a**2+3*a+1<n:
    a += 1
print(a+1)

# 1193

x = int(input())
n = 1
while n*(n+1)/2 < x:
    n += 1
a = (n**2-n)/2
if n % 2 ==0:
    print('%d/%d'%(x-a,n+1-(x-a)))
else:
    print('%d/%d'%(n+1-(x-a),x-a))
    
# 2869

a,b,v = map(int, input().split())
c = (v-a)//(a-b)
if (v-a)%(a-b)==0:
    print(c+1)
else:
    print(c+2)
    
# 2775

from math import factorial

t = int(input())
s = 0
for i in range(t):
    k = int(input())
    n = int(input()) 
    for j in range(1,n+1):
        s += factorial(n+k-2)/factorial(k-1)/factorial(n-1)*j
        n -= 1
    print(int(s))
    s = 0
        
# 2839

n = int(input())
a=-1
b=0
c=[]
while 5*a < n:
    a += 1
    if 5*a == n:
        c.append(a)
    while 5*a+3*b < n:
        b += 1
        if 5*a+3*b == n:
            c.append(a+b)
            b = 0
            break
        if 5*a+3*b > n:
            b = 0
            break
if c == []:
    print(-1)
else:
    print(min(c))

# 10757

a,b=map(int, input().split())
print(a+b)

# 1011

t = int(input())
n = 0
for i in range(t):
    x,y = map(int, input().split())
    while True:
        if y-x == 1:
            print(1)
            break
        else:
            n += 1
            if y-x <= n*(n+1):
                print(2*n)
                n = 0
                break
            else:
                if y-x <= n*(n+1)+n+1:
                    print(2*n+1)
                    n = 0
                    break

# 2749
n = int(input())
n = n%1500000
a,b = 0,1
for i in range(n):
    a,b = b%1000000,(a+b)%1000000  
print(a%1000000)

# 1978
n = int(input())
b = list(map(int, input().split()))
a=[2]
c=0
for i in range(3,1000):
    for j in a:
        if i%j ==0:
            c += 1
    if c == 0:
        a.append(i)
    c = 0
for i in b:
    if i in a:
        c += 1
print(c)         

# 2581

m=int(input())
n=int(input())

a=[2]
b=[]
c=0
for i in range(3,10000):
    for j in a:
        if i%j ==0:
            c += 1
    if c == 0:
        a.append(i)
    c = 0

for i in range(m,n+1):
    if i in a:
        b.append(i)
        
if b == []:
    print(-1)
else:
    print(sum(b))
    print(min(b))
    
# 1316

n = int(input())
c = 0
d = 0
for i in range(n):
    a = input()
    l = len(a)
    for j in range(l-1):
        if a[j] != a[j+1]:
            if a[j] in a[j+2:l]:
                c += 1
    if c == 0:
        d += 1
    c = 0
print(d)
                
# 11653

n = int(input())
a = []
i = 2
if n != 1:
    while i <= n:
        if n % i == 0:
            a.append(i)
            n = n//i
        else:
            i += 1
    if a == []:
        print(n)
    else:
        a.sort()
        for i in a:
            print(i)
          
# 1929

m,n = map(int, input().split())

c=0
for i in range(m,n+1):
    for j in range(2,int(i**0.5)+1):
        if i%j ==0:
            c += 1
            break
    if c == 0:
        if i != 1:    
            print(i)
    c=0
    
# 4948

b=0
c=0
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n+1,n*2+1):
        for j in range(2,int(i**0.5)+1):
            if i%j ==0:
                c += 1
                break
        if c == 0:
            if i != 1:
                b += 1             
        c=0
    print(b)
    b=0

# 9020

n = int(input())

a=[2]
c=0
for i in range(3,10000,2):
    for j in a:
        if i%j ==0:
            c += 1
    if c == 0:
        a.append(i)
    c = 0

b=[]
c=[]
for _ in range(n):
    p = int(input())
    e=0
    while a[e]<p/2:
        e +=1
    for i in a[e:]:
        for j in a[e::-1]:
            if p == i+j:
                b.append(j)
                b.append(i)                
    if len(b)==2:
        print(b[0],b[1])
    else:
        for i in range(0,int(len(b)/2)+2,2):
            c.append(b[i+1]-b[i])
        d=c.index(min(c))
        print(b[2*d],b[2*d+1])
        d=0
    b=[]
    c=[]    

# 1085

x,y,w,h = map(int, input().split())
print(min(x,y,abs(w-x),abs(y-h)))

# 3009

a = []
for _ in range(3):
    a.append(input().split())
for i in range(3):
    c = 0
    for j in range(3):
        if a[i][0] != a[j][0]:
            c += 1
    if c == 2:
        print(a[i][0], end=' ')
        
for i in range(3):
    c = 0
    for j in range(3):
        if a[i][1] != a[j][1]:
            c += 1
    if c == 2:
        print(a[i][1])

# 4153

while True:
    l = list(map(int, input().split()))
    if l==[0,0,0]:
        break
    l.sort()
    if l[2]**2 == l[0]**2+l[1]**2:
        print('right')
    else:
        print('wrong')
        
# 3053

from math import pi

r = int(input())
print(r**2*pi)
print(r**2*2)

# 1002

n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d1 = ((x2-x1)**2+(y2-y1)**2)**0.5
    d2 = abs(r2-r1)
    d3 = abs(r2+r1)
    if d1 ==0 and d2==0:
        print(-1)
    else:    
        if d1 < d2 or d1 > d3:
            print(0)
        elif d1 == d2 or d1 == d3:
            print(1)
        else:
            print(2)

# 10872

n = int(input())

def factorial(n):
    if n ==0:
        return 1
    else:
        return factorial(n-1)*n

print(factorial(n))

# 10870

n = int(input())

def fi(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    else:
        return fi(n-1)+fi(n-2)

print(fi(n))

#   
        
        
                
    
        
        
        
    