#PCA - 고차원 데이터 셋의 시각화 - 암환자 산포도 그리려면 32 by 32 개의 차트를 그려야 한다 
#악성과 양성의 두 클래스에 대한 각각의 히스토그램을 그려보자
from sklearn.datasets import make_blobs
import mglearn
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split 
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#한글 지정하기 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'


from sklearn.datasets import load_digits
iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split( 
    iris["data"], iris["target"], random_state=0)

from sklearn.cluster import KMeans 

kmeans = KMeans(n_clusters=3)
kmeans.fit(X_train)
print(kmeans.labels_)
print(y_train)

print(kmeans.predict(X_test))
