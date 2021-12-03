import pandas as pd
from matplotlib import pyplot as plt , font_manager as fm , rc
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier


#데이터 불러오기
accident=pd.read_csv('./car_accident.csv')

#이상치제거
accident = accident.drop(accident['부상자수'][accident['부상자수'] >= 9].index)
accident = accident.drop(accident['사망자수'][accident['사망자수'] >= 3].index)
accident = accident.drop(accident['중상자수'][accident['중상자수'] >= 5].index)
accident = accident.drop(accident['경상자수'][accident['경상자수'] >= 5].index)
accident = accident.drop(accident['부상신고자수'][accident['부상신고자수'] >= 2].index)

#x,y설정
X=accident.drop(['사고년도', '발생월일시','사망자수', '부상자수', '중상자수',
           '경상자수', '부상신고자수', '발생위치X좌표', '발생위치Y좌표',
           '경도좌표', '위도좌표', '발생위치시군구', '발생위치시도'], axis=1)
X=pd.get_dummies(X)
y=accident.loc[:,'부상자수']

#---KNeighborsClassifier n_neighbors값 1부터 10까지 바꿔서 그래프그리기---


# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, train_size=0.75, random_state=0)
  
# trainScores = []
# testScores = []
# for i in range(1,11):
#     model = KNeighborsClassifier(n_neighbors=i)
#     model.fit(X_train, y_train)

#     print(f'----- KNeighborsClassifier n_neighbors={i} -----')
#     trainScore = model.score(X_train, y_train)
#     testScore = model.score(X_test, y_test)
#     trainScores.append(trainScore)
#     testScores.append(testScore)
#     print('훈련셋', trainScore)
#     print('테스트셋', testScore)
# plt.plot(range(1,11), trainScores, color='lightseagreen', label='train')
# plt.plot(range(1,11), testScores, color='aquamarine', label='test')
# plt.xlabel('n_neighbors')
# plt.legend()
# plt.xlim([1, 10])
# plt.xticks(range(1,11))
# plt.title('KNeighborsClassifier')
# plt.show()

#--------kneighbor 따로---------


# y=accident.loc[:,'부상자수']
# y2=accident.loc[:,'사망자수']
# y3=accident.loc[:,'중상자수']
# y4=accident.loc[:,'경상자수']
# y5=accident.loc[:,'부상신고자수']

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, train_size=0.75, random_state=0)
# X2_train, X2_test, y2_train, y2_test = train_test_split(
#     X, y2, train_size=0.75, random_state=0)
# X3_train, X3_test, y3_train, y3_test = train_test_split(
#     X, y3, train_size=0.75, random_state=0)
# X4_train, X4_test, y4_train, y4_test = train_test_split(
#     X, y4, train_size=0.75, random_state=0)
# X5_train, X5_test, y5_train, y5_test = train_test_split(
#     X, y5, train_size=0.75, random_state=0)

# model = KNeighborsClassifier()
# model.fit(X_train,y_train)
# pred_y=model.predict(X_test)
# model.fit(X2_train,y2_train)
# pred_y2=model.predict(X2_test)
# model.fit(X3_train,y3_train)
# pred_y3=model.predict(X3_test)
# model.fit(X4_train,y4_train)
# pred_y4=model.predict(X4_test)
# model.fit(X5_train,y5_train)
# pred_y5=model.predict(X5_test)


# unique,counts=np.unique(np.logical_and(np.logical_and(np.logical_and(np.logical_and(y_test==pred_y, y2_test==pred_y2),y3_test==pred_y3),y4_test==pred_y4),y5_test==pred_y5)
#                          ,return_counts=True)

# print(unique)
# print(counts[1]/y_test.shape[0])


#----------결정트리 그래프-----------

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, train_size=0.75, random_state=0)
  
# trainScores = []
# testScores = []
# for i in range(1,11):
#     model = DecisionTreeClassifier(max_depth=i ,random_state=0)
#     model.fit(X_train, y_train)

#     print(f'----- DecisionTreeClassifier max_depth={i} -----')
#     trainScore = model.score(X_train, y_train)
#     testScore = model.score(X_test, y_test)
#     trainScores.append(trainScore)
#     testScores.append(testScore)
#     print('훈련셋', trainScore)
#     print('테스트셋', testScore)
# plt.plot(range(1,11), trainScores, color='lightseagreen', label='train')
# plt.plot(range(1,11), testScores, color='aquamarine', label='test')
# plt.xlabel('max_depth')
# plt.legend()
# plt.xlim([1, 10])
# plt.xticks(range(1,11))
# plt.title('DecisionTreeClassifier')
# plt.show()

#------------xgboost 따로----------



# y=accident.loc[:,'부상자수']
# y2=accident.loc[:,'사망자수']
# y3=accident.loc[:,'중상자수']
# y4=accident.loc[:,'경상자수']
# y5=accident.loc[:,'부상신고자수']

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, train_size=0.75, random_state=0)
# X2_train, X2_test, y2_train, y2_test = train_test_split(
#     X, y2, train_size=0.75, random_state=0)
# X3_train, X3_test, y3_train, y3_test = train_test_split(
#     X, y3, train_size=0.75, random_state=0)
# X4_train, X4_test, y4_train, y4_test = train_test_split(
#     X, y4, train_size=0.75, random_state=0)
# X5_train, X5_test, y5_train, y5_test = train_test_split(
#     X, y5, train_size=0.75, random_state=0)


# model = XGBClassifier(num_class=2)
# model.fit(X_train,y_train)
# pred_y=model.predict(X_test)
# model.fit(X2_train,y2_train)
# pred_y2=model.predict(X2_test)
# model.fit(X3_train,y3_train)
# pred_y3=model.predict(X3_test)
# model.fit(X4_train,y4_train)
# pred_y4=model.predict(X4_test)
# model.fit(X5_train,y5_train)
# pred_y5=model.predict(X5_test)

# unique,counts=np.unique(np.logical_and(np.logical_and(np.logical_and(np.logical_and(y_test==pred_y, y2_test==pred_y2),y3_test==pred_y3),y4_test==pred_y4),y5_test==pred_y5)
#                          ,return_counts=True)

# print(unique)
# print(counts[1]/y_test.shape[0])


#-------------------randomforest 그래프------

# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, train_size=0.75, random_state=0)

# trainScores = []
# testScores = []
# for i in range(5,16):
#     model = RandomForestClassifier(random_state=0, max_depth=i)
#     model.fit(X_train, y_train)

#     print(f'----- 랜덤포레스트 max_depth={i} -----')
#     trainScore = model.score(X_train, y_train)
#     testScore = model.score(X_test, y_test)
#     trainScores.append(trainScore)
#     testScores.append(testScore)
#     print('훈련셋', trainScore)
#     print('테스트셋', testScore)
# plt.plot(range(5,16), trainScores, color='lightseagreen', label='train')
# plt.plot(range(5,16), testScores, color='aquamarine', label='test')
# plt.xlabel('max_depth')
# plt.legend()
# plt.xlim([5,15])
# plt.xticks(range(5,16))
# plt.title('RandomForestClassifier')
# plt.show()

#------------특성중요도------------

# def treeChart(model, feature_names):
#     n_features = len(model.feature_importances_)    # 특성 개수
#     # 수평막대그래프
#     # np.arange - range 함수처럼 일련번호를 만든다. 특성의 개수만큼 y축 값을 생성한다
#     plt.barh(np.arange(n_features),
#             # y축, arange함수 - n값만큼 배열 생성
#             model.feature_importances_, # x축
#             align='center', color='lightseagreen')
#     # 눈금에 이름 붙이기
#     plt.yticks(np.arange(n_features), feature_names)
#     plt.ylim(-1, n_features)    # 눈금의 범위
#     plt.show()

# treeChart(model, np.array(X.columns))
