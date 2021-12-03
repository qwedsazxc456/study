#단어임베딩1.py

#imdb 데이터셋 가져와서 사용-> ndarray

from tensorflow.keras.datasets import reuters  
from tensorflow.keras import preprocessing 

#특성으로 사용할 단어의 숫자
max_features = 10000

max_length=50 #영화 리뷰에서 단어의 개수가 20개 까지만 처리할 예정임 
(X_train, y_train), (X_test, y_test) = reuters.load_data(num_words=max_features)
print( X_train[:5]) #시퀀스 -숫자의 연속 배열
print( y_train[:5])

#리스트를 (samples, max_length) 형태의 2D 텐서로(ndarray)바꿔야 한다 
X_train = preprocessing.sequence.pad_sequences( X_train, maxlen=max_length )
X_test = preprocessing.sequence.pad_sequences( X_test, maxlen=max_length )
print( X_train[:5]) 

#target 를 원핫인코딩 \
from tensorflow.keras.utils import to_categorical

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Embedding 

#임베딩층은 단어벡터화가 진행된 층이다. 이 층을 통해서 학습을 시킨다 
#임베딩층은 단어와 단어사이를 knn이웃처럼 거리로 계산 
#8차원의 공간을 만들고 그 공간 속에 흩어져 있는 데이터로 바라본다 
model = Sequential()
model.add( Embedding(max_features, 8, input_length = max_length))
model.add(Flatten()) #CNN -> Deeplearning
#model.add(Dense(256, activation="relu" ))
model.add(Dense(46, activation="softmax")) #긍부정판단 둘중하나 sigmoid

model.compile(optimizer="rmsprop", loss="categorical_crossentropy", 
        metrics=['accuracy'])

model.summary() #내부 파라미터- 모델에 대한 부분 확인가능

history = model.fit(X_train, y_train, 
epochs=10, batch_size=32, validation_split=0.2)

results = model.evaluate(X_train, y_train)
print("훈련셋:",results)
results = model.evaluate(X_test, y_test)
print("테스트셋:",results)





