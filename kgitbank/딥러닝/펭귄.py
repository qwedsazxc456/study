from numpy.lib.npyio import load
from scipy.sparse.construct import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing  import StandardScaler
import tensorflow as tf 
import pandas as pd 

tf.random.set_seed(2) #시드고정하기 

data = pd.read_csv("./penguins.csv")
print( data.head() )

#결측치 없애기 
print( data.isna().sum() )
data = data.dropna(axis=0)
print( data.isna().sum() )

X = data.iloc[:, 2:6]
y = data.iloc[:, 0]
print(X.iloc[:10, :])
print(y[:10]) 
print(y.value_counts())

X = pd.get_dummies(X) #전체필드를 원핫인코딩 해준다. 숫자를 문자로 바꾸어서 한번에 해야 한다 
print(X.iloc[:10, :])

X_train, X_test , y_train, y_test = train_test_split(X, y, random_state=0)

#2.딥러닝 모델을 만든다 
from tensorflow.keras import models 
from tensorflow.keras import layers 

#신경망 모델 만들기 
network = models.Sequential()
#층을 추가한다. - 입력층과 출력층 두개는 추가해야 한다 

network.add( layers.Dense(16, activation="relu", input_shape=(4, )))
#새로운 hidden층을 추가해본다 
network.add( layers.Dense(16, activation="relu")) #히든층의 경우에는 input_shape 속성이 없다 
network.add( layers.Dense(3, activation="softmax")  )

network.compile( optimizer="sgd",  
                 loss="categorical_crossentropy",
                 metrics=['accuracy']) 


#입력데이터 스케일링
scalar = StandardScaler()
#학습을 한다 
scalar.fit(X_train)
X_train = scalar.transform(X_train)  #학습된 내용으로 데이터를 변환한다 
X_test = scalar.transform(X_test)  #학습된 내용으로 데이터를 변환한다 

# #다중이미지분류 - 딥러닝은 반드시 원핫인코딩으로 해서 전달해야 한다 

from tensorflow.keras.utils import to_categorical #케라스가 제공하는 원핫인코딩 
#문자열로 전달된 데이터는 원핫인코딩 못함 
y_train = pd.get_dummies(y_train)
y_test = pd.get_dummies(y_test)
print( y_train[:10] )

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


#예측하기 
y_pred = network.predict(X_test)
print(y_pred[:10])

# result = network.predict_classes(X_test)
# print(result[:10])
import numpy as np 
y_pred=np.argmax(y_pred, axis=1)  #np.argmax  [0.21312772 0.26518998 0.5216823 ] 젤 큰값이 있는곳을 반환

target_names=y.unique()
for i in range(20):
    print(target_names[y_pred[i]])