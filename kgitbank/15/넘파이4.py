import numpy as np

#range 함수 대응되는 np 함수
a=np.arange(1,11)
print(a)

print(a[0])
print(a[1])

print(a[0:5])
print(a[:5])
print(a[5:])
print(a[::-1])

#numpy는 [조건식] 조건식을 부여할 수 있다.

print([a>5]) #모든 요소에 대해서 하나하나 비교를 해서 true, false 집합을 출력한다

print(a[[1,3,4]])
print(a[[5,3,1,4,8]])

print(a[1::2])
print(a[::2])

print(a[a%2==0])
print(a[a%2==1])
