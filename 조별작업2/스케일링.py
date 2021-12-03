import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf 


tf.random.set_seed(2)

train_data = pd.read_csv('./data_for_train_PCA.csv')
test_data = pd.read_csv('./data_for_test_refine_PCA.csv')


X_train = train_data[['learning_level2', 'diff2']]
y_train = train_data['answered_correctly']

X_test = test_data[['learning_level2', 'diff2']]
y_test = test_data['answered_correctly']

from tensorflow.keras import models 
from tensorflow.keras import layers 

#신경망 모델 만들기 
network = models.Sequential()
network.add( layers.Dense(64, activation="relu", input_shape=(2, )))
network.add( layers.Dense(128, activation="relu"))
network.add( layers.Dense(32, activation="relu"))
network.add( layers.Dense(16, activation="relu"))
network.add( layers.Dense(1, activation="sigmoid")  )

network.compile( optimizer="sgd",  
                 loss="binary_crossentropy",
                 metrics=['accuracy']) 


from sklearn.preprocessing  import StandardScaler

# scalar = StandardScaler()
# #학습을 한다 
# scalar.fit(X_train)
# X_train = scalar.transform(X_train)  #학습된 내용으로 데이터를 변환한다 
# X_test = scalar.transform(X_test)  #학습된 내용으로 데이터를 변환한다 


# from tensorflow.keras.utils import to_categorical
# y_train = to_categorical(y_train)
# y_test = to_categorical(y_test)


# 학습시작 
hist =  network.fit (  
               X_train, 
               y_train, 
               epochs=1000, #총 학습횟수 
               batch_size=100
         )

train_loss, train_acc = network.evaluate(X_train, y_train)
print("훈련셋 손실 {} 정확도 {}".format(train_loss, train_acc))
test_loss, test_acc = network.evaluate(X_test, y_test)
print("테스트셋 손실 {} 정확도 {}".format(test_loss, test_acc))

pred = network.predict(X_test)
df = pd.DataFrame(pred)

df.to_csv('pred.csv', index=False)
# def changeData(pred):
#     for i in range(len(pred)):
#         if pred[i] < 0.5:
#             pred[i] = 0
#         else:
#             pred[i] = 1
#     return pred

# pred = changeData(pred)
# count = 0
# for i in range(len(y_test)):
#     if pred[i] == y_test[i]:
#         count += 1
# print(count / len(y_test))

