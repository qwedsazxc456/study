import numpy as np 
import pandas as pd  #판다스

iris = pd.read_csv("./iris.csv")

print(iris)

print( iris.isna() ) #결측치가 있는지 확인해본다 

print( iris.isna().sum() ) #결측치 카운트 하기  

#결측치 제거하기 
iris2 = iris.dropna(axis=0, how="any") #행의 필드중에 NaN이 하나라도 있으면 데이터 삭제 
print( iris2.isna().sum() ) 
print( iris2.shape )

#삭제대신에 평균값으로 채우길 원한다. fillna
iris["sepal.length"].fillna( iris["sepal.length"].mean(), inplace=True)
iris["sepal.width"].fillna( iris["sepal.width"].mean(), inplace=True)
iris["petal.length"].fillna( iris["petal.length"].mean(), inplace=True)

print( iris.isna().sum() ) 
print( iris.shape )

#boxplot 을 그리자 
import matplotlib.pyplot as plt 

iris.boxplot()
plt.show()

from CommonUtil import outfliers_iqr 
for id in ["sepal.length", "sepal.width", "petal.length", "petal.width"]:
    lower, upper = outfliers_iqr(iris[id])
    iris[id][iris[id]<lower ] = lower 
    iris[id][iris[id]>upper ] = upper 

iris.boxplot()
plt.show()