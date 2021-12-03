import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x=[12,14,16,20,24,30,35,12,17,20,18,19,24,27,20,35,40]
y=[50,55,50,60,70,80,80,60,55,60,70,70,75,80,65,90,95]

#산포도
#데이터프레임 만들어서 산포도 그린다
#필드가 너무 많으면 시간이 오래 걸리니까 주요 요소만 그린다

plt.scatter(x,y)
plt.show()

#상관계수
print(np.corrcoef(x,y))
X=np.array(x)
y=np.array(y)

X=X.reshape(-1,1)
print(X.shape,y.shape)

#데이터 쪼개기
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, train_size=0.7)

#학습모델
model = LinearRegression()

model.fit(X_train, y_train) #학습

#예측
y_pred = model.predict(X_test)

print(y_pred)
print(y_test)

#평가
print( model.score(X_train, y_train))
print( model.score(X_test, y_test))
