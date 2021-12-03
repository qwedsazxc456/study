import numpy as np

np.random.seed(123) #아무숫자나 쓰면 랜덤값이 고정 1~65535 사이
#랜덤하게 정수 발생
a = np.random.randint(1,10,5) # low, high, size

print(a)

#랜덤하게 실수 발생
a= np.random.rand(3,6,10)
print(a)

#정규분포
a=np.random.randn(10)

a=np.random.normal(170,20,10) #평균, 표준편차, 크기

print(a)

