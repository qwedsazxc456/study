from numpy.lib.npyio import load
from sklearn.datasets import make_blobs
import mglearn 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 

#한글설정하기
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer['data'], cancer['target'],
    stratify=cancer['target'],
    random_state=0)

#DecisionTreeClassifier- 끝까지 가지치기를 하기 때문에 무조건 과대적합이 나타난다 
#트리를 끝까지 만들게 하면 무조건 모든데이터를 다 학습한다. 중간에 트리의 깊이를 제한해야 한다 
#max_depth 트리의 깊이ㅡㅜ
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

treeChart(tree, np.array(cancer['feature_names']))

#y  = a1x1 + a2x2 + a3x3 + .................... + b 


# 1 class1           문자열을 카테고리 타입으로 바꾼다. - one hot encoding   
# 2 class2
# 3 class3

#       p_class1   p_class2 p_class3
# 1      1           0        0
# 2      0           1        0 
# 3      0           0        1