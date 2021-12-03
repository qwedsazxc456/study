from numpy.lib.npyio import load
from scipy.sparse.construct import random
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris 
from sklearn.preprocessing  import StandardScaler
import tensorflow as tf 

tf.random.set_seed(2) #시드고정하기 

iris = load_iris()
X_train, X_test , y_train, y_test = train_test_split(iris['data'], iris['target'],random_state=0)

#2.딥러닝 모델을 만든다 
from tensorflow.keras import models 
from tensorflow.keras import layers 

#신경망 모델 만들기 
network = models.Sequential()
#층을 추가한다. - 입력층과 출력층 두개는 추가해야 한다 
network.add( layers.Dense(64, activation="relu", input_shape=(4, )))
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


#예측하기 
y_pred = network.predict(X_test)
print(y_pred[:10])

result = network.predict_classes(X_test)
print(result[:10])