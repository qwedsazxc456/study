from os import path
from nltk.tag.brill import Word
from wordcloud import WordCloud
import nltk
from matplotlib import font_manager, rc, matplotlib_fname
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import  ImageColorGenerator
from PIL import Image

#한국 법률 말뭉치
from konlpy.corpus import kolaw
from konlpy.tag import  Okt #형태소를 분석하는 라이브러리 (예전에 Twitter)
import wordcloud 

def createTokens():
    constitution = kolaw.open('constitution.txt').read()

    #형태소 분석하기 
    okt = Okt() 
    tokens = okt.nouns(constitution)  #Okt의 nouns 함수가 명사 분리 
    #print(tokens)


    #불필요한 단어들을 제거하기 
    stop_words = ["최초", "다만", "대하", "모든", "거나"]
    #comprehension 을 이용해서 제거하자 

    tokens = [ word for word in tokens   if word not in  stop_words and len(word)>=2]
    #print(tokens)
    #stop_words 에 있는 데이터만 제거된다 

    #각 토큰별 빈도수를 센다. (nltk - 자연어 처리)

    tokens_count = nltk.Text( tokens, name="헌법")
    #print( tokens_count)  #Text  객체로 전환 

    data = tokens_count.vocab().most_common(100) #자주 쓰는 단어 100개만 
    print( data )

    # tuple  형태인데 dict  으로 바꾸자 
    temp_data = dict(data)
    return temp_data


#사용자 정의 생 바꾸기 - callback
def  multi_color_func(word, 
                   font_size, 
                   position, 
                   orientation, 
                   random_state=None,
                   **kwargs):
    #hsl 은 명도 채도를 통해 색을 반환한다 
    #0~255까지 
    r = np.random.randint(low=100, high=255)
    g = np.random.randint(low=100, high=255)
    b = np.random.randint(low=100, high=255)
    
    return "rgb({}, {}, {})".format(r,g,b)


def make_WordCloud(temp_data):
    if temp_data==None or temp_data=="":
        file = open("temp_data.bin", "rb")
        temp_data = pickle.load(file)
        file.close()
        print(temp_data)

    image_name = input("이미지명은 ? ")
    mask = np.array(Image.open("./images/"+ image_name))
    wordcloud = WordCloud( font_path="c:/Windows/Fonts/malgun.ttf",
                        relative_scaling=0.2, background_color='white',
                        mask=mask).generate_from_frequencies(temp_data)

    wordcloud.recolor(color_func=multi_color_func, random_state=3)


    plt.figure(figsize=(16,8))

    plt.imshow(wordcloud, interpolation="bilinear")
    #plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")

    plt.axis("off")
    plt.show()

#pickle
import pickle 
def save_data(temp_data):
    file = open( "temp_data.bin", "wb")
    pickle.dump(temp_data, file)
    file.close()
    

if __name__=="__main__":
    
    #temp_data = createTokens()
    #save_data(temp_data)
    #파일읽기를 넣어놓는다 
    make_WordCloud("")



