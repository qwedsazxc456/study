"""
iris(붓꽃) -> setosa, virginica, vesicolor  세가지 종류 
우리 눈으로 보기에 모양이 서로 다르다 
sepal_length, sepal_width, petal_length, petal_width 이 요소 4가지면 구분할 수 있지 않을까란 가설을 세운다 

데이터를 수집했음 :   (특성-feature, 독립변수, class)
결과 : 꽃의 종류를 나누는거 (분류)-라벨, 종속변수, target
셋중에 하나 고르기 

분류는 결과값을 확률로 나타낸다. 
"""

from numpy.testing._private.utils import KnownFailureException
from scipy.sparse.construct import random
from sklearn.datasets import load_iris

iris = load_iris()
print( iris )
#키값들을 확인해보자 
print(iris.keys())

#dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])

print( iris['data']) #데이터 
print( iris['target']) #라벨, 결과, 꽃종류, 종속변수 
print( iris["target_names"] )
print( iris["feature_names"] ) #특성의 이름임 
print( iris["filename"] ) 

"""
1. 데이타를 분할한다 (7~3) (6~4) (8~2)
   학습을 제대로 했는지 평가를 해야 한다. 
   훈련데이터셋과 테스트데이터셋으로 나눈다 

2. 학습을한다. (머신러닝 알고리즘 중에 선택, K-이웃알고리즘)
   학습을 결과로 model을 준다 

3.  model에 테스트 셋을 넣고 평가를 한다 
"""
#1. 데이터 분할 
from sklearn.model_selection import train_test_split 

X_train, X_test, y_train, y_test = train_test_split(
    iris["data"], iris["target"], random_state=0, train_size=0.7
)

print( type(X_train) ) #ndarray
print( X_train.shape ) #(105, 4) 데이터가 105개이고 특정은 4개

print( type(X_test) ) #ndarray
print( X_test.shape ) #

print( type(y_train) ) #ndarray
print( y_train.shape ) #

print( type(y_train) ) #ndarray
print( y_train.shape ) #

"""
train_test_split  : 반환값이 4개임  훈련셋의 입력값, 테스트셋의 입력값, 훈련셋의 출력값, 테스트셋의 출력값
train_size=0.7 : 데이터 분할비율 지정
y = 2X + 1 

"""
print(X_train[:10])
print(X_test[:10])
print(y_train[:10])
print(y_test[:10])


#2단계 적절한 알고리즘을 선택해서 모델을 만든다 
#결과를 알경우 지도학습을 하고 지도학습  회귀외 분류 
#회귀는 결과값 하나로 맞출때(평균)을 중요시 할때, 분류는 둘중 하나 셋중하나 
#분류알고리즘들에는 Classifier 회귀는  Regressor 이다. 
from sklearn.neighbors import KNeighborsClassifier #분류는 Classifier 가 붙어있다 

model = KNeighborsClassifier(n_neighbors=1) #이웃의 숫자를 1로 해서 , 적절한 이웃의 숫자를 지정해야 한다 

#3.  학습을 한다 - 학습을 해서 특징들을 model객체에 저장한다 
model.fit(X_train, y_train) #ndarray 앞에는 행렬, 뒤에는 벡터 

#4. 학습 종료후 예측읗 해보자  predict 에 테스트셋을 던지면 테스트 데이터로 예측한 결과를 내보낸다. 
y_pred = model.predict(X_test)

#y_test - 관측값 또는 실제값 
#y_pred - 기대값 또는 예측값 

print( y_pred )
k=1
for item in zip(y_test, y_pred):
    print(iris["target_names"][item[0]], iris["target_names"][item[1]] )
    k=k+1
print(k)



