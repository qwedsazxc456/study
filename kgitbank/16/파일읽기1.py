import numpy as np
f=open("C:/Users/Administrator/Desktop/python/16/height.txt",'r')
lines=f.readlines()

alist=[]
for line in lines:
    alist.append(float(line.replace("\n","").replace(",","")))

a=np.array(alist)
print(np.sum(a))
print(np.mean(a))
print(np.median(a))
print(np.var(a))
print(np.std(a))
print(np.max(a))
print(np.min(a))
print(np.argmax(a))
print(np.argmin(a))
