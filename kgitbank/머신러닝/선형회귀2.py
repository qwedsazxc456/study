import mglearn
import matplotlib.pyplot as plt 
from sklearn.datasets import load_boston

#회귀=평균값이 중요하다. 연속적인 값중에 하나를 맞춘다 
X,y = mglearn.datasets.make_wave(n_samples=60) #샘플 60개 달라고

print(X.shape)
print(X[:10, : ] )
print(y[:10])


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

#random_state=42  쓰고싶은거 마음대로 쓰면된다. 일관성만 있으면 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = KNeighborsRegressor(n_neighbors=1)
model.fit( X_train, y_train ) #학습
y_pred = model.predict(X_test)

for item in zip(y_pred, y_test):
    print(item)
#분류는 score 맞춘개수 , 회귀에서는 실제값와 잔차(오차)
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))





