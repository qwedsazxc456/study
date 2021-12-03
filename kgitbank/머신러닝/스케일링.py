from pandas.core.tools.datetimes import Scalar
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split 

cancer = load_breast_cancer()

X_train, X_test, y_train, y_test = train_test_split(
    cancer["data"], cancer["target"], random_state=1)

print(X_train.shape)
print(X_test.shape)

from sklearn.preprocessing import StandardScaler
#객체 만들고 
scalar = StandardScaler()
#학습을 한다 
scalar.fit(X_train)
X_train_scaled = scalar.transform(X_train)  #학습된 내용으로 데이터를 변환한다 
X_test_scaled = scalar.transform(X_test)  #학습된 내용으로 데이터를 변환한다

from sklearn.svm import SVC
svc = SVC() 
svc.fit(X_train, y_train)
print("스케일링전")
print("훈련셋", svc.score(X_train, y_train))
print("테스트셋", svc.score(X_test, y_test))

svc = SVC() 
svc.fit(X_train_scaled, y_train)
print("스케일링후")
print("훈련셋", svc.score(X_train_scaled, y_train))
print("테스트셋", svc.score(X_test_scaled, y_test))

print("------------- LogisticRegression --------------------")
from sklearn.linear_model import LogisticRegression
svc = LogisticRegression() 
svc.fit(X_train, y_train)
print("스케일링전")
print("훈련셋", svc.score(X_train, y_train))
print("테스트셋", svc.score(X_test, y_test))

svc = LogisticRegression() 
svc.fit(X_train_scaled, y_train)
print("스케일링후")
print("훈련셋", svc.score(X_train_scaled, y_train))
print("테스트셋", svc.score(X_test_scaled, y_test))

print("------------- RandomForestClassifier --------------------")
from sklearn.ensemble import RandomForestClassifier
svc = RandomForestClassifier(max_depth=3) 
svc.fit(X_train, y_train)
print("스케일링전")
print("훈련셋", svc.score(X_train, y_train))
print("테스트셋", svc.score(X_test, y_test))

svc = RandomForestClassifier(max_depth=3) 
svc.fit(X_train_scaled, y_train)
print("스케일링후")
print("훈련셋", svc.score(X_train_scaled, y_train))
print("테스트셋", svc.score(X_test_scaled, y_test))