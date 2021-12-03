from numpy.lib.npyio import load
from sklearn.datasets import make_blobs
import mglearn 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

train_data=pd.read_csv('./dataset/타이타닉/train_data.csv')
test_data=pd.read_csv('./dataset/타이타닉/test_data.csv')

X=train_data.iloc[:,1:15]
y=train_data.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    stratify=y,
    random_state=0)

from sklearn.tree import DecisionTreeClassifier #Classifier 분류  Regression 회귀 
tree = DecisionTreeClassifier(random_state=0, max_depth=4)
tree.fit( X_train, y_train)

print("훈련셋 정확도 : ", tree.score(X_train, y_train))
print("테스트셋 정확도 : ", tree.score(X_test, y_test))

#각 특성(X)중에 중요도에 대한 정보를 갖고 있다 
print( tree.feature_importances_ )

def treeChart(model, feature_names):
    n_features = len(model.feature_importances_) #특성개수
    #수평막대그래프 
    #np.arange - range 함수처럼 일련번호를 만든다. 특성의 개수만큼 y축 값을 생성한다 
    plt.barh(np.arange( n_features), 
         #y축, arange함수-n값만큼 배열생성
        model.feature_importances_, #x축 
        align='center'
     )
    #눈금에 이름붙이기 
    plt.yticks(np.arange( n_features), feature_names)
    plt.ylim(-1, n_features) #눈금의 범위 
    plt.show()#화면에 출력

treeChart(tree, np.array(X.columns))
