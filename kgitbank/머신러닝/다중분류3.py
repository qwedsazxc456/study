from sklearn.datasets import load_iris 
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

data = pd.read_csv("./diamonds (1).csv")
print( data.head() )

#산포도 그리기 
# sns.pairplot(data, 
#              diag_kind='kde',
#              hue="cut", 
#              palette='bright') # pastel, bright, deep, muted, colorblind, dark
# plt.show()

# #결측치 확인
print(data.isna().sum())

#결측치 삭제 
data = data.dropna(axis=0) #결측치를 포함하는 행삭제, axis=1 열삭제 
X = data.iloc[:, 1:]
print(X.head())
y = data.loc[:, "cut"]
print(y.head())

#이상치제거 
import CommonUtil 

for col in ["carat",  "depth",  "table",  "price",   "x",   "y"  ,"z"]:
    lower, upper = CommonUtil.outfliers_iqr(data[col])
    data[col][data[col]<lower] = lower 
    data[col][data[col]>upper] = upper 
    


#2.데이터 분리하기 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
#3.모델만들기 
model = LogisticRegression()
#4.학습
model.fit(X_train, y_train)
#5.평가 
print("훈련셋 {:.3}".format(model.score(X_train, y_train) ))
print("테스트셋 {:.3}".format(model.score(X_test, y_test) ))

#6.예측하기
# y_pred = model.predict( X_test )
# for item in zip(y_pred, y_test):
#     print(item)