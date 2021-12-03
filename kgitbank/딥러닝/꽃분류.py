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
import tensorflow as tf 

def study():
        batch_size = 32  #한번에 불러오는 이미지 개수 
        img_height = 180 #이미지의 높이 
        img_width  = 180  #이미지의 넓이 

        data_augmentation = keras.Sequential(
                [
                        layers.experimental.preprocessing.RandomFlip("horizontal", 
                                    input_shape=(img_height, img_width, 3)),
                        layers.experimental.preprocessing.RandomRotation(0.1),
                        layers.experimental.preprocessing.RandomZoom(0.1),
                ]
        )

        model = models.Sequential()
        
        model.add(data_augmentation)
        model.add(layers.experimental.preprocessing.Rescaling(1./255)) #스케일링 

        model.add(layers.Conv2D(32, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dropout(0.2)) #중간에 데이터 절반을 없애버림 - 과대적합을 막기 위해서 
        model.add(layers.Dense(256, activation='relu'))
        model.add(layers.Dense(5, activation='softmax')) #5개로 분류 

        model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

        train_dir = "./data/flowers_/train"
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
                train_dir,
                validation_split=0.2,
                subset="training",  #훈련용
                seed=123,
                image_size=(img_height, img_width),
                batch_size=batch_size)
        
        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            train_dir,
            validation_split=0.2,
            subset="validation", #검증용 
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)

        epochs=5
        
        history = model.fit(
                train_ds,   #train_ds.repeat(1),
                epochs=epochs, 
                validation_data= val_ds
        )
                

        # 모델 저장하기 
        model.save('flowers_model.h5')      
        f = open("flowers_hist.hist", "wb")
        pickle.dump( history.history, file=f)
        f.close()

def drawChart():
        f = open("flowers_hist.hist", "rb")
        history = pickle.load(f)
        f.close()
        print( history.keys())
        acc = history['accuracy']
        val_acc = history['val_accuracy']
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

def Predict():
        model = load_model("flowers_model.h5")
        test_dir = "./data/flowers_/test"
        test_ds = tf.keras.preprocessing.image_dataset_from_directory(
                test_dir,
                seed=123,
                image_size=(180, 180),
                batch_size=1)
        print("-- Predict --")
        
        print("데이터개수 : ", tf.data.experimental.cardinality(test_ds).numpy())
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

        #데이터셋은 한번에 예측이 안된다. 
        i=0
        match_cnt=0
        for images, labels  in test_ds:
            output = model.predict(images) 
            #print( labels, np.argmax(output))
            if labels==np.argmax(output):
                match_cnt=match_cnt+1
            
        print("일치한 숫자 : ", match_cnt)
        print("불일치한 숫자 : ", tf.data.experimental.cardinality(test_ds).numpy()  - match_cnt)


def Evaluate():
        model = load_model("flowers_model.h5")
        batch_size = 32  #한번에 불러오는 이미지 개수 
        img_height = 180 #이미지의 높이 
        img_width  = 180  #이미지의 넓이 
        train_dir = "./data/flowers_/train"
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            train_dir,
            validation_split=0.2,
            subset="training",  #훈련용
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)
        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            train_dir,
            validation_split=0.2,
            subset="validation", #검증용 
            seed=123,
            image_size=(img_height, img_width),
            batch_size=batch_size)                                                                                                 
        test_dir = "./data/flowers_/test"
        test_ds = tf.keras.preprocessing.image_dataset_from_directory(
                test_dir,
                seed=123,
                image_size=(180, 180),
                batch_size=32)
    
        print( "훈련셋 : ",   model.evaluate(train_ds) )
        print( "검증셋 : ",   model.evaluate(val_ds) )
        print( "테스트셋 : ", model.evaluate(test_ds) )
        
if __name__=="__main__":
        while(True):
                print("1. 기본학습   ")
                print("2. 차트")
                print("3. 예측하기 ")
                print("4. 평가하기 ")
                sel = input("선택 : ")
                if sel=="1":
                    study()
                elif sel=="2":
                      drawChart()
                elif sel=="3":
                      Predict()
                elif sel=="4":
                      Evaluate()
                else:
                    break
        