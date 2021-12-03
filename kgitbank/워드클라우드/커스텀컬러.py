from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS
dir = path.dirname(__file__) #현재 디렉토리를 가져온다 

#각 단어마다 색정보를 반환하는 함수를 만들어서 그 함수를 호출한다 
#함수 호출자가  WordCloud 클래스, 함수의 원형 (파라미터라든지 ) 결정되어 있어서 
#함수이름은 마음대로, 함수의 파라미터는 못바꾼다. - callback 함수
#색정보를 문자열의 형태로 hsl, rgb  방식 
import random  #파이썬이 제공하는 랜덤, numpy도 사용가능하다 

def grey_color_func(word, 
                   font_size, 
                   position, 
                   orientation, 
                   random_state=None,
                   **kwargs):
    #hsl 은 명도 채도를 통해 색을 반환한다 
    #60 ~ 100사이의 값
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)




# Read the whole text.
print(path.join(dir, './txt/alice.txt')) #디렉토리 연결하기 
text="""
동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 
무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세
남산위에 저소나무 철갑을 두른듯 바람서리 불변함은 우리기상일세
무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세
"""

f = open("./황선우.txt", "r", encoding="utf8")
text = f.read()

filename = path.join(dir, "./images/1.jpg")
image = Image.open(filename) #이미지를 읽어서 
alice_mask = np.array(image) #ndarray 타입으로 전환하자 


stopwords = set(STOPWORDS)
stopwords.add("said")
stopwords.add("alice")
stopwords.add("little")

#워드 클라우드 객체를 따로 만들고 mask속성에 아까 읽어온 그림의 ndarray타입을 전달한다 
wc = WordCloud(background_color="black", max_words=2000, mask=alice_mask, 
              stopwords=stopwords, font_path="c:/Windows/Fonts/malgun.ttf")
wc.generate(text)

wc.to_file(path.join(dir, "alice.png")) #결과 저장
plt.imshow(wc, interpolation='bilinear') #화면출력
plt.show()