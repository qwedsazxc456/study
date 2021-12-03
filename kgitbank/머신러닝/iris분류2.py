from sklearn import neighbors
from sklearn.datasets import load_iris
import pandas as pd 
import mglearn 
import matplotlib.pyplot as plt
iris = load_iris()

iris_df = pd.DataFrame(iris["data"], columns=iris.feature_names)

# # 데이터프레임을 사용해 y_train에 따라 색으로 구분된 산점도 행렬을 만듭니다.
# pd.plotting.scatter_matrix(iris_df, c=iris["target"], figsize=(15, 15), marker='o',
#                            hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
# plt.show()

#1. 데이터 분할 
from sklearn.model_selection import train_test_split 

X_train, X_test, y_train, y_test = train_test_split(
    iris["data"], iris["target"], random_state=0, train_size=0.7, stratify=iris.target)

#stratify=iris.target  데이터를 배분할때 타겟의 배분울 3:3:3 이거에 맞춰서 데이터를 분할한다 

from sklearn.neighbors import KNeighborsClassifier #분류는 Classifier 가 붙어있다 

#모델을 이웃의 숫자를 바꿔가면서 새로만들어서 평가를 저장했다가 저장값으로 차트를 그려보자 

trainList=[]
testList=[]
for i in range(1, 11):
    model = KNeighborsClassifier(n_neighbors=i) #이웃의 숫자를 1로 해서 , 적절한 이웃의 숫자를 지정해야 한다 
    #3.  학습을 한다 - 학습을 해서 특징들을 model객체에 저장한다 
    model.fit(X_train, y_train) #ndarray 앞에는 행렬, 뒤에는 벡터 
    trainList.append( model.score(X_train, y_train))
    testList.append(model.score(X_test, y_test))
    # print("이웃숫자 : ", i )
    # print("훈련셋", model.score(X_train, y_train))
    # print("테스트셋", model.score(X_test, y_test))

import matplotlib.pyplot as plt 

#한글 지정하기 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

#훈련셋
plt.plot(range(1,11), trainList, label="훈련정확도")
plt.plot(range(1,11), testList, label="평가정확도")
plt.xlabel("이웃수")
plt.ylabel("정확도")
plt.legend()
plt.show() 