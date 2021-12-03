#filename : commonUtil.py
#공통모듈은 프로그램이 가동중인 폴더, anaconda 설치된 lib 폴더아래에 
import matplotlib.pyplot as plt 
#차트 그리기 ( history)
def drawChartLoss(history):
    history_dict = history
    length = range(1,  len(history_dict['loss'])+1 )
    plt.plot( length, history_dict['loss'], 'bo', 
                    label='Training loss')
    plt.plot( length, history_dict['val_loss'], 'b', 
                    label='Validation loss')
    plt.show()                            
   
def drawChartAccuary(history):
    history_dict = history 
    length = range(1,  len(history_dict['acc'])+1 )
    plt.plot( length, history_dict['acc'], 'bo', 
                    label='Training acc')
    plt.plot( length, history_dict['val_acc'], 'b', 
                    label='Validation acc')
    plt.show() 

import numpy as np 
def vectorize_sequences( sequences, dimension=5000):
    results = np.zeros( (len(sequences), dimension) )

    for i, sequence in enumerate(sequences):
        #enumerate 함수, 데이터를 인덱스와 데이터로 반환 
        results[i, sequence] = 1. #results[i]에서 특정인덱스를1로
    return results 


def showDictionary(word_index, cnt):
    i=0
    for key in dict(word_index.items()):
        if i >= cnt: 
            break 
        i = i+1 
        print(key, dict(word_index.items())[key])

def sequencesToWords(word_index, data):
    temp = [(value, key) for (key, value) in word_index.items()]
    reverse_word_index = dict(temp) 
    decoded_review = ' '.join( 
          [reverse_word_index.get(i-3, '?') for i in data])
    return decoded_review