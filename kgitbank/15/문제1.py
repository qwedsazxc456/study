import numpy as np

#문제1
a=[1,2,3,4,5]
b=[6,7,8,9,10]

a=np.array(a)
b=np.array(b)

print(a+b,a-b,a*b,a/b)

#문제2
a=[70,80,90,60,60,50,50,60,70,80,90,95,100,100,90,60,70]

a=np.array(a)
print(np.sum(a),np.mean(a),np.var(a),np.std(a))

#문제3
a=np.arange(1,11)
print(a)

#문제4
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a=np.array(a)
a1=a.reshape(4,5)
a2=a.reshape(5,4)
a3=a.reshape(2,10)
a4=a.reshape(10,2)

print(a1,a2,a3,a4)

#문제5
x=[1,2,3,4,5]
x=np.array(x)
y=2*x+1

print(y)

#문제6
print(np.random.randn(10))

#문제7
a=np.array([[4,2,3],[4,5,1]])
b=np.array([[1,2],[2,2],[2,1]])

print(a.dot(b))


