import os, shutil
import pickle 
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# 이미지 전처리 유틸리티 모듈
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model 
import matplotlib.pyplot as plt
from tensorflow.keras import optimizers

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


        model.compile(loss='categorical_crossentropy',
                optimizer="sgd",   #optimizers.RMSprop(lr=1e-2),
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
                epochs=50,
                validation_data=validation_generator,
                validation_steps=50)

        # model.save('cats_and_dogs_small.h5')
        # file = open('cats_and_dogs_history.hist', 'wb' )
        # pickle.dump( history, file=file) #history 저장하기 
        # file.close()

Training()