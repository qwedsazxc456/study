from pandas.core.tools.datetimes import Scalar
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 
#한글설정하기
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(
    cancer["data"], cancer["target"], random_state=1)

print(X_train.shape)
print(X_test.shape)

#2차원의 ndarray 를 넘겨주고 컬럼명은  feature_names 특성의 이름 
data = pd.DataFrame(cancer["data"], columns=cancer["feature_names"])
#타겟필드 추가 
data["target"]= cancer["target"]
print(data.head())


#특성이 너무 많으면 산포도를 그리기가 어렵다 
# #3. 산포도 - 데이터가 너무 많아서 주석처리-_-
# sns.pairplot(data,
#     diag_kind='kde',  # 각 변수별 커널밀도추정곡선 / hist - 히스토그램
#     hue='target',     # 성별로 색깔을 다르게
#     palette='deep') #pastel,bright,deep,muted,colorblind,dark
# plt.show()

import numpy as np 
import mglearn 
#화면을 나눈다  15 by 2 
fig, axes = plt.subplots(15, 2, figsize=(10, 20))
#악성데이터 셋만 가져온다 
malignant = cancer.data[cancer.target == 0]
#양성 데이터셋만 가져온다 
benign = cancer.data[cancer.target == 1]

ax = axes.ravel() #쪼개진 면적에 대한 객체를 리스트형태로 가져온다 
print( ax )
for i in range(30):
    _, bins = np.histogram(cancer.data[:, i], bins=50) #구간 나누기 
    ax[i].hist(malignant[:, i], bins=bins, color=mglearn.cm3(0), alpha=.5)
    ax[i].hist(benign[:, i], bins=bins, color=mglearn.cm3(2), alpha=.5)
    ax[i].set_title(cancer.feature_names[i])
    ax[i].set_yticks(())
ax[0].set_xlabel("특성 크기")
ax[0].set_ylabel("빈도")
ax[0].legend(["악성", "양성"], loc="best")
fig.tight_layout() 
plt.show()

