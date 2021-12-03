import numpy as np 
import os 
import random 
import PIL.Image as pilimg 
import imghdr
import pandas as pd 
import tensorflow as tf

#데이터 만드는 수 
def makeData(folder, label, isTrain):
    if isTrain == 'train':
        path = "./data/chest_xray/train/" + folder
    else:
        path = "./data/chest_xray/test/" + folder
    data = []   # 이미지를 ndarray로 바꾸어서 저장할 배열
    labels = [] # 라벨  daisy 0, dandelion 1, rose 2, sunflower 3, tulip 4
    #고양이 사진을 읽어서 넘파이 바꾸고 
    i=1 
    for filename in os.listdir(path):   # os.listdir 해당 폴더의 디렉토리를 포함해서 모든 파일 목록을 가져온다
        if i%1000==0:
            print(i)
        i += 1
        try: 
            #print(filename)
            kind = imghdr.what(path + "/" + filename)
            #print(kind)
            if kind in ["gif", "png", "jpeg", "jpg"]:
                img = pilimg.open(path + "/" + filename) #이미지 크기가 다 달라서 이미지 크기를 변형한다 
                resize_img = img.resize( (150, 150 )) 
                pixel = np.array(resize_img) #이미지가 -> ndarray타입으로 전환된다. 
                if pixel.shape==(150, 150):
                    data.append(pixel)
                    labels.append(label) #고양이를 0 으로 본다 
        except:
            print(filename + " error ")

    #print( data )
    np.savez("xray_imagedata{}.npz".format(str(label) + '_' + isTrain), data=data, targets=labels)
    print("파일저장완료")

# #방법 1
# flowers = ["NORMAL", "PNEUMONIA"]
# label=0 
# for flower in flowers:
#      makeData(flower, label, 'train')
#      makeData(flower, label, 'test')
#      label += 1


normal = np.load("xray_imagedata0_train.npz")
pneumonia = np.load("xray_imagedata1_train.npz")


data1 = normal["data"]
target1 = normal["targets"]

data2 = pneumonia["data"]
target2 = pneumonia["targets"]

trainData = np.concatenate((data1, data2), axis=0)
print(trainData.shape)

trainTarget =np.concatenate((target1, target2), axis=0)
print(trainTarget.shape)


normal = np.load("xray_imagedata0_test.npz")
pneumonia = np.load("xray_imagedata1_test.npz")

data1 = normal["data"]
target1 = normal["targets"]

data2 = pneumonia["data"]
target2 = pneumonia["targets"]

testData = np.concatenate((data1, data2), axis=0)
print(testData.shape)

testTarget =np.concatenate((target1, target2), axis=0)
print(testTarget.shape)


tf.random.set_seed(2)

from tensorflow.keras import models
from tensorflow.keras import layers

network = models.Sequential()

network.add(layers.Conv2D(64, (3,3), activation='relu', input_shape=(150,150, 1))) #Convolutional 층 
network.add(layers.MaxPooling2D((2, 2))) #Pooling 층
network.add(layers.Flatten()) #완전연결층과 연결하기 위한 층 반드시 필요하다 
network.add(layers.Dense(32, activation='relu'))
network.add(layers.Dense(16, activation='relu'))
network.add(layers.Dense(2, activation='softmax'))

network.compile(optimizer='sgd',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

trainData = trainData.reshape((trainData.shape[0], 150,150, 1))
testData = testData.reshape((testData.shape[0], 150,150, 1))

print( trainData.shape) 

trainData = trainData.astype('float32')/255
testData = testData.astype('float32')/255

from tensorflow.keras.utils import to_categorical
trainTarget = to_categorical(trainTarget)
testTarget = to_categorical(testTarget)

hist = network.fit(trainData,
                    trainTarget,
                    epochs=10,          # 총 학습횟수
                    batch_size=100)

train_loss, train_acc = network.evaluate(trainData, trainTarget)
print('훈련셋 손실 {}   정확도 {}'.format(train_loss, train_acc))
test_loss, test_acc = network.evaluate(testData, testTarget)
print('테스트셋 손실 {}   정확도 {}'.format(test_loss, test_acc))