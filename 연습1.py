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
#