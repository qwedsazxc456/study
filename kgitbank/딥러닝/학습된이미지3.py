import tensorflow.keras
from tensorflow.keras.applications import VGG16

#keras 에 이미 있음 - 완전연결층은 사용 안함 
#이전에 이미 학습되었던 시스템을 불러온다 
conv_base = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(150, 150, 3))

#합성곱 기반 층 위에 완전연결 분류기 추가하기 

import matplotlib.pyplot as plt 
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers

base_dir = './dataset/cats_and_dogs_small'

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')


from tensorflow.keras import models
from tensorflow.keras import layers

def make_model():
    model = models.Sequential()
    model.add(conv_base)
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(5, activation='softmax'))

    print('conv_base를 동결하기 전 훈련되는 가중치의 수:', 
        len(model.trainable_weights))
    conv_base.trainable = False

    print('conv_base를 동결한 후 훈련되는 가중치의 수:', 
        len(model.trainable_weights))

    model.compile(loss='categorical_crossentropy',
                optimizer=optimizers.RMSprop(learning_rate=2e-5),
                metrics=['acc'])
    return model 

import imghdr
import PIL.Image as pilimg 
#데이터 만드는 수 
def makeData(path, label, savefilename):
    data = []   # 이미지를 ndarray로 바꾸어서 저장할 배열
    labels = [] 
    i=1 
    for filename in os.listdir(path):   # os.listdir 해당 폴더의 디렉토리를 포함해서 모든 파일 목록을 가져온다
        if i%1000==0:
            print(i)
        i += 1
        try: 
            kind = imghdr.what(path + "/" + filename)
            #print(kind)
            if kind in ["gif", "png", "jpeg", "jpg"]:
                img = pilimg.open(path + "/" + filename) #이미지 크기가 다 달라서 이미지 크기를 변형한다 
                resize_img = img.resize( (150, 150 )) 
                pixel = np.array(resize_img) #이미지가 -> ndarray타입으로 전환된다. 
                if pixel.shape==(150, 150, 3):
                    data.append(pixel)
                    labels.append(label) #고양이를 0 으로 본다 
        except:
            print(filename + " error ")
    np.savez(savefilename, data=data, targets=labels)
    print("파일저장완료")

def saveData():
    flowers = ["daisy", "dandelion", "rose", "sunflower", "tulip"]
     
    for i in range(len(flowers)):
        path = "./data/flowers_/train/"+flowers[i]  
        makeData(path, i, './flower/train_'+flowers[i]+".npz")
    
    for i in range(len(flowers)):
        path = "./data/flowers_/test/"+flowers[i]  
        makeData(path, i, './flower/test_'+flowers[i]+".npz")
    
#saveData() 

    
    
    #1.폴더안의 이미지를 다 읽어서 numpy 배열로 바꾸고 라벨링도 하고 
    # train, test 

    #2.학습하기

def getData():
    train_data=""
    train_label=""
    test_data=""
    test_label=""

    for file in os.listdir("./flower"):
        filedata = np.load("./flower/"+file)
        data1 = filedata["data"]
        target1 = filedata["targets"]

        if "train" in file:       
            if train_data =="":
                train_data = data1
                train_label = target1
            else:
                train_data = np.concatenate((train_data, data1), axis=0)
                train_label = np.concatenate((train_label, target1), axis=0)
        else:
            if test_data =="":
                test_data = data1
                test_label = target1
            else:
                test_data = np.concatenate((test_data, data1), axis=0)
                test_label = np.concatenate((test_label, target1), axis=0)


    print(train_data.shape)
    print(train_label.shape)
    return train_data, train_label, test_data, test_label

def study():
    #1.데이터 가져오기 
    train_data, train_label, test_data, test_label = getData()
    #2.모델 가져오기 
    model = make_model()
    #3.이미지 스케일링 작업 
    #4.라벨 원핫인코딩 
    #5.학습하기 





# acc = history.history['acc']
# val_acc = history.history['val_acc']
# loss = history.history['loss']
# val_loss = history.history['val_loss']

# epochs = range(len(acc))

# plt.plot(epochs, acc, 'bo', label='Training acc')
# from tensorflow.keras import layers

# plt.plot(epochs, val_acc, 'b', label='Validation acc')
# plt.title('Training and validation accuracy')
# plt.legend()

# plt.figure()

# plt.plot(epochs, loss, 'bo', label='Training loss')
# plt.plot(epochs, val_loss, 'b', label='Validation loss')
# plt.title('Training and validation loss')
# plt.legend()

# plt.show()