# # 4의 배수이면서 100의 배수는 안되고 400의 배수는 윤년이다 - 규칙 
# year = int(input("년도 : "))

# if year%4==0 and year%100!=0 or year%400==0:
#     print("윤년")
# else:
#     print("윤년이 아니다")

def isLeap(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return 1
    else:
        return 0
#머신러닝 학습할 자료를 만들어줘야 한다. 2000년치 부분을 만들고 , 결과는 각 연도마다 윤년인지 아닌지 
#우리가 넣어야 한다 [1,2,3,4,5,6,7,8,....  ] [0,0,0,1,]

input_data = []
output_data=[]
for i in range(1,2001):
    input_data.append(i)
    output_data.append(isLeap(i))

print(input_data[:20])
print(output_data[:20])

#머신러닝은  numpy 타입어어야 한다 - 머신러닝 라이브러리 내부구조가 다 c언어이다. 
#c언어가 속도가 빠르다. 파이썬 -> numpy나 pandas로 바꾸어야 머신러닝이나 딥러닝에서 사용이 가능하다 
#머신러닝이 입력데이터는 2차원이어야 하고, 결과데이터는 1차원이어야 한다 
import numpy as np 
input_data = np.array(input_data)
output_data = np.array(output_data)

#입력데이터는 언제나 2차원 구조로 바꿔야한다. (1->2, 3->2, 4->2) reshape
input_data =input_data.reshape(-1, 1) 
print(input_data[:20] )  # [] - 1차원  [ [ ]] - 2차원 

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier

X_train, X_test, y_train, y_test = train_test_split(
    input_data, output_data, train_size=0.6, random_state=0
)

print(X_train.shape)
print(X_test.shape)


#2. 모델 만들기 
model = KNeighborsClassifier(n_neighbors=1) #n_neighbors 이 값을 1~10까지 가면서 적절한 이웃의 숫자를 찾는다 
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





  