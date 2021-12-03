import mglearn
import matplotlib.pyplot as plt
from numpy.lib.npyio import load 
from sklearn.datasets import load_boston

data = load_boston()
print( data.keys() )

X = data["data"]
y = data["target"]

print( X.shape)
print( y.shape)

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

#random_state=42  쓰고싶은거 마음대로 쓰면된다. 일관성만 있으면 
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

#최적화된 이웃을 찾아보자 - 지나치게 학습을 진해애서 딱 훈련데이터 셋에 맞춰 있ㄷ 
#적절한 이웃을 찾아보자 

trainList=[]
testList=[]
for n in range(1, 11):
    model = KNeighborsRegressor(n_neighbors = n )
    model.fit( X_train, y_train ) #학습
    trainList.append( model.score(X_train, y_train) )
    testList.append( model.score(X_test, y_test) )

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'
plt.plot(range(1, 11), trainList, label="훈련셋")
plt.plot(range(1, 11), testList, label="테스트셋")
plt.legend()
plt.show()

for score in zip(trainList, testList):
    print(score[0], score[1], score[0]-score[1])


model = KNeighborsRegressor(n_neighbors = 5 )
model.fit( X_train, y_train ) #학습
y_pred = model.predict(X_test)
for item in zip(y_pred, y_test):
    print(item)
#분류는 score 맞춘개수 , 회귀에서는 실제값와 잔차(오차)
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))




