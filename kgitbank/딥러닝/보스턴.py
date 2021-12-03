#보스톤 집값 - 회귀분석
import tensorflow as tf 
from tensorflow.keras.datasets import boston_housing

(X_train, y_train), (X_test, y_test) = boston_housing.load_data()
print( X_train.shape)
print( y_train.shape)

#입력 - 2차원 ndarray, 라벨- 1차원 ndarray  
print( X_train[:10, :])
print( y_train[:10])


#딥러닝은 데이터 스케일링을 하지 = normalize(표준화)
mean = X_train.mean(axis=0) #행을 기준으로 평균을 구함 
X_train -= mean 
std = X_train.std(axis=0)
X_train /= std 

X_test -= mean 
X_test /=std 

from tensorflow.keras import models 
from tensorflow.keras import layers

def build_model():
    model = models.Sequential()
    #input_shape에 들어갈 값은 특성의 개수이다. X_train.shape[0] - 데이터 개수 
    #X_train.shape[1] - 특성의 개수(열의 수)
    model.add(layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
    model.add(layers.Dense(64, activation='relu')) #hidden layer - 깊이 학습 
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(1)) #회귀분석의 경우 출력층, activation="softmax" 가 빠짐 
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae']) #회귀분석일때 
    return model


model = build_model() 
model.fit(X_train, y_train)
print("훈련셋 {} ".format(model.evaluate(X_train, y_train) ))
print("테스트셋 {} ".format(model.evaluate(X_test, y_test) ))
