# 시간 측정

import time
start_time = time.time()
# 코드
end_time = time.time()
print(end_time-start_time)



# 자료형

# 지수 표현방식

print(3e9) # 3*10**9
# 실수형으로 출력


# 실수
a=0.3
b=0.6
print(a+b) # 2진수로 0.9를 표현할 수 없어서 최대한 가까운값으로 표현
# round 함수 사용
print(round(a+b,2)) # 둘째자리 까지 표현 세번째자리에서 반올림
# 나누기 연산자(/)는 실수형 반환


# 리스트 컴프리헨션

# 반복문과 조건문으로 초기화

array=[i for i in range(10)]
array_2=[i for i in range(10) if i%2==0]
array_3=[i*i for i in range(10)]
array_4=[]
for i in range(10):
    if i%2 == 0:
        array_4.append(i)

print(array) 
print(array_2) 
print(array_3) 
print(array_4) # array_3의 값과 같다

# 2차원 리스트를 초기화 할때 효과적

m,n = 3,4
array = [[0]*m for _ in range(n)]
array_2 = [[0]*m]*n # 리스트 안에 포함된 리스트를 같은 객체로 인식
array[1][1] = 1
array_2[1][1] = 1

print(array) 
print(array_2)

# 리스트 관련 메서드
# append()
# sort() -오름차순 / sort(reverse=True)- 내림차순
# reverse()
# insert(인덱스,값) 뒤에 값 인덱스 하나씩 뒤로
# count(값)
# remove(값) 하나만 제거

# remove 특정값 모두 제거 하기
a = [1,2,3,4,5,5,5]
remove_set={3,5}
result=[i for i in a if i not in remove_set]
print(result)


# 문자열은 인덱싱과 슬라이싱 가능 변경은 불가능


# 튜플

# 한번 선언한 값을 변경 불가능
# ()
# 공간 효율적

# 튜플을 사용하면 좋은 경유

# 서로 다른 성질 묶어서 관리
# 데이터의 나열을 해싱(hashing)의 키값으로 사용
# - 튜플은 변경 불가능 하므로 키값으로 사용 가능 / 리스트는 불가능
# 리스트 보다 메모리 효율적


# 사전 자료형
# keys() / values() 객체 반환 list()로 list 형태 만들어서 사용


# 집합 자료형
# 중복 허용 X / 순서 X
# set() 함수 이용 
# {} 안에 원소를 콤마(,) 기준으로 구분하여 삽입

# 집합 자료형의 연산

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

# 합집합
print(a|b)
# 교집합
print(a&b)
# 차집합
print(a-b)

# 집합 관련 함수
data = set([1,2,3])

# 새로운 원소 추가
data.add(4)
# 새로운 원소 여러 개 추가
data.update([5,6])
# 특정 값 원소 삭제
data.remove(3)

# 사전 자료형과 집합 자료형은 순서가 없기 때문에 인덱싱 X



# 입력

# input() 한 줄의 문자열 입력
# map() 리스트의 모든 원소에 각각 특정한 함수를 적용


# 빠르게 입력 받기

# sys 라이브러리의 sys.stdin.readline() 메서드 이용
# - 입력 후 엔터가 줄 바꿈 기호로 입력 되므로 rstrip() 메서드 함께 사용


# f-string 

a=1
print(f'ㅂㅈㄷㄱ{a}ㅂㅈㄷㄱ')



# pass 아무것도 안할때 / 나중에 작성

# 조건문 간소화

# 조건문에서 실행될 코드가 한 줄인 경우 줄 바꿈 안해도 됨
score=85
if score >= 80: result = 'success'
else: result = 'fail'

# 조건부 표현식은 if ~ else 한줄에
result = 'success' if score >= 80 else 'fail' # if 앞에 쓰기

# x > 0 and x < 20 을 0<x<20 으로 사용가능 - python 에서만



# 함수와 람다 표현식


# 람다 표현식
# 함수를 간단하게 작성할 수 있다

c = (lambda a,b:a+b)(3,7)
print(c)

a=[('a',3),('b',2),('c',1)]
print(sorted(a, key=lambda x:x[1]))



# 라이브러리

# itertools - 반복되는 형태의 데이터를 처리 / 순열, 조합
# heapq - 힙(Heap) 자료구조 / 우선순위 큐
# bisect - 이진 탐색(Binary Search)
# collections = 덱(deque), 카운터(counter)
# math - 필수 수학 기능 / 팩토리얼, 제곱근, 최대공약수, 삼각함수, 파이

# eval()
a=eval('(3+5)*7') 
print(a) 

# sorted()


# 순열
from itertools import permutations
data = ['a','b','c']
result = list(permutations(data,3))
print(result)

# 조합
from itertools import combinations

# 중복 순열
from itertools import product

# 중복 조합
from itertools import combinations_with_replacement



# Counter
from collections import Counter

c = Counter(['r','b','r','g','b','b'])
print(c['b'])
print(c)
print(dict(c))



# 최대 공약수 / 최소공배수

import math

# 최소공배수
def lcm(a,b):
    return a*b//math.gcd(a,b)

print(math.gcd(21,14))
print(lcm(21,14))


    


