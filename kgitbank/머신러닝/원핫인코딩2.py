#Tokenizer 클래스 영어기반 한글 적용 어렵다.

from typing import Sequence
import numpy as np
from tensorflow.python.keras.preprocessing.text import one_hot
samples= ['The cat sat on the mat',
         'The dog ate my homework',
         'The cat is very cute',
         'The fox if very smart and very beatiful and follow people well']

from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(num_words=50)
tokenizer.fit_on_texts(samples) #사전이 만들어진다.

sequence=tokenizer.texts_to_sequences(samples)
print(sequence) #텍스트를 숫자로 만든다

#사전
word_index = tokenizer.word_index
print(word_index)

#원핫인코딩
one_hot_results = tokenizer.texts_to_matrix(samples, mode='binary')
print(one_hot_results)

#희소행렬, sparse matrix: 0이 많아서 -> 원핫해싱