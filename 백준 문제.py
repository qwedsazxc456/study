# 1
# Hello World!를 출력하시오.

print('Hello World!')

# 2
# 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.

print('강한친구 대한육군')
print('강한친구 대한육군')

# 3
# \    /\
#  )  ( ')
# (  /  )
#  \(__)|

print('\\    /\\')
print(' )  ( \')')
print('(  /  )')
print(' \\(__)|')

# 4
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

# 5
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
print(int(a)+int(b))

# 6
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
print(int(a)-int(b))

# 7
# 두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
print(int(a)*int(b))

# 8
# 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.

a,b=input().split()
print(int(a)/int(b))

# 9
# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

a,b=input().split()
print(int(a)+int(b))
print(int(a)-int(b))
print(int(a)*int(b))
print(int(a)//int(b))
print(int(a)%int(b))

# 10
# 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

a,b,c=input().split()
A=int(a)
B=int(b)
C=int(c)
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

# 11

a=int(input())
b=input()
c=int(b[2])
d=int(b[1])
e=int(b[0])
b=int(b)
print(a*c, a*d,a*e,a*b,sep='\n')

# 12
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
    
# 13
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
    
# 14
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
    
# 15
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
        
# 16
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

# 17
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.

a = int(input())
for i in range(1,10):
    print(a,'*',i,'=',a*i)
    
# 18
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

n = int(input())
for i in range(n):
    a,b=input().split()
    a=int(a)
    b=int(b)
    print(a+b)
    
# 19
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

n = int(input())
print(int((n*(n+1))/2))

# 20
# 빠른 A+B

import sys
n = int(sys.stdin.readline())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
    
# 21
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

n = int(input())
for i in range(n):
    print(i+1)
    
# 22
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

n = int(input())
for i in range(n):
    print(n-i)
    
# 23
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 

import sys
n = int(input())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d'%(i+1,a+b))
    
# 24
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. 

import sys
n = int(input())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print('Case #%d: %d + %d = %d'%(i+1,a,b,a+b))

# 25
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

n = int(input())
for i in range(n):
    print('*'*(i+1))
    
# 26
# 오른쪽을 기준으로 정렬한 별

n = int(input())
for i in range(n):
    print(' '*(n-i-1) , '*'*(i+1),sep='')
    
# 27
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

import sys
n,x = map(int, sys.stdin.readline().split())
a = sys.stdin.readline().split()
for i in range(n):
    if int(a[i]) < x:
        print(a[i], end=' ')
        
# 28
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력의 마지막에는 0 두 개가 들어온다.

import sys
while True:
    a,b = map(int, sys.stdin.readline().split())
    if a == 0 and b ==0:
        break
    else:
        print(a+b)
        
# 29
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# eof

import sys
while True:
    try:
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break
    
# 30
# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
