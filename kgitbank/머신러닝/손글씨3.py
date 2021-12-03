import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
fashion_mnist= tf.keras.datasets.fashion_mnist 

mnist = tf.keras.datasets.mnist

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(type(X_train))
print(type(y_train))

print(X_train.shape) # 60000 by 28 by 28  - 3차원 -> 2차원으로 바꿔야 reshape  
print(X_test.shape)

X_train = X_train.reshape(60000, 28 *28)
X_test = X_test.reshape(10000, 28 *28)

print(X_train.shape) # 60000 by 28 by 28  - 3차원 -> 2차원으로 바꿔야 reshape  
print(X_test.shape)

#이미지 색상 0~ 255 /255  -> 0 ~1 사이에 머무른다. 
X_train = X_train / 255.0
X_test = X_test / 255.0

pca = PCA(n_components=50, random_state=0).fit(X_train)
X_train = pca.transform(X_train)
X_test = pca.transform(X_test)

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