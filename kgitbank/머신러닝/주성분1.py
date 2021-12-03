from pandas.core.tools.datetimes import Scalar
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
from sklearn.preprocessing import StandardScaler

#한글설정하기
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

cancer = load_breast_cancer()
X = cancer["data"]
y = cancer["target"]

ss = StandardScaler()
ss.fit(X)
X_scaled = ss.transform(X)

#주성분 분석 - 나머지 특성을 축소시켜 버린다. 
from sklearn.decomposition import PCA
# 데이터의 처음 두 개 주성분만 유지시킵니다
pca = PCA(n_components=2)  #원하는 만큼 주성분을 유지한다 
#주성분이라 함은 그 방향으로 데이터들의 분산이 가장 큰 방향벡터를 의미
#유방암 데이터로 PCA 모델을 만듭니다 - 30개의 특성중 중요한 성분의 두 데이터만 
pca.fit(X_scaled)

#주성분으로 차원을 축소시킨다 
X_pca = pca.transform(X_scaled)
print("원본 데이터 형태:", str(X_scaled.shape)) #30 -> 2
print("축소된 데이터 형태:", str(X_pca.shape))

print("주성분", pca.components_)

#히트맵 
plt.matshow(pca.components_, cmap='viridis')
plt.yticks([0, 1], ["첫 번째 주성분", "두 번째 주성분"])
plt.colorbar()
plt.xticks(range(len(cancer.feature_names)),
           cancer.feature_names, rotation=60, ha='left')
plt.xlabel("특성")
plt.ylabel("주성분")
plt.show() 

#PCA 를 이용해서 특성이 30 -> 2 개로 축소 
from sklearn.neighbors import KNeighborsClassifier
print("X_train_pca.shape:", X_pca.shape)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_pca, y)
print("주성분 세트 정확도: {:.2f}".format(knn.score(X_pca, y)))
 
from sklearn.neighbors import KNeighborsClassifier
print("X.shape:", X.shape)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
print("모든 특성 다 사용한  세트 정확도: {:.2f}".format(knn.score(X, y)))








