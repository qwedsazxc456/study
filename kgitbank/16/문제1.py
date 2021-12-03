import numpy as np
a=np.zeros((3,4)) #변수가 tuple타입이라 괄호가 필요하다

print(a)
print(a.shape[0])
print(a.shape[1])

row, col=a.shape
for i in range(0,row):
    for j in range(0,col):
        a[i][j]=np.random.randint(1,10)
        
#행출력
print(a[0])
print(a[1])
print(a[2])

#열출력
print(a[:,0])
print(a[:,1])
print(a[:,2])
print(a[:,3])

#행의 누적합계 구하기
#매개변수 - 축 1차원 배열, 2차원 배열
print(np.array([1,2,3,4,5]).cumsum(axis=0))
print(a.cumsum(axis=0))

#열의 누적합계
print(a.cumsum(axis=1))

#a를 파일로 저장하기
np.save("a.npy",a)

#load-읽어오기
b=np.load("a.npy")
print(b)