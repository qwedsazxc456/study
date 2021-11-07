# 1
# python 언어에서 가장 기본적인 명령이 출력문이다.
# print( )를 이용해 다음 단어를 출력하시오.

# Hello

print('Hello')

# 2
# 이번에는 공백( )을 포함한 문장을 출력한다.
# 다음 문장을 출력해보자.

# Hello World

print('Hello World')

# 3
# 이번에는 줄을 바꿔 출력하는 출력문을 연습해보자.
# 다음과 같이 줄을 바꿔 출력해야 한다.

# Hello
# World

print('Hello')
print('World')

# 4
# 이번에는 작은 따옴표(')(single quotation mark)가 들어있는
# 출력문 연습을 해보자.

# 다음 문장을 출력하시오.

# 'Hello'

print("'Hello'")

# 5
# 이번에는 큰따옴표(")(double quotation mark)가 포함된 출력문을 연습해보자.

# 다음 문장을 출력하시오.

# "Hello World"
# (단, 큰따옴표도 함께 출력한다.)

print('"Hello World"')

# 6
# 이번에는 특수문자 출력에 도전하자!!

# 다음 문장을 출력하시오.

# "!@#$%^&*()'
# (단, 큰따옴표와 작은따옴표도 함께 출력한다.)

print('\"!@#$%^&*()\'')

# 7
# 윈도우 운영체제의 파일 경로를 출력하는 연습을 해보자.
 
# 파일 경로에는 특수문자들이 포함된다.

# 다음 경로를 출력하시오.

# "C:\Download\'hello'.py"
# (단, 따옴표도 함께 출력한다.)

print('\"C:\\Download\\\'hello\'.py\"')

# 8
# 출력문 연습의 마지막 문제이다.
# (생각과 시도를 많이 해야하는 문제들은 한 두 문제씩 넘겼다가 나중에 풀어보면 된다.)

# 이번에는 다음과 같은 python프로그램의 소스코드를 출력해보자.

# print("Hello\nWorld")

# 위 코드를 정확히 그대로 출력하시오.(공백문자 주의)

print('print(\"Hello\\nWorld\")')

# 9 
# 문자(character)는
# 0~9, a~z, A~Z, !, @, #, {, [, <, ... 과 같이 
# 길이가 1인 기호라고 할 수 있다.

# 변수에 문자 1개를 저장한 후
# 변수에 저장되어 있는 문자를 그대로 출력해보자.

c=input()
print(c)

# 10
# 변수에 정수값을 저장한 후 정수로 변환하여 출력해보자.

n=input()
n=int(n)
print(n)

# 11
# 변수에 실수값을 저장한 후
# 변수에 저장되어 있는 값을 그대로 출력해보자.

f = input()
f = float(f)
print(f)

# 12
# 줄을 바꿔 정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

a = int(input())
b = int(input())
print(a)
print(b)

# 13
# 줄을 바꿔 문자(character) 2개를 입력받고, 순서를 바꿔 한 줄씩 출력해보자.

a = input()
b = input()
print(b)
print(a)

# 14
# 실수(real number) 1개를 입력받아 줄을 바꿔 3번 출력해보자.

f = input()
f = float(f)
print(f)
print(f)
print(f)

# 15
# 공백을 두고 입력된정수(integer) 2개를 입력받아 줄을 바꿔 출력해보자.

a,b = input().split()
print(a)
print(b)

# 16
# 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.

a,b = input().split()
print(b)
print(a)

# 17
# 정수(integer), 실수, 문자(character), 문자열(string) 등 1개만 입력받아 한 줄로 3번 출력해보자.

a = input()
print(a,a,a)

# 18
# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

a,b=input().split(':')
print(a,b,sep=':')

# 19
# "연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

y, m, d = input().split('.')
print(d,m,y,sep='-')

# 20
# 주민번호는 다음과 같이 구성된다.
# XXXXXX-XXXXXXX

# 왼쪽 6자리는 생년월일(YYMMDD)이고, 오른쪽 7자리는 성별,출생지역,확인코드로 구성되어있다.
# 주민번호를 입력받아 형태를 바꿔 출력해보자.

a,b = input().split('-')
print(a+b)

# 21
# 알파벳과 숫자로 이루어진 단어 1개가 입력된다.
# 입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.

s = input()
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# 22
# 6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.

s = input()
print(s[0:2],s[2:4],s[4:6])

# 23
# 시:분:초 형식으로 시간이 입력될 때 분만 출력해보자.

a,b,c = input().split(':')
print(b)

# 24
# 알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
# 순서대로 붙여 출력하는 프로그램을 작성해보자.

w1, w2 = input().split()
s = w1 + w2
print(s)

# 25
# 정수 2개를 입력받아
# 합을 출력하는 프로그램을 작성해보자.

a, b = input().split()
print(int(a)+int(b))

# 26
# 실수 2개를 입력받아
# 합을 출력하는 프로그램을 작성해보자.

a = input()
b = input()
print(float(a)+float(b))

# 27
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자.

a = input()
n = int(a)            
print('%x' % n)

# 28
# 10진수를 입력받아 16진수(hexadecimal)로 출력해보자. (대문자)

a = input()
n = int(a)            
print('%X' % n)

# 29
# 16진수를 입력받아 8진수(octal)로 출력해보자.

a = input()
n = int(a, 16)   
print('%o' % n) 

# 30
# 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.

n = ord(input())
print(n)

# 31
# 10진 정수 1개를 입력받아
# 유니코드 문자로 출력해보자.

a = int(input())
print(chr(a))

# 32
# 입력된 정수의 부호를 바꿔 출력해보자.

a = int(input())
print(-a)

# 33
# 문자 1개를 입력받아 그 다음 문자를 출력해보자.
# 영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

a = input()
a = ord(a)
print(chr(a+1))

# 34
# 정수 2개(a, b)를 입력받아 a에서 b를 뺀 차를 출력하는 프로그램을 작성해보자.

a , b = input().split()
print(int(a)-int(b))

# 35
# 실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

f1, f2 = input().split()
f1 = float(f1)
f2 = float(f2)
print(f1*f2)

# 36
# 단어와 반복 횟수를 입력받아 여러 번 출력해보자.

w, n = input().split()
print(w*int(n))

# 37
# 반복 횟수와 문장을 입력받아 여러 번 출력해보자.

n = input()
s = input()
print(int(n)*s)

# 38
# 정수 2개(a, b)를 입력받아
# a를 b번 곱한 거듭제곱을 출력하는 프로그램을 작성해보자.

a,b=input().split()
c = int(a)**int(b) 
print(c)

# 39
# 실수 2개(f1, f2)를 입력받아
# f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.

f1, f2 = input().split()
f1 = float(f1)
f2 = float(f2)
print(f1**f2)

# 40
# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.

a,b=input().split()
a = int(a)
b = int(b)
print(a//b)

# 41
# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.

a,b=input().split()
a = int(a)
b = int(b)
print(a%b)

# 42
# 실수 1개를 입력받아
# 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.

a=float(input())
print( format(a, ".2f") )

# 43
# 실수 2개(f1, f2)를 입력받아
# f1 을 f2 로 나눈 값을 출력해보자. 
# 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력한다.

f1, f2 = input().split()
f1 = float(f1)
f2 = float(f2)
print(format(f1/f2, '.3f'))

# 44
# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.

a,b=input().split()
a = int(a)
b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,'.2f'))

# 45
# 정수 3개를 입력받아 합과 평균을 출력해보자.

a,b,c, = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a+b+c, format((a+b+c)/3, '.2f'))

# 46
# 정수 1개를 입력받아 2배 곱해 출력해보자.

a = int(input())
print(a*2)

# 47
# 정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력해보자.

a,b = input().split()
a = int(a)
b = int(b)
print(a<<b)

# 48
# 두 정수(a, b)를 입력받아
# a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

a,b = input().split()
a = int(a)
b = int(b)
print(a<b)

# 49
# 두 정수(a, b)를 입력받아
# a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

a,b = input().split()
a = int(a)
b = int(b)
print(a==b)

# 50
# 두 정수(a, b)를 입력받아
# b의 값이 a의 값 보다 크거나 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

a,b = input().split()
a = int(a)
b = int(b)
print(a<=b)

# 51
# 두 정수(a, b)를 입력받아
# a의 값이 b의 값과 서로 다르면 True 를, 같으면 False 를 출력하는 프로그램을 작성해보자.

a,b = input().split()
a = int(a)
b = int(b)
print(a!=b)

# 52
# 정수가 입력되었을 때, True/False 로 평가해주는 프로그램을 작성해보자.

n = int(input())
print(bool(n))

# 53
# 정수값이 입력될 때,
# 그 불 값을 반대로 출력하는 프로그램을 작성해보자.

n = not(bool(int(input())))
print(n)

# 54
# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = input().split()
a = int(a)
b = int(b)
print(bool(a) and bool(b))

# 55
# 2개의 정수값이 입력될 때,
# 그 불 값이 하나라도 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = input().split()
a = int(a)
b = int(b)
print(bool(a) or bool(b))

# 56
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = input().split()
a = int(a)
b = int(b)
a = bool(a)
b = bool(b)
print((a==True and b==False) or (a==False and b == True))

# 57
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 서로 같을 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = input().split()
a = int(a)
b = int(b)
a = bool(a)
b = bool(b)
print((a==True and b==True) or (a==False and b == False))

# 58
# 2개의 정수값이 입력될 때,
# 그 불 값(True/False) 이 모두 False 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a,b = input().split()
a = int(a)
b = int(b)
a = bool(a)
b = bool(b)
print(a==False and b == False)

# 59
# 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.

a = int(input())
print(~a)

# 60
# 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.

a,b = input().split()
a = int(a)
b = int(b)
print(a&b)

# 61
# 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.

a,b = input().split()
a = int(a)
b = int(b)
print(a|b)

# 62
# 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
# 비트 단위가 서로 다른지???

a,b = input().split()
a = int(a)
b = int(b)
print(a^b)

# 63
# 입력된 두 정수(a, b) 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

a, b = input().split()
a = int(a) 
b = int(b)
c = (a if (a>=b) else b)
print(int(c))

# 64
# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 3항 연산을 사용한다.

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = (a if (a<=b) else b) if ((a if (a<=b) else b)<c) else c
print(d)

# 65
# 3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)
    
# 66
# 3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2==0:
    print('even')
else:
    print('odd')
if b%2==0:
    print('even')
else:
    print('odd')
if c%2==0:
    print('even')
else:
    print('odd')
    
# 67
# 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
# 음수이면서 짝수이면, A
# 음수이면서 홀수이면, B
# 양수이면서 짝수이면, C
# 양수이면서 홀수이면, D
# 를 출력한다.

a = int(input())
if a<0:
    if a%2==0:
        print('A')
    else:
        print('B')
else:
    if a%2==0:
        print('C')
    else:
        print('D')
        
# 68
# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
# 평가 기준
# 점수 범위 : 평가
#  90 ~ 100 : A
#  70 ~   89 : B
#  40 ~   69 : C
#    0 ~   39 : D
# 로 평가되어야 한다.

a = int(input())
if a>=90:
    print('A')
else:
    if a >=70:
        print('B')
    else:
        if a >=40:
            print('C')
        else: print('D')
        
# 69
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

a = input()
if a == 'A':
    print('best!!!')
else:
    if a == 'B':
        print('good!!')
    else:
        if a == 'C':
           print('run!')
        else:
            if a == 'D':
                print('slowly~')
            else:
                print('what?')

# 70
# 월이 입력될 때 계절 이름이 출력되도록 해보자.
# 월 : 계절 이름
# 12, 1, 2 : winter
#   3, 4, 5 : spring
#   6, 7, 8 : summer
#   9, 10, 11 : fall

a = int(input())
if a == 12 or a==1 or a==2:
    print('winter')
else:
    if a == 3 or a==4 or a==5:
        print('spring')
    else:
        if a == 6 or a==7 or a==8:
            print('summer')
        else:
            print('fall')
            
# 71
# 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

n=1
while n != 0:
    n=int(input())
    if n != 0:
        print(n)

# 72
# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자. - 1까지

n=int(input())
while n!=0 :
    print(n)
    n = n-1
    
# 73
# 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자. - 0까지/입력숫자제외

n=int(input())
while n > 0 :
    n = n-1
    print(n)
    
# 74
# 영문 소문자(a ~ z) 1개가 입력되었을 때,
# a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
# a부터 입력한 문자까지 순서대로 공백을 두고 한 줄로 출력한다.

o = ord(input())
a = ord('a')
while a <= o:
    print(chr(a), end=' ')
    a = a+1

# 75
# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
# 0부터 그 수까지 줄을 바꿔 한 개씩 출력한다.

a = int(input())
b = 0
while b <= a:
    print(b)
    b += 1
    
# 76
# 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
# for 이용

a = int(input())
for i in range(0,a+1):
    print(i)
    
# 77
# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

a = int(input())
s = 0
for i in range(1,a+1):
    if i%2==0:
        s += i
print(s)

# 78
# 영문 소문자 'q'가 입력될 때까지
# 입력한 문자를 계속 출력하는 프로그램을 작성해보자.

while a != 'q':
    a = input()
    print(a)

# 79
# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.

a = 0
b = int(input())
s = 0
while s < b:
    a += 1
    s += a
print(a)