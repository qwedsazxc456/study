import numpy as np 
import os 
import random 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing  import StandardScaler
import tensorflow as tf 

a = np.load("imagedata0.npz")
b = np.load("imagedata1.npz")

data1 = a["data"]
target1 = a["targets"]

data2 = b["data"]
target2 = b["targets"]

data = np.concatenate((data1, data2), axis=0)
print(data.shape)

target =np.concatenate((target1,target2), axis=0)
print(target.shape)




tf.random.set_seed(2) #시드고정하기 

X_train, X_test , y_train, y_test = train_test_split(data, target,random_state=0)

#2.딥러닝 모델을 만든다 
from tensorflow.keras import models 
from tensorflow.keras import layers 

#신경망 모델 만들기 
network = models.Sequential()
#층을 추가한다. - 입력층과 출력층 두개는 추가해야 한

#출력레이어 : 뉴런의 개수, 활성화함수 : softmax 를 쓴다 
#softmax 는 각 뉴런들의 출력값의 합이 1이 되도록 확률로 만들어 주는 일을 한다 

network.add( layers.Dense(64, activation="relu", input_shape=(150*150*3, )))
network.add( layers.Dense(64, activation="relu"))
network.add( layers.Dense(32, activation="relu"))
network.add( layers.Dense(2, activation="softmax")  )

network.compile( optimizer="sgd",  
                 loss="categorical_crossentropy",
                 metrics=['accuracy']) 



print( X_train.shape)
print( y_train.shape)

#X_train.shape[0]  데이터개수, 150, 150, => 2차원 

X_train = X_train.reshape( (X_train.shape[0], 150*150*3) ) #딥러닝은 2차원 데이터만 처리 가능 
X_test = X_test.reshape( (X_test.shape[0], 150*150*3) )

print( X_train.shape)
print( y_train.shape)

#스케일링 
X_train = X_train.astype('float32')/255
X_test = X_test.astype('float32')/255

#다중이미지분류 - 딥러닝은 반드시 원핫인코딩으로 해서 전달해야 한다 

from tensorflow.keras.utils import to_categorical #케라스가 제공하는 원핫인코딩 
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)



#학습시작 
hist =  network.fit (  
               X_train, 
               y_train, 
               epochs=10, #총 학습횟수 
               batch_size=100
         )

train_loss, train_acc = network.evaluate(X_train, y_train)
print("훈련셋 손실 {} 정확도 {}".format(train_loss, train_acc))
test_loss, test_acc = network.evaluate(X_test, y_test)
print("테스트셋 손실 {} 정확도 {}".format(test_loss, test_acc))



