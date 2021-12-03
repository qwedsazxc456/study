from re import I
from sklearn.model_selection import train_test_split
import mglearn 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#한글설정하기
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

#1. 데이터를 mglearn 라이브러리로부터 가져온다 
# boston = mglearn.datasets.load_boston()
# print( type(boston ))  #sklearn.utils.Bunch != pandas 가 아니다. 
# print(boston.keys())
# print( boston["data"] )
# print( boston["target"] )
# print( boston["feature_names"])

#이 데이타셋을 만든 사람 의도
X, y = mglearn.datasets.load_extended_boston()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from sklearn.linear_model import LinearRegression
model = LinearRegression() #모델을 만든다 
model.fit(X_train, y_train) 
#fit 함수를 호출해서 학습을 하고나면 학습의 결과값인 알고리즘은 모델안에 저장되어 있다 
print("LinearReguration-----------------")
print("훈련셋:", model.score(X_train, y_train))
print("테스트셋:", model.score(X_test, y_test))
#print("기울기 : ", model.coef_)
print("절편 : ", model.intercept_)

#훈련셋: 0.9520519609032729
#테스트셋: 0.6074721959665852

#훈련셋: 0.941368878146875
#테스트셋: 0.8474325481954188

#현재 학습이 지나치게 많이 된 상황이다. 

#결론 : LinearRegression 모델 자체에 뭔가 파라미터가 없다. 대신에 Ridge, Lasso알고리즘이 나온다 

#선형회귀모델은 y = ax + b의 꼴로 a와 b를 구한다. a와 b값을 랜덤하게 놓고 반복적으로 오차를 줄여가면서 구한다 
#Ridge 와  Lasso는 기울기인 a에 제약을 가해서 가급적 0에 가깝게 만들자 
#Ridge는 기울기 a를 최대한 0에 가깝게 
#Lasso 요소중에 필요없다고 생각하면 데이터 특성을 없애기도 한다. 분석을 데이터(X 의 열의 개수 - 특성)

#------------------- Ridge 학습하기 ---------------------------
from sklearn.linear_model import Ridge 
ridge = Ridge(alpha=1) #Ridge  모델을 만들때 alpha 라는 값이 있다. 값을 안주면 1이다. 
ridge.fit(X_train, y_train)
print("Ridge  1 -----------------")
print("훈련셋:", ridge.score(X_train, y_train))
print("테스트셋:", ridge.score(X_test, y_test))
#print("기울기 : ", ridge.coef_)
print("절편 : ", ridge.intercept_)
#과대 적합이 많이 준다 

ridge = Ridge(alpha=10) #Ridge  모델을 만들때 alpha 라는 값이 있다. 값을 안주면 1이다. 
ridge.fit(X_train, y_train)
print("Ridge  10 -----------------")
print("훈련셋:", ridge.score(X_train, y_train))
print("테스트셋:", ridge.score(X_test, y_test))
#print("기울기 : ", ridge.coef_)
print("절편 : ", ridge.intercept_)
#과대 적합이 많이 준다 

##### -------------   xgboost 알고리즘 사용하기 
import xgboost as xgb 
xgbmodel = xgb.XGBRegressor(random_state=0, n_estimators=3, max_depth=5, learning_rate=0.01)
xgbmodel.fit(X_train, y_train)
print("훈련셋:", xgbmodel.score(X_train, y_train))
print("테스트셋:", xgbmodel.score(X_test, y_test))


#LogisticRegression
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

for C in [1, 10, 100, 0.1, 0.001]:
    model = LogisticRegression(C=C)
    model.fit(X_train, y_train)

    #선형회귀모델 - 모든 데이터들을 X와 y와의 관계로 봐서 y 에 이르는 X에 대한 기울기와 절편을 얻어내는 모델이다 
    #분류-로지스틱 회귀-선형회귀모델(Ridge, Lasso 개선판) , 처음 초창기 알고리즘 
    print(f"로지스틱 {C}-----------------")
    print("훈련셋 : ", model.score(X_train, y_train))
    print("테스트셋 : ", model.score(X_test, y_test))

    print(f"서포트 벡터 머신 {C} -----------------")
    svc = LinearSVC(C=C)
    svc.fit(X_train, y_train)
    print("훈련셋 : ", svc.score(X_train, y_train))
    print("테스트셋 : ", svc.score(X_test, y_test))