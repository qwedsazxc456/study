
# numpy
# - numerical Python
# - 파이썬의 고성능 과학 계산용 패키지
# -Matrix와 vector와 같은 Array 연산의 표준
# - list에 비해 빠르고, 메모리 효율적
# - 반복문 없이 데이터 배열에 대한 처리를 지원함
# - c,c++,포트란 등의 언어와 통합 가능

import numpy as np 

test_array = np.array([1,4,5,8],float)
print(test_array)
print(type(test_array[3]))

# ndarray 객체
# numpy는 하나의 데이터 type

a = [1,2,3,4,5]
b = [5,4,3,2,1]

a = np.array(a, int)
print(a)

a = [1,2,3,4,5]
b = [5,4,3,2,1]
print(a[0] is b[-1]) # True

a = np.array(a)
b = np.array(b)
print(a[0] is b[-1]) # False

# shape: numpy array의 dimention
# dtype: numpy array의 type

# rank / name 
# 0    / scalar
# 1    / vector
# 2    / matrix
# 3    / 3-tensor

### ndim - 행의 개수??



# reshape
# - array의 shape의 크기를 변경, element의 갯수는 동일
# - (-1)의 값을 하면 알아서

test_matrix=[[1,2,3,4],[1,2,5,8]]
test_matrix= np.array(test_matrix).reshape(-1,2) # 할당 안하면 안바뀜
print(test_matrix)

# flatten
# 다차원 array를 1차원 array로 변환

test_matrix = [[1,2,3,4],[1,2,5,8],[1,2,3,4],[1,2,5,8]]
test_matrix = np.array(test_matrix).flatten()
print(test_matrix)
print(test_matrix.shape)



# indexing
# - [0,0] 표기법 제공 / row, column

test_example = np.array([[1,2,3],[4,5,6]],int)
print(test_example[0][2]) # 1행 3열 -> 3
print(test_example[0,2]) # 1행 3열 -> 3
test_example[0,0]=10
test_example[1,2]=5
print(test_example)

# slicing
# -list와 달리 행과 열 부분을 나눠서 slicing 가능
# -matrix의 부분 집합을 추출할 때 유용



# creation function

# arange
# - step에 float 가능

# zeros
# 0으로 가득찬 ndarray
# np.zeros(shape, dtype, order)

# ones

# empty
# - memory initialization 되지 않음

# someting_like
# 기존 ndarray의 shape 만큼 0,1 또는 empyt array 반환

test_matrix= np.arange(30).reshape(5,6)
test_matrix2=np.ones_like(test_matrix)
print(test_matrix2)

# identity
# -단위 행렬 생성

# eye
# 대각선이 1인 행렬, k값의 시작 index 변경 가능

print(np.eye(3,5,k=2))

# diag
# 대각 행렬의 값 추출
# np.diag(matrix, k=1) - k=start index

print(np.diag(test_matrix, k=-2)) # (-) 값도 가능 // ### 1행에서만 시작...?? 

# random
np.random.exponential(scale=2, size=100) 

# sum
test_array=np.arange(1,11)
test_array.sum()
# mean std

test_array.mean()
test_array.std()

# axis
# 기준이 되는 축

# concatenate
# - numpy array를 합치는 함수
# vstack / hstack
# np.concatenate / axis

# np.newaxis 새로운 축 추가



# numpy는 기본적인 연산가능
# *는 성분곱 - element-wise operation

# dot product 
# dot 사용

# transpose
# transpose 또는 T attribute사용

# broadcasting
# Scalar-vector 외에도 vector-matrix도 연산

### numpy 속도가 빠름??



# comparisons
a = np.arange(10)
print(a<4) # 모두 True/False나옴

# any 하나라도 조건에 만족하면 True
# all 모두 조건 만족하면 True

# element간 비교 boolean type

# logical_and / logical_not / logical_or



# np.where / np.isnan / np.isfinite

# np.argmax/ np.argmin 최대값 또는 최소값의 index 반환

# argsort - index를 알려준다

# boolean index
# 조건에 맞는거만

# fancy index
# index value로 사용해서 값 추출 / 반드시 integer로 선언
# matrix 형태도 가능

# i/o
# loadtxt / savetxt
# np.save / np.load 피클형태로 저장

