from sklearn.datasets import make_blobs
import mglearn
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier

#한글 지정하기 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'



X, y = mglearn.datasets.make_forge()

#1. 데이터 나누기 6:4로 나눠보자 

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.6, random_state=0
)

print(X_train.shape)
print(X_test.shape)

model = KNeighborsClassifier(n_neighbors=3) #n_neighbors 이 값을 1~10까지 가면서 적절한 이웃의 숫자를 찾는다 
                                                #3 쓴이유 - 강사마음 
#3.학습
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("훈련셋", model.score(X_train, y_train))
print("테스트셋", model.score(X_test, y_test))

fig, axes = plt.subplots(1, 3, figsize=(10, 3))
for i, ax in zip([1,3,9], axes):
    #2. 모델 만들기 
    model = KNeighborsClassifier(n_neighbors=i) #n_neighbors 이 값을 1~10까지 가면서 적절한 이웃의 숫자를 찾는다 
                                                #3 쓴이유 - 강사마음 

    #3.학습
    model.fit(X_train, y_train)
    mglearn.plots.plot_2d_separator(model, X, fill=True, eps=0.5, ax=ax, alpha=.4)
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
    ax.set_title("{}이웃".format(i))
    ax.set_xlabel("특성")
    ax.set_ylabel("이웃")
axes[0].legend(loc=3)

plt.show()