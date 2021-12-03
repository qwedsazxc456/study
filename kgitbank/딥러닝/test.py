#https://www.tensorflow.org/tutorials/images/classification

import os, shutil
import pickle 
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# 이미지 전처리 유틸리티 모듈
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model 
import matplotlib.pyplot as plt
from tensorflow.keras import optimizers

import numpy as np 
import os 
import random 
import PIL.Image as pilimg 
import imghdr
import pandas as pd 

# 원본 데이터셋을 압축 해제한 디렉터리 경로-원래 이미지 있는 폴더 
original_dataset_dir = './dataset/cats_and_dogs/train'

#옮길 위치 
base_dir = './dataset/cats_and_dogs_small'

train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')

#-------------------------------------
train_cats_dir = os.path.join(train_dir, 'cats')
train_dogs_dir = os.path.join(train_dir, 'dogs')

test_cats_dir = os.path.join(test_dir, 'cats')
test_dogs_dir = os.path.join(test_dir, 'dogs')

validation_cats_dir = os.path.join(validation_dir, 'cats')
validation_dogs_dir = os.path.join(validation_dir, 'dogs')

#이미지 복사
def ImageCopyMove():
    #디렉토리내의 파일 개수 알아내기 
    totalCount = len(os.listdir(original_dataset_dir))
    print("전체개수 : ", totalCount)
    # 소규모 데이터셋을 저장할 디렉터리
    
    # 반복적인 실행을 위해 디렉토리를 삭제합니다.
    if os.path.exists(base_dir):  #기존에 디렉토리가 존재하면 전부 지우기 
        shutil.rmtree(base_dir, ignore_errors=True, onerror=None)   
    
    #새로폴더만들기
    os.mkdir(base_dir) #없으면 만들기 

    os.mkdir(train_dir)
    os.mkdir(validation_dir)
    os.mkdir(test_dir)

    os.mkdir(train_cats_dir)
    print( train_cats_dir) 
    os.mkdir(train_dogs_dir)
    os.mkdir(validation_cats_dir)
    os.mkdir(validation_dogs_dir)
    os.mkdir(test_cats_dir)
    os.mkdir(test_dogs_dir)

    # 처음 1,000개의 고양이 이미지를 train_cats_dir에 복사합니다
    fnames = ['cat.{}.jpg'.format(i) for i in range(1000)]
    for fname in fnames:
            src = os.path.join(original_dataset_dir, fname)
            dst = os.path.join(train_cats_dir, fname)
            shutil.copyfile(src, dst)

    # 다음 500개 고양이 이미지를 validation_cats_dir에 복사합니다
    fnames = ['cat.{}.jpg'.format(i) for i in range(1000, 1500)]
    for fname in fnames:
            src = os.path.join(original_dataset_dir, fname)
            dst = os.path.join(validation_cats_dir, fname)
            shutil.copyfile(src, dst)
    
    # 다음 500개 고양이 이미지를 test_cats_dir에 복사합니다
    fnames = ['cat.{}.jpg'.format(i) for i in range(1500, 2000)]
    for fname in fnames:
            src = os.path.join(original_dataset_dir, fname)
            dst = os.path.join(test_cats_dir, fname)
            shutil.copyfile(src, dst)
    
    # 처음 1,000개의 강아지 이미지를 train_dogs_dir에 복사합니다
    fnames = ['dog.{}.jpg'.format(i) for i in range(1000)]
    for fname in fnames:
            src = os.path.join(original_dataset_dir, fname)
            dst = os.path.join(train_dogs_dir, fname)
            shutil.copyfile(src, dst)
    
    # 다음 500개 강아지 이미지를 validation_dogs_dir에 복사합니다
    fnames = ['dog.{}.jpg'.format(i) for i in range(1000, 1500)]
    for fname in fnames:
            src = os.path.join(original_dataset_dir, fname)
            dst = os.path.join(validation_dogs_dir, fname)
            shutil.copyfile(src, dst)
    
    # 다음 500개 강아지 이미지를 test_dogs_dir에 복사합니다
    fnames = ['dog.{}.jpg'.format(i) for i in range(1500, 2000)]
    for fname in fnames:
            src = os.path.join(original_dataset_dir, fname)
            dst = os.path.join(test_dogs_dir, fname)
            shutil.copyfile(src, dst)

#ImageCopyMove()

def Training():
        model = models.Sequential()
        model.add(layers.Conv2D(32, (3, 3), activation='relu',  input_shape=(150, 150, 3)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(16, activation='relu'))
        model.add(layers.Dense(1, activation='sigmoid')) #이진 분류라서 1, sigmoid 

        model.summary() #내부에 모델의 학습과정 - 특성들으 확인 가능하다 


        model.compile(loss='binary_crossentropy',
                optimizer=optimizers.RMSprop(learning_rate=1e-4),
                metrics=['acc'])

        train_datagen = ImageDataGenerator(
                rescale=1./255,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True)
        test_datagen = ImageDataGenerator(rescale=1./255)
        train_generator = train_datagen.flow_from_directory(
                train_dir,
                target_size=(150, 150),
                batch_size=20,
                class_mode='binary')
        validation_generator = test_datagen.flow_from_directory(
                validation_dir,
                target_size=(150, 150),
                batch_size=20,
                class_mode='binary')
        #함수가 fit_generator 가 없어짐 
        

        history = model.fit(
                train_generator,
                steps_per_epoch=100,
                epochs=10,
                validation_data=validation_generator,
                validation_steps=50)

        model.save('cats_and_dogs_small.h5')

        file = open('cats_and_dogs_history.hist', 'wb' )
        pickle.dump( history.history, file=file) #history 저장하기 
        file.close()

def LoadModels():

        #저장된 모델 불러오기 
        model = load_model('cats_and_dogs_small.h5')
        file = open('cats_and_dogs_history.hist', 'rb' )
        history = pickle.load(file)
        file.close()
        

        acc = history['acc']
        val_acc = history['val_acc']
        loss = history['loss']
        val_loss = history['val_loss']

        epochs = range(len(acc))

        plt.plot(epochs, acc, 'bo', label='Training acc')
        plt.plot(epochs, val_acc, 'b', label='Validation acc')
        plt.title('Training and validation accuracy')
        plt.legend()

        plt.figure()

        plt.plot(epochs, loss, 'bo', label='Training loss')
        plt.plot(epochs, val_loss, 'b', label='Validation loss')
        plt.title('Training and validation loss')
        plt.legend()

        plt.show()

def ImageIncrease():
        #데이터 증식 사용하기-이전버전거라 안돌아감 
        #ImageDataGenerator 로 이미지 증식은 더이상 못함 
        datagen = ImageDataGenerator(
                rotation_range=40,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True,
                fill_mode='nearest')


        #rotation_range는 랜덤하게 사진을 회전시킬 각도 범위입니다(0-180 사이).
        #width_shift_range와 height_shift_range는 사진을 수평과 수직으로 랜덤하게 평행 이동시킬 범위입니다(전체 넓이와 높이에 대한 비율).
        #shear_range는 랜덤하게 전단 변환을 적용할 각도 범위입니다.
        #zoom_range는 랜덤하게 사진을 확대할 범위입니다.
        #horizontal_flip은 랜덤하게 이미지를 수평으로 뒤집습니다. 수평 대칭을 가정할 수 있을 때 사용합니다(예를 들어, 풍경/인물 사진).
        #fill_mode는 회전이나 가로/세로 이동으로 인해 새롭게 생성해야 할 픽셀을 채울 전략입니다.\

   
        fnames = sorted([os.path.join(train_cats_dir, fname) for fname in os.listdir(train_cats_dir)])

        # 증식할 이미지 선택합니다
        img_path = fnames[0]

        # 이미지를 읽고 크기를 변경합니다
        img = image.load_img(img_path, target_size=(150, 150))

        # (150, 150, 3) 크기의 넘파이 배열로 변환합니다
        x = image.img_to_array(img)

        # (1, 150, 150, 3) 크기로 변환합니다
        x = x.reshape((1,) + x.shape)

        # flow() 메서드는 랜덤하게 변환된 이미지의 배치를 생성합니다.
        # 무한 반복되기 때문에 어느 지점에서 중지해야 합니다!
        i = 0
        for batch in datagen.flow(x, batch_size=1):
                plt.figure(i)
                imgplot = plt.imshow(image.array_to_img(batch[0]))
                i += 1
                if i % 4 == 0:
                        break
        plt.show()
        print("$$$$$$$")

import tensorflow as tf



#데이터 증식 - 새로운 버전에서 사라짐 
def DataIncrease():
        batch_size = 32  #한번에 불러오는 이미지 개수 
        img_height = 180 #이미지의 높이 
        img_width = 180  #이미지의 넓이 

        data_augmentation = keras.Sequential(
                [
                        layers.experimental.preprocessing.RandomFlip("horizontal", 
                                                                input_shape=(img_height, img_width, 3)),
                        layers.experimental.preprocessing.RandomRotation(0.1),
                        layers.experimental.preprocessing.RandomZoom(0.1),
                ]
        )

        model = models.Sequential()
        
        #model.add(layers.experimental.preprocessing.Rescaling(1./255, input_shape=(img_height, img_width, 3)))
        model.add(data_augmentation)
        model.add(layers.experimental.preprocessing.Rescaling(1./255))

        model.add(layers.Conv2D(32, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dropout(0.5)) #중간에 데이터 절반을 없애버림 - 과대적합을 막기 위해서 
        model.add(layers.Dense(512, activation='relu'))
        model.add(layers.Dense(2, activation='softmax'))

        model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
                train_dir,
                validation_split=0.2,
                subset="training",
                seed=123,
                image_size=(img_height, img_width),
                batch_size=batch_size)
        
        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
                validation_dir,
                validation_split=0.2,
                subset="validation",
                seed=123,
                image_size=(img_height, img_width),
                batch_size=batch_size)
        

        epochs=5
        history = model.fit(
                train_ds,   #train_ds.repeat(1),
                validation_data=val_ds,
                epochs=epochs
        )
                

        # #모델 저장하기 
        model.save('cats_and_dogs_small.h5')      

        acc = history.history['accuracy']
        val_acc = history.history['val_accuracy']
        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs = range(len(acc))

        plt.plot(epochs, acc, 'bo', label='Training acc')
        plt.plot(epochs, val_acc, 'b', label='Validation acc')
        plt.title('Training and validation accuracy')
        plt.legend()

        plt.figure()

        plt.plot(epochs, loss, 'bo', label='Training loss')
        plt.plot(epochs, val_loss, 'b', label='Validation loss')
        plt.title('Training and validation loss')
        plt.legend()

        plt.show()

import numpy as np
def Predict():
        model = load_model("cats_and_dogs_small.h5")
        test_datagen = ImageDataGenerator(rescale=1./255)
        validation_generator = test_datagen.flow_from_directory(
                validation_dir,
                target_size=(150, 150),
                batch_size=1,
                class_mode='categorical')

        print("-- Predict --")
        output = model.predict(validation_generator)
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
        print(validation_generator.class_indices)
       
        i=0
        match_cnt=0
        for input_batch, labels_batch in validation_generator:
                print(labels_batch,  np.argmax(output[i]))
                if np.argmax(labels_batch)==np.argmax(output[i]):
                        match_cnt=match_cnt+1
                i=i+1
                if i == 500: 
                       break 
        print("일치한 숫자 : ", match_cnt)
        print("불일치한 숫자 : ", 500-match_cnt)
        
if __name__=="__main__":
        while(True):
                print("1. 이미지 복사")
                print("2. 기본학습   ")
                print("3. 모듈 로딩하기")
                print("4. 이미지 증가")
                print("5. 데이터 증식 ")
                print("6. 예측하기 ")
                
                sel = input("선택 : ")
                if sel=="1":
                        ImageCopyMove()
                elif sel=="2":
                        Training()
                elif sel=="3":
                        LoadModels()
                elif sel=="4":
                        ImageIncrease()
                elif sel=="5":
                        DataIncrease()
                elif sel=="6":
                        Predict()
                else:
                        break
        