from sklearn.datasets import make_blobs
import mglearn 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from CommonUtil import outfliers_iqr
import matplotlib.pyplot as plt
import seaborn as sns

#한글설정하기
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'


#데이터 불러오기
gender = pd.read_csv('./gender_classification_v7.csv')
#데이터건수
print(gender.shape) #(5001, 8)
print(gender.keys()) 

# 1. 결측치제거
print(gender.isna().sum()) #결측치X

# 2. 박스플롯, 이상치
gender.boxplot()  # 결측치 long_hair만 있음
plt.show() 
from CommonUtil import outfliers_iqr
lower, upper = outfliers_iqr(gender['long_hair'])
print(lower,upper)
gender['long_hair'][gender['long_hair']<lower] = lower
gender['long_hair'][gender['long_hair']>upper] = upper 
gender.boxplot()
plt.show() 

# 3. 산포도 - 데이터가 너무 많아서 주석처리-_-
# sns.pairplot(gender,
#     diag_kind='kde',  # 각 변수별 커널밀도추정곡선 / hist - 히스토그램
#     hue='gender',     # 성별로 색깔을 다르게
#     palette='bright') #pastel,bright,deep,muted,colorblind,dark
# plt.show()

# 4. 상관계수
print('==상관계수==')
print(gender.corr())

# 5. 데이터 쪼개기
X = gender.iloc[:,0:6]
#print(X.head())
y = gender.iloc[:,7] # 구하려는 값 'gender'
#print(y.head())

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0)

# 6. 결정트리 -> 각 특성의 중요도
from sklearn.tree import DecisionTreeClassifier #Classifier-분류, Regression-회귀
tree = DecisionTreeClassifier(random_state=0,max_depth=4)
tree.fit(X_train,y_train)
#모든데이터를 끝까지 가기때문에 무조건 훈련셋은 100% ∴ max_depth=3 지정해주기
print('~~~ DecisionTreeClassifier 의사결정트리 ~~~')
print('훈련셋 : {:.3}'.format(tree.score(X_train, y_train)))
print('테스트셋 : {:.3}'.format(tree.score(X_test, y_test)))

def treeChart(model, feature_names):
    n_features = len(model.feature_importances_) #특성개수
    #수평막대그래프 
    #np.arange - range 함수처럼 일련번호를 만든다. 특성의 개수만큼 y축 값을 생성한다 
    plt.barh(np.arange( n_features),  #y축, arange함수-n값만큼 배열생성
        model.feature_importances_, #x축 
        align='center'
     )
    #눈금에 이름붙이기 
    plt.yticks(np.arange( n_features), feature_names)
    plt.ylim(-1, n_features) #눈금의 범위 
    plt.show()#화면에 출력

treeChart(tree, np.array(X_train.columns))

# 7. 로지스틱 분류
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(C=1)
model.fit(X_train, y_train)
print('~~~ 로지스틱회귀 ~~~')
print("훈련셋:{:.3}".format(model.score(X_train, y_train)))
print("테스트셋:{:.3}".format(model.score(X_test, y_test)))

# 8. 랜덤포레스트
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=5,random_state=2)
model.fit(X_train,y_train)    
print('~~~ 랜덤포레스트 random forest ~~~')
print('훈련셋 :{:.3}'.format(model.score(X_train, y_train)))
print('테스트셋{:.3}'.format(model.score(X_test, y_test)))

# 9. 그라디언트부스팅
from sklearn.ensemble import GradientBoostingClassifier
boost = GradientBoostingClassifier(n_estimators=5,random_state=0,learning_rate=0.01,max_depth=3)
boost.fit(X_train,y_train)    
print('~~~ 그라디언트 부스팅 ~~~')
print('훈련셋 : {:.3}'.format(boost.score(X_train, y_train)))
print('테스트셋 : {:.3}'.format(boost.score(X_test, y_test)))

# 10 xgb부스트
import xgboost as xgb
xgmodel = xgb.XGBClassifier(random_state=0,n_estimators=3,learning_rate=0.01,max_depth=5)
xgmodel.fit(X_train,y_train)    
print('~~~ XGboost ~~~')
print('훈련셋 : {:.3}'.format(xgmodel.score(X_train, y_train)))
print('테스트셋 : {:.3}'.format(xgmodel.score(X_test, y_test)))

#서포트 벡터 머신
from sklearn.svm import SVC
svc = SVC()
svc.fit(X_train,y_train)
print('~~~ 서포트 벡터 머신 ~~~')
print('훈련셋:{:.3}'.format(svc.score(X_train,y_train)))
print('테스트셋:{:.3}'.format(svc.score(X_test,y_test)))

