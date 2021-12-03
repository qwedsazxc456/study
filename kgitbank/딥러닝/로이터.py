from tensorflow.keras.datasets import reuters 
from tensorflow.keras import models 
from tensorflow.keras import layers

(train_data, train_labels), (test_data, test_labels)= reuters.load_data(num_words=10000)
#자주 쓰는 데이터만 
print( train_data[:5])
print( train_labels[:5])

#데이터가 시퀀스로 온다. 문자열(단어)의 경우 그 자체로는 딥러닝을 못한다
#사전을 정해두고 단어들을 사전의 index 로 바꾸어서 해야 한다 
#이를 시퀀스라고 한다 

# #원래의 단어로 바꾸어서 보자 ################################3
word_index = reuters.get_word_index()
print( word_index )

print( type(word_index.items())) #dict하고 달라서 dict타입으로 전환

# 내부 구조 확인해보기 
def showDictionary(cnt):
    i=0
    for key in dict(word_index.items()):
        if i >= cnt: 
            break 
        i = i+1 
        print(key, dict(word_index.items())[key])

showDictionary(10)

#숫자 -> 단어로 바꿔보자  word_index 는 '단어':숫자   dict 타입은 키로 검색가능 값으로 검색이 안된다. 
# 'school':123  'go':23  => 키와값을 바꿔치기를 해보자  123:'school'  23:'go'

temp = [(value, key) for (key, value) in word_index.items()]
reverse_word_index = dict(temp) 
print(reverse_word_index)


#index -> 단어로 바꾸어서  - 다 합쳐서 보자 
decoded_review = ' '.join( [reverse_word_index.get(i-3, '?')  for i in train_data[0]])
print( decoded_review)

print( type(train_data) )

#원핫인코딩 
import numpy as np 
def vectorize_sequences( sequences, dimension=10000):
    results = np.zeros( (len(sequences), dimension) )  #2차원배열 
    # I(4) like(2) star(5)
    # 0 0 1 0 1 1 0 0 0 0  ..........  I 

    #0으로 채워진 numpy 배열을 만든다. 
    #np.zeros( 행, 열) - 행 by 열 만큼 0으로 이루어진 행렬을 
    #                   만들어주는 함수이다 
    #미리 메모리 확보하고 
    for i, sequence in enumerate(sequences):
        #enumerate 함수, 데이터를 인덱스와 데이터로 반환 
        results[i, sequence] = 1. #results[i]에서 특정인덱스를1로
    return results 

X_train = vectorize_sequences(train_data)
print( X_train[:3])
X_test = vectorize_sequences(test_data)


#출력데이터를 벡터로 전환  - 기사 섹션 46 
from tensorflow.keras.utils import to_categorical
one_hot_train_labels = to_categorical(train_labels)
one_hot_test_labels = to_categorical(test_labels)

print( one_hot_train_labels)


# #훈련셋을 훈련셋과 검증셋으로 나눈다 
X_val = X_train[:1000] #훈련셋을 만개만 
partial_x_train = X_train[1000:] #검증셋 
y_val = one_hot_train_labels[:1000]
partial_y_train = one_hot_train_labels[1000:]

model = models.Sequential()
model.add( layers.Dense(64, activation="relu", input_shape=(10000,)))
model.add( layers.Dense(64, activation="relu"))
model.add( layers.Dense(46, activation="softmax")) #이진분류, 결과가 1, activation 시그모이드 

model.compile( optimizer='rmsprop', 
               loss='categorical_crossentropy',
               metrics=['accuracy'])

history = model.fit( partial_x_train, 
                     partial_y_train, 
                     epochs=10, 
                     batch_size=100, 
                     validation_data = (X_val, y_val) )

results = model.evaluate(partial_x_train, partial_y_train)
print(results)


#훈련과 검증  정확도 그리기 
import matplotlib.pyplot as plt 
history_dict = history.history 
acc = history_dict['accuracy']  #훈련셋 정확도
val_acc = history_dict['val_accuracy'] #검증셋 정확도 

print(acc)
print(val_acc)

length = range(1,  len(history_dict['accuracy'])+1 ) #x축만들기 
plt.plot( length, acc , 'bo',  label='Training acc')
plt.plot( length, val_acc , 'b', label='Validation acc')
plt.title("Training and Validation acc")
plt.xlabel('Epochs')
plt.ylabel('Acc')
plt.legend()
plt.show()  