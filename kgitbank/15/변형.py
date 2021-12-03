#배열의 차원을 전환할 수 있다
import numpy as np

a=np.arange(1,13)
print(a) #1~12 까지 1차원 배열

#reshape - 형태를 바꾸는 함수이다. 데이터 개수가 맞을때
#ex)12개 2*6 3*4 4*3 6*2 2*2*3 ...

print(a.reshape(3,4))
print(a.reshape(2,2,3))

#-1을 쓰는 경우가 있다. 행과 열 알아서 잡아준다
print(a.reshape(3,-1))
print(a.reshape(-1,3))

#1차원에 차원을 추가하기
print(a.reshape(-1,1))

