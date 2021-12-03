import os 
import numpy as np
from tensorflow.keras.preprocessing import sequence 

#파일로부터 데이터를 읽어서 ndarray 타입으로 전환하자 

folder_url="./dataset/aclImdb/aclImdb/train"
#현재 이 폴더아래에 데이터 파일이 있다 

def getData(folder_url):
    #텍스트 파일을읽어서 저장할 변수
    texts = []
    #라벨을 읽어서 저장 
    labels = []

    #부정적 데이터를
    # os.listdir(경로명) 해당경로의 모든 파일을 가져온다  
    neg_url = folder_url+"/neg"
    i=1
    for filename in os.listdir(neg_url):
        if i%100==0:
            print("{}번째처리중...".format(i))
        i+=1

        f = open(neg_url +"/"+filename, "r", encoding="utf8")
        #print(f.read())
        texts.append(f.read())
        labels.append(0) #부정으로 
        f.close()

    pos_url = folder_url+"/pos"
    i=1
    for filename in os.listdir(neg_url):
        if i%100==0:
           print("{}번째처리중...".format(i))
        i+=1
        f = open(neg_url +"/"+filename, "r", encoding="utf8")
        #print(f.read())
        texts.append(f.read())
        labels.append(1) #긍정으로 
        f.close()
    return texts, labels 

    # for label, text in zip(texts, labels):
    #     print(label, text)

import pickle 
def save(texts, labels):
    f = open("imdb.dat", "wb")
    data = {"texts":texts, "labels":labels}
    pickle.dump(data, file=f)
    f.close() 

def load():
    print("*************")
    #불러오기
    f = open("imdb.dat", "rb")
    data = pickle.load(f)
    texts = data["texts"]
    labels = data["labels"]
    f.close()

    return texts, labels 
 
# texts, labels = getData(folder_url)
# save(texts, labels)
texts, labels =load()

#데이터를 ndarray로 바꾸는 과정이 필요
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

maxlen = 100 #한문장을 구성하는 단어는 최대 100개이다 

train_samples = 20000
validatin_samples = 5000
max_words = 10000 #특성은최대 10000개 까지만 처리한다 

#토큰을 나누고 사전만들기
tokenizer = Tokenizer(num_words= max_words)
tokenizer.fit_on_texts(texts) #토큰화를 한다 

#dict 타입 
word_index = tokenizer.word_index
i=1
for word in word_index:
    if i>50:
        break
    i=i+1
    print(word, word_index[word])

#2D 텐서 -2차원배열, ndarray 
sequences = tokenizer.texts_to_sequences(texts)
print(sequences[:5])
data = pad_sequences(sequences, maxlen=maxlen)
print(data[:5])

#라벨도 1D(1차원) ndarray로 바꾸자 
labels = np.asarray( labels )

print(data.shape)
print(labels.shape)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(data, labels, random_state=0)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Embedding 

#임베딩층은 단어벡터화가 진행된 층이다. 이 층을 통해서 학습을 시킨다 
#임베딩층은 단어와 단어사이를 knn이웃처럼 거리로 계산 
#8차원의 공간을 만들고 그 공간 속에 흩어져 있는 데이터로 바라본다 
model = Sequential()
model.add( Embedding(max_words, 8, input_length = maxlen))
model.add(Flatten()) #CNN -> Deeplearning
model.add(Dense(16, activation="relu", ))
model.add(Dense(1, activation="sigmoid")) #긍부정판단 둘중하나 sigmoid

model.compile(optimizer="rmsprop", loss="binary_crossentropy", 
        metrics=['acc'])

model.summary() #내부 파라미터- 모델에 대한 부분 확인가능

history = model.fit(X_train, y_train, 
epochs=10, batch_size=32, validation_split=0.2)

results = model.evaluate(X_train, y_train)
print("훈련셋:",results)
results = model.evaluate(X_test, y_test)
print("테스트셋:",results)






