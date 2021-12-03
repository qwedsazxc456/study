import numpy as np

a=[54,66,70,100,90,40,33,34,55]

#평균구하기
a=np.array(a)
print("평균:",np.mean(a))

b=[60,70,50,65,55,72,60,61,70]

b=np.array(b)
print("평균:",np.average(b))

print('중간값',np.median(a))
print('중간값',np.median(b))

#히스토그램
#import matplotlib.pyplot as plt

#plt.hist(a)
#plt.show()

a1=a-np.mean(a)
print(a1) 

print(int(int(np.sum(a1))))

#분산
a1=np.sum((a-np.mean(a))**2)/a.shape[0]
print(a1)

print(np.var(a)) 
print(np.var(b))

#표준편차
print(np.std(a))
print(np.std(b))