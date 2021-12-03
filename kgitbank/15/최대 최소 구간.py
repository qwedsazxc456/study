import numpy as np
a=[170,178,180]
a=np.array(a)

#최대값이 있는 곳의 위치
print(a.max(),a.argmax())

#최소값
print(a.min(),a.argmin())

#구간나누기
a=np.linspace(0,1,50)
print(a)