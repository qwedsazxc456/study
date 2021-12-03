#케라스 내부의 칼라이미지 사용하기 
from tensorflow.keras.datasets import cifar10
import numpy as np 
(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

#50000개의 훈련데이터셋, 10000개의 테스트셋 
#신경망의 이미지는 3차원을 2차원으로 바꾸서 인식 
import tensorflow as  tf
tf.random.set_seed(1234) #시드고정하기

print( train_images.shape)  #이미지의 크기와 타입을 확인해보자 
print(type(train_images))

print( train_labels.shape)
print( train_labels[:10])

#numpy 배열이라서  numpy 안에 unique 함수 유일한값을 배열형태로 전달 len 함수를 써서 타겟의 개수를 확인하자 
print( len(np.unique(train_labels)))

import matplotlib.pyplot as plt 

def imageShow(id):
    image = train_images[id]
    #cmap - 미리 지정된 파레트 
    plt.imshow(image, cmap= plt.cm.binary)
    plt.show()
#imageShow(0)

def imageShow2(train_images, row, col):
    plt.figure(figsize=(10, 5))
    for i in range(row*col):
        plt.subplot(row,col, i+1)
        image = train_images[i]
        plt.imshow(image, cmap= plt.cm.binary)
    plt.show()

imageShow2(train_images, 5, 5)

#3차원 2차원으로 바꿔서 딥러닝으로 학습하기 

from tensorflow.keras import models 
from tensorflow.keras import layers 

def make_model1():
    (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

    network = models.Sequential()
    network.add( layers.Dense(256, activation="relu", input_shape=(32*32*3, )))
    network.add( layers.Dense(256, activation="relu")) 
    network.add( layers.Dense(10, activation="softmax")) 

    network.compile( optimizer="sgd",  #바꿀 수 있다  rmsprop, sgd  
                    loss="categorical_crossentropy",
                    metrics=['accuracy']) 

    data = train_images.reshape( ( 50000, 32*32*3 )) #4차원 -> 2차원   32*32*3(3차원을) -> 1차원으로 
    data = data.astype('float32')/255  #스케일링 

    test = test_images.reshape( ( 10000, 32*32*3 )) #4차원 -> 2차원
    test = test.astype('float32')/255  #스케일링 

    #라벨은 원핫인코딩을 한다 
    from tensorflow.keras.utils import to_categorical 
    train_labels = to_categorical( train_labels )
    test_labels = to_categorical( test_labels )

    #학습시작함 
    hist =  network.fit ( data, 
                train_labels, 
                epochs=100, #총 학습횟수 
                batch_size=100
            )
    #머신러닝 score 함수 대신에 평가 
    train_loss, train_acc = network.evaluate( data, train_labels)
    print("훈련셋 손실 {} 정확도 {}".format(train_loss, train_acc))

    test_loss, test_acc = network.evaluate(test,   test_labels)
    print("테스트셋 손실 {} 정확도 {}".format(test_loss, test_acc))


#합성곱으로 학습하기 
#데이터를 3차원 그대로 넣을 수 있다 

#Convolutional 계층 - 이미지를 식별할 수 있는 필터를 자동으로 만든다. (많이)
#stride - 필터를 적용해서 이미지 전체를 스캔한다 
#padding - 필터를 자꾸 적용하다보면 이미지가 작아짐, 이미지의 경계를 강제로 0으로 채워서 줄지않도록
#pooling - 중요한 특성만 찾아낸다. 
#dropout - 인위적으로 노이즈를 일으킨다. 데이터를 반쯤 날려서 일반화가 되도록 한다 
#Flatten - Convolutional 계층이 내보내는 출력을 완전연결층하고 맵핑하는 역할을 한다 

def make_model2():
    (train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

    model = models.Sequential()
    model.add(layers.Conv2D(64, (3,3), activation='relu', input_shape=(32, 32, 3))) #Convolutional 층 
    model.add(layers.MaxPooling2D((2, 2))) #Pooling 층
    model.add(layers.Conv2D(32, (3,3), activation='relu'))  
    model.add(layers.Conv2D(32, (3,3), activation='relu')) 
    model.add(layers.MaxPooling2D((2, 2))) #Pooling 층
    model.add(layers.Conv2D(32, (3,3), activation='relu')) 
    model.add(layers.MaxPooling2D((2, 2))) #Pooling 층
    
    model.add(layers.Flatten()) #완전연결층과 연결하기 위한 층 반드시 필요하다 
    
    model.add(layers.Dense(256, activation='relu')) #완전연결층(feed forward 층)
    model.add(layers.Dense(128, activation='relu')) #완전연결층(feed forward 층)
    model.add(layers.Dense(64, activation='relu')) #완전연결층(feed forward 층)
    model.add(layers.Dense(10, activation='softmax'))
    model.compile( optimizer="rmsprop",
               loss="categorical_crossentropy",
               metrics=['accuracy'])

    from tensorflow.keras.utils import to_categorical 
    train_labels = to_categorical( train_labels )
    test_labels = to_categorical( test_labels )

    train_images=train_images/255
    test_images=test_images/255
    model.fit( train_images, train_labels, epochs=50, batch_size=100)


    #평가 
    results = model.evaluate( train_images, train_labels)
    print(results)
    results = model.evaluate( test_images, test_labels)
    print(results)

make_model1()
