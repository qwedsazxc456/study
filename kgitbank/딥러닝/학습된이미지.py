from tensorflow.keras.applications import VGG16

#keras 에 이미 있음 - 완전연결층은 사용 안함 
#이전에 이미 학습되었던 시스템을 불러온다 
conv_base = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(150, 150, 3))

conv_base.summary()   #컨버 계층 까지만 


#마지막 층이 4 by 4 by 512 이다 

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

datagen = ImageDataGenerator(rescale=1./255)
batch_size = 20

#특성을 추출하자 
def extract_features(directory, sample_count):
    #block5_pool (MaxPooling2D)   (None, 4, 4, 512)         
    #받은 데이터 개수 만큼 0으로 채워진 4 by 4 by 512 배열 만들기 
    features = np.zeros(shape=(sample_count, 4, 4, 512))
    #라벨 - 정답 만들기 
    labels = np.zeros(shape=(sample_count))
    #디렉토리로부터 파일을 불러온다   - 디스크에 
    generator = datagen.flow_from_directory(
        directory,
        target_size=(150, 150),
        batch_size=batch_size,
        class_mode='binary')
    
    i = 0
    for inputs_batch, labels_batch in generator:
        #conv_base 로부터 예측 데이터를 가져온다 _특성을 가져온다 
        features_batch = conv_base.predict(inputs_batch)
        #해당 위치에 데이터 입력하기 0~31, 32~63, 64~95, .....
        features[i * batch_size : (i + 1) * batch_size] = features_batch
        #라벨은 전달받은 그대로 전달하기  
        labels[i * batch_size : (i + 1) * batch_size] = labels_batch
        print(i * batch_size, sample_count)
        i += 1
        if i * batch_size >= sample_count:
            
            # 제너레이터는 루프 안에서 무한하게 데이터를 만들어내므로 
            # 모든 이미지를 한 번씩 처리하고 나면 중지해야 한다 
            break
    return features, labels

#특성을 뽑아온다 
print("특성 추출중 1........")
train_features, train_labels = extract_features(train_dir, 2000)
print("특성 추출중 2........")
validation_features, validation_labels = extract_features(validation_dir, 1000)
print("특성 추출중 3........")
test_features, test_labels = extract_features(test_dir, 1000)
print("특성 추출중 4........")
#완전연결층에게 데이터를 전달하기 위해서 4차원에서 2차원으로 전환 
train_features = np.reshape(train_features, (2000, 4 * 4 * 512))
validation_features = np.reshape(validation_features, (1000, 4 * 4 * 512))
test_features = np.reshape(test_features, (1000, 4 * 4 * 512))



model = models.Sequential()
#완전연결층을 만든다 -  합성곱 연산을 안해도 되므로 속도가 빠르다 
model.add(layers.Dense(256, activation='relu', input_dim=4 * 4 * 512))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1, activation='sigmoid'))
#분류는 개와 고양이이므로 1단계 

model.compile(optimizer=optimizers.RMSprop(lr=2e-5),
              loss='binary_crossentropy',
              metrics=['acc'])
print("***************")
#내가 갖고있던 데이터가 아니라 새로 받아온 특성을 이용해 학습을 진행한다 
history = model.fit(train_features, train_labels,
                    epochs=30,
                    batch_size=20,
                    validation_data=(validation_features, validation_labels))
print("***************")

import matplotlib.pyplot as plt
acc = history.history['acc']
val_acc = history.history['val_acc']
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
