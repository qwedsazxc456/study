from tensorflow.keras.datasets import mnist  #우편번호 분리하려고 만든 데이테셋 
#전체 7만개
import tensorflow as  tf
tf.random.set_seed(1234) #시드고정하기

#교재의 데이터 분석 순서 정리하기 
#1.제공하는 데이터 불러오기 
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

#이미 데이터가 만들어져 있다. 60000개의 훈련데이터셋, 10000개의 테스트셋 
#신경망의 이미지는 3차원을 2차원으로 바꾸서 인식 
#28 by 28 이미지가 60000 개가 있음
print( train_images.shape)  #이미지의 크기와 타입을 확인해보자 
print(type(train_images))

print( train_labels.shape)
print( train_labels[:10])

#2.딥러닝 모델을 만든다 
from tensorflow.keras import models 
from tensorflow.keras import layers 

#신경망 모델(네트워크) 만들기 
network = models.Sequential()
#층을 추가한다. - 입력층과 출력층 두개는 추가해야 한다
network.add(layers.Conv2D(64, (3,3), activation='relu', input_shape=(28, 28, 1))) #Convolutional 층 
network.add(layers.MaxPooling2D((2, 2))) #Pooling 층
network.add(layers.Conv2D(32, (3,3), activation='relu'))  
network.add(layers.Conv2D(32, (3,3), activation='relu')) 
network.add(layers.MaxPooling2D((2, 2))) #Pooling 층
network.add(layers.MaxPooling2D((2, 2))) #Pooling 층
network.add(layers.Flatten()) #완전연결층과 연결하기 위한 층 반드시 필요하다 

network.add( layers.Dense(64, activation="relu"))
network.add( layers.Dense(10, activation="softmax")  )

network.compile( optimizer="sgd",  
                 loss="categorical_crossentropy",
                 metrics=['accuracy']) 


#입력은 2차원형태이어야 한다  3차원 -> 2차원으로 벼경한다 
train_images = train_images.reshape( (60000, 28, 28, 1) )
test_images = test_images.reshape( (10000, 28, 28, 1) )

#딥러닝은 스케일링 필요 - normalize 0~1사이에 머무르게 한다 
train_images = train_images.astype('float32')/255
test_images = test_images.astype('float32')/255
#다중이미지분류 - 딥러닝은 반드시 원핫인코딩으로 해서 전달해야 한다 

from tensorflow.keras.utils import to_categorical #케라스가 제공하는 원핫인코딩 
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

#학습시작 
hist =  network.fit (  train_images, 
               train_labels, 
               epochs=10, #총 학습횟수 
               batch_size=128 #데이터가 클때 학습한번하자고
                             #모든데이터한번에 메모리에
                             #로딩 못함, batch_size 에서
                             #준만큼 읽어와서 실행
         )

train_loss, train_acc = network.evaluate( train_images, train_labels)
print("훈련셋 손실 {} 정확도 {}".format(train_loss, train_acc))
test_loss, test_acc = network.evaluate( test_images, test_labels)
print("테스트셋 손실 {} 정확도 {}".format(test_loss, test_acc))


#0.9147999882698059