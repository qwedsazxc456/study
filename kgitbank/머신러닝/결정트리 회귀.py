from sklearn.datasets import make_blobs
import mglearn 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 

#차트에 한글을 사용하려면 
import matplotlib
import matplotlib.font_manager as fm 

font_path = "c:/Windows/fonts/H2GSRB.TTF"
font_name = fm.FontProperties(fname=font_path).get_name()

matplotlib.rcParams['axes.unicode_minus']=False 
matplotlib.rc('font', family=font_name)

ram_prices = pd.read_csv("./data/ram_price.csv")

plt.yticks(fontname="Arial")
plt.semilogy( ram_prices.date, ram_prices.price)
plt.xlabel("년")
plt.ylabel("가격")
plt.show()

#시간에 따른 예측이 안된다. 
#결정트리회귀로 미래예측이 가능한가??
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

#2000년을 기점으로 데이터 나누기 
data_train = ram_prices[ ram_prices.date<2000]
data_test = ram_prices[ ram_prices.date>=2000]

#가격예측을 위해 날짜특성만(타겟이 가격이므로) 추출하기 
# 
X_train = data_train['date'] #결과가 날짜 1차원 ->2차원으로 변경하자
X_train = X_train[:, np.newaxis] #축 하나 추가하기 

print(X_train.shape)
print(X_train[:5])

#y_train 학습의 효과를 높이기 위해서 단위를 log화 시킨다 
y_train = np.log(data_train['price']) 


tree = DecisionTreeRegressor()
tree.fit(X_train, y_train)
print("중요도 ", tree.feature_importances_)

model = LinearRegression()
model.fit(X_train, y_train)

#전체 기간에 대해서 예측을 해보자 
X_all = ram_prices.date[:, np.newaxis]

pred_tree = tree.predict(X_all) #결정트리 예측값 
pred_model = model.predict(X_all) #선형회귀모델 예측값 

#스케일 원래대로 
price_tree = np.exp( pred_tree)
price_model = np.exp(pred_model)

plt.semilogy( data_train.date, data_train.price, label='훈련데이터')
plt.semilogy( data_test.date, data_test.price, label='테스트데이터')
plt.semilogy( X_all, price_tree, label='결정트리예측')
plt.semilogy( X_all, price_model, label='선형회귀예측')

plt.show()