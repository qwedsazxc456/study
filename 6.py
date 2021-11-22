# pandas
# panel data

# 열 - attribute, field, feature, column
# 행 - instance, tuple, row

import pandas as pd

df_data=pd.read_csv() # 불러오기

df_data.head() # 위에서 5개

# series
# 한줄 Series 전체 DataFrame
# comlumn vector를 표현하는 object

list_data = [1,2,3,4,5]
list_name = ['a','b','c','d','e']
example_obj = pd.Series(data = list_data, index=list_name)
print(example_obj)
# index 문자로 가능
# Subclass of numpy.ndarray

import numpy as np

dict_data={'a':1,'b':2, 'c':3, 'd':4 ,'e':5}
example_obj = pd.Series(dict_data, dtype=np.float32, name='example_data')
print(example_obj)

print(example_obj.index)
print(example_obj.values)
print(example_obj['a'])
example_obj=example_obj.astype(int)
print(example_obj)

# index 값을 기준으로 series 생성 / 값 없으면 NaN값



# dataframe

# 열마다 타입이 다를 수 있다
# 열도 index중심 없으면 NaN값
# 열 접근은 . 이나 [] 사용

# loc는 index 이름 , iloc는 index number
# T 전치, values 값들, to_csv csv형식으로

# column 삭제
# del df[]
# df.drop('열 이름',aixs=1)



# selection with column names
# T로 데이터를 옆으로 보면 편하다
# boolean index 가능

# df.index 
# df.reset_index(drop=True) - 기존 index 지우고 새로
# df.reset_index(inplace=True, drop=True)

# 지우려면 df.drop('', aixs=1) - column 지운다
# inplace 안하면 데이터가 변하지는 않는다

# index 기준으로 연산 / 겹치는 index가 없을경우 NaN값

# fill_value=0 없는값은 0으로 해서 NaN값 없게



# pandas built-in function

# describe() 데이터 요약정보
# unique() 유일한 값을 list 반환
# sum(axis=)
# isnull() True/False 반환
# df.isnull().sum()

# corr() 모든 상관관계



# groupby
# df.groupby('column')['적용받는 컬럼'].sum()
# df.groupby(['',''])[].sum() # 컬럼 여러개 가능

# Hierarchical index
# index 여러개 만들어진다

# unstack - matrix로 만들어준다 / stack
# reset_index()

# swaplevel() - column 순서 바꾼다

# grouped - 튜플형태로 
# get_group 으로 가져온다

# aggratation
# agg 로 grouped된 상태에서 column별로 - 한줄씩 X / column별로

# groupby-filter

### groupby filter R에서 쓰는것과 비슷하게??? 
