#PCA - 고차원 데이터 셋의 시각화 - 암환자 산포도 그리려면 32 by 32 개의 차트를 그려야 한다 
#악성과 양성의 두 클래스에 대한 각각의 히스토그램을 그려보자
from numpy.lib.function_base import piecewise
from sklearn.datasets import make_blobs
import mglearn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
import numpy as np 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#한글 지정하기 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'


#fetch_lfw_people - 얼굴 이미지 데이터

#C:\Users\user\scikit_learn_data\lfw_home\lfw_funneled\Donald_Rumsfeld
from sklearn.datasets import fetch_lfw_people
#사진이 20개 이상인 사람만 추출한다 
people = fetch_lfw_people(min_faces_per_person=20, resize=0.7)
#20명의 사람 얼굴, 크기를 0.7로 바꿔서 불러오기 
image_shape = people.images[0].shape  #첫번째 이미지의 크기가 87 X 65
print(image_shape) #전체 특성 87 by 65 
from PIL import Image 

#화면을 2 by 5로 나눈다 
fig, axes = plt.subplots(2, 5, figsize=(15, 8),
                         subplot_kw={'xticks': (), 'yticks': ()})
for target, image, ax in zip(people.target, people.images, axes.ravel()):
    ax.imshow(image)
    ax.set_title(people.target_names[target])
#plt.show()

print( people.keys() )

#각 타깃이 나타난 횟수 계산
counts = np.bincount(people.target) ##dataframe의 value_count
print( counts )

# 타깃별 이름과 횟수 출력
for i, (count, name) in enumerate(zip(counts, people.target_names)):
    print("{0:25} {1:3}".format(name, count))
    

#사진이 누구는 20개 있고 누구는 530개 있음 이중에서 50 개 씩만 추출하자 
print(people.target.shape) #1058개의 mask 배열을 만든다 
#False, False, False 
#각 조지부시 
print(people.target)
print(people.target_names)
mask = np.zeros(people.target.shape, dtype=np.bool) # 0으로 채워진 2차원배열 
print(mask)
print( np.unique(people.target)) #배열에서 유일한 타겟을 찾아낸다

for target in np.unique(people.target): #타깃들로부터 중복을 제거한다 
    #np.where 조건을 만족하는 데이터 배열을 반환한다 
    print( np.where(people.target == target) )#2차원형태 
    #앞에 50개만 골라서 True 설정하기 
    mask[np.where(people.target == target)[0][:50]] = 1

#해당 데이터만 고른다 
X_people = people.data[mask]
y_people = people.target[mask]

print( X_people.shape )
print( y_people.shape )

# # 0~255 사이의 흑백 이미지의 픽셀 값을 0~1 사이로 스케일 조정합니다.
# # (옮긴이) MinMaxScaler를 적용하는 것과 거의 동일합니다.
# X_people = X_people / 255. #스케일조정, 이미지 값이 0~255중에 하나값을 가지므로 

# from sklearn.neighbors import KNeighborsClassifier
# # 데이터를 훈련 세트와 테스트 세트로 나눕니다
# X_train, X_test, y_train, y_test = train_test_split(
#     X_people, y_people, stratify=y_people, random_state=0)
# # 이웃 개수를 한 개로 하여 KNeighborsClassifier 모델을 만듭니다
# knn = KNeighborsClassifier(n_neighbors=1)
# knn.fit(X_train, y_train)
# print("1-최근접 이웃의 테스트 세트 점수: {:.2f}".format(knn.score(X_test, y_test)))


# #주성분분석 (5655개의 특성중에서 100개만 선택한다 )
# pca = PCA(n_components=100, whiten=True, random_state=0).fit(X_train)
# X_train_pca = pca.transform(X_train)
# X_test_pca = pca.transform(X_test)

# #100개의 특성만으로 Knn 학습을 진행함 
# print("X_train_pca.shape:", X_train_pca.shape)
# knn = KNeighborsClassifier(n_neighbors=1)
# knn.fit(X_train_pca, y_train)
# print("주성분 테스트 세트 정확도: {:.2f}".format(knn.score(X_test_pca, y_test)))
# print("pca.components_.shape:", pca.components_.shape)
# #100개로 해도 57%로 맞춤 

# fig, axes = plt.subplots(3, 5, figsize=(15, 12),
#                          subplot_kw={'xticks': (), 'yticks': ()})
# for i, (component, ax) in enumerate(zip(pca.components_, axes.ravel())):
#     ax.imshow(component.reshape(image_shape), cmap='viridis')
#     ax.set_title("주성분 {}".format((i + 1)))
# plt.show()
    