import pandas as pd 
import mglearn
import os
import matplotlib.pyplot as plt
import numpy as np


# ## 데이터 표현과 특성 공학
# ### 범주형 변수
# #### 원-핫-인코딩 (가변수) - pandas가 지원하는 원핫인코딩

import os
# 이 파일은 열 이름을 나타내는 헤더가 없으므로 header=None으로 지정하고
# "names" 매개변수로 열 이름을 제공합니다
data = pd.read_csv(
    os.path.join(mglearn.datasets.DATA_PATH, "adult.data"), header=None, index_col=False,
    names=['age', 'workclass', 'fnlwgt', 'education',  'education-num',
           'marital-status', 'occupation', 'relationship', 'race', 'gender',
           'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
           'income'])
# 예제를 위해 몇개의 열만 선택합니다
data = data[['age', 'workclass', 'education', 'gender', 'hours-per-week',
             'occupation', 'income']]
print(data.head())

#범주형 자료 원핫인코딩
data=pd.get_dummies(data)
print(data.head())
print(data.columns)

from sklearn.linear_model import LogisticRegression

X=data.loc[:,'age':'occupation_ Transport-moving']
y=data.loc[:,'income_ >50K']

model=LogisticRegression()
model.fit(X,y)
print(model.score(X,y))