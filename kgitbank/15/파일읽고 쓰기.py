import numpy as np

a=[1,3,2,4,6,7,9,8,11,12]
np.save("datafile.npy",a) #무조건 확장자가 npy여야 한다
#binary 모드로 저장한다.

b=np.load("datafile.npy") #불러오기
print(b)

b=np.arange(1,101)
c=np.random.normal(1,10,10)

#확장자가 npz이어야 한다 dick형태 저장 키와값
np.savez("datafile.npz",key1=a,key2=b,key3=c)

result=np.load("datafile.npz")
print(result.files)

a1=result['key1']
a2=result['key2']
a3=result['key3']

print(a1,a2,a3)