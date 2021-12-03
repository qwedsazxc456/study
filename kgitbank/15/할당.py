import numpy as np
a=np.zeros(10) #크기 10개의 배열을 만들어서 0으로 채워준다
print(a)

a=np.zeros((4,5)) #tuple로 전달해야 한다

a=np.zeros((3,4,5)) #tuple로 전달해야 한다

print(a)
print(a.shape)

#1로 채우기
a=np.ones((3,4))
print(a)

