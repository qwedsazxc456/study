import numpy as np

a=[1,2,3,4,5]
print(type(a),a)

b=np.array(a)
print(type(b),b)

a=[1,2,3,4,5]
b=[6,7,8,9,10]

a1=np.array(a)
b1=np.array(b)

c=a+b
c1=a1+b1

print(c)
print(c1)

print(c1.shape) #(5,) - tuple 타입이다

a=[1,2,3,4,5.5]
for i in a:
    print(type(i),i)
    
a1=np.array(a)
print(a1)
for i in a1:
    print(type(i),i)

