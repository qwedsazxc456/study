from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier

cancer = load_breast_cancer()
print(cancer.keys())
print("특성의 이름")
print(cancer["feature_names"])
print("타켓 이름")
print(cancer["target_names"])

print("전체데이터개수 ")
print(cancer["data"].shape)

#1. 데이터 나누기 6:4로 나눠보자 

X_train, X_test, y_train, y_test = train_test_split(
    cancer["data"], cancer["target"], train_size=0.6, random_state=0
)

print(X_train.shape)
print(X_test.shape)


#2. 모델 만들기 
model = KNeighborsClassifier(n_neighbors=3) #n_neighbors 이 값을 1~10까지 가면서 적절한 이웃의 숫자를 찾는다 
                                            #3 쓴이유 - 강사마음 

#3.학습
model.fit(X_train, y_train)

#4.예측하기 
y_pred = model.predict(X_test)

cnt=0
for item in zip(y_pred, y_test):
    if item[0] == item[1]:
        cnt+=1 
print("전체 개수 : ", len(y_pred))
print("일치개수 : ", cnt)
print("적중률 : ", cnt/len(y_pred))

