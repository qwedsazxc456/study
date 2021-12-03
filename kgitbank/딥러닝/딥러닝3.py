from tensorflow.keras.datasets import mnist  #우편번호 분리하려고 만든 데이테셋 
#전체 7만개
from tensorflow.keras.datasets import fashion_mnist

#교재의 데이터 분석 순서 정리하기 
#1.제공하는 데이터 불러오기 
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

#이미 데이터가 만들어져 있다. 60000개의 훈련데이터셋, 10000개의 테스트셋 
#신경망의 이미지는 3차원을 2차원으로 바꾸서 인식 
#딥러닝도 입력은 ndarray 2차원 출력은 ndarray 1차원  
#28 by 28 이미지가 60000 개가 있음
print( train_images.shape)  #이미지의 크기와 타입을 확인해보자 
print(type(train_images))

print( train_labels.shape)
print( train_labels[:10])

#2.딥러닝 모델을 만든다 
from tensorflow.keras import models 
from tensorflow.keras import layers 

#신경망 모델 만들기 
network = models.Sequential()

#필요한 만큼의 층을 쌓는다. 얼마큼 쌓을지는 아무도 모른다.
#층을 추가한다. - 입력층과 출력층 두개는 추가해야 한다 
network.add( layers.Dense(256, activation="relu", input_shape=(28*28, )) ) 
network.add( layers.Dense(256, activation="relu")) 
network.add( layers.Dense(128, activation="relu")) 
network.add( layers.Dense(64, activation="relu")) 
network.add( layers.Dense(10, activation="softmax")  )
#10 - 분류하고자 하는 데이터 개수(0~9) 10개   softmax
#분류는 결과를 확률로  0.1 0.01 0.12, ,, 0.62,  ,,, 
network.compile( optimizer="sgd",  
                 loss="categorical_crossentropy",
                 metrics=['accuracy'])  

#optimizer -  sgd:경사하강법, 최적화된 기울기를 찾아가는 통계학 기법중 하나 #
#loss - 회귀, 이진분류, 다중분류  categorical_crossentropy 
#evalute 함수를 호출할떄 평가기준을 무엇으로 볼까, 정확도   

#입력은 2차원형태이어야 한다  3차원 -> 2차원으로 벼경한다 
train_images = train_images.reshape( (60000, 28*28) )
test_images = test_images.reshape( (10000, 28*28) )

#딥러닝은 스케일링 필요 - normalize 0~1사이에 머무르게 한다 
train_images = train_images.astype('float32')/255
test_images = test_images.astype('float32')/255
#다중이미지분류 - 딥러닝은 반드시 원핫인코딩으로 해서 전달해야 한다 

from tensorflow.keras.utils import to_categorical #케라스가 제공하는 원핫인코딩 
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#학습시작 
hist =  network.fit (  
               train_images, 
               train_labels, 
               epochs=2, #총 학습횟수 
               batch_size=128 #데이터가 클때 학습한번하자고
                             #모든데이터한번에 메모리에
                             #로딩 못함, batch_size 에서준만큼 읽어와서 실행
         )

train_loss, train_acc = network.evaluate( train_images, train_labels)
print("훈련셋 손실 {} 정확도 {}".format(train_loss, train_acc))


test_loss, test_acc = network.evaluate( test_images, test_labels)
print("훈련셋 손실 {} 정확도 {}".format(test_loss, test_acc))
