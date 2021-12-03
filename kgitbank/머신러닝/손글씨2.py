import tensorflow as tf
fashion_mnist= tf.keras.datasets.fashion_mnist 

mnist = tf.keras.datasets.mnist

#tf.keras.datasets.mnist 이미지를 7만개를 손으로 쓴 이미지를 갖고 있다 
#애초에 머신러닝 - 미국애들이 주가 52 우편번호를 보고 분리를 해야한다 
#이미지를 읽어서 -> ndarray로 바꿔서 주었음  60000 개 28 by 28크기의 이미지
(X_train, y_train), (X_test, y_test) = mnist.load_data()

import matplotlib.pyplot as plt 
from PIL  import Image

def imageShow(image):
    plt.imshow(image, cmap= plt.cm.binary)
    plt.show()
    im = Image.fromarray(image)
    im.save("1.jpeg")

imageShow(X_train[1])


print(type(X_train))
print(type(y_train))

print(X_train.shape) # 60000 by 28 by 28  - 3차원 -> 2차원으로 바꿔야 reshape  
print(X_test.shape)

X_train = X_train.reshape(60000, 28 *28)
X_test = X_test.reshape(10000, 28 *28)

print(X_train.shape) # 60000 by 28 by 28  - 3차원 -> 2차원으로 바꿔야 reshape  
print(X_test.shape)

#X_train = X_train / 255.0
#X_test = X_test / 255.0

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=5, random_state=2)
model.fit(X_train, y_train) 

print("훈련셋 정확도 : ", model.score(X_train, y_train))
print("테스트셋 정확도 : ", model.score(X_test, y_test))

#로지스틱회귀분석 
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train) 

print("훈련셋 정확도 : ", model.score(X_train, y_train))
print("테스트셋 정확도 : ", model.score(X_test, y_test))


from sklearn.svm import SVC
svc = SVC()
svc.fit( X_train, y_train)
print('~~~ 서포트 벡터머신 ~~~')
print('훈련셋 : {:.3}'.format(svc.score(X_train, y_train)))
print('테스트셋 : {:.3}'.format(svc.score(X_test, y_test)))