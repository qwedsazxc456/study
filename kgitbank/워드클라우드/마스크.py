from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
dir = path.dirname(__file__) #현재 디렉토리를 가져온다 

# Read the whole text.
print(path.join(dir, './txt/alice.txt')) #디렉토리 연결하기 
text = open(path.join(dir, './txt/alice.txt')).read()
print(text)

filename = path.join(dir, "./images/alice_color.png")
image = Image.open(filename) #이미지를 읽어서 
alice_mask = np.array(image) #ndarray 타입으로 전환하자 

image_colors=ImageColorGenerator(alice_mask)

stopwords=set(STOPWORDS)
stopwords.add('said')
stopwords.add('alice')

#워드 클라우드 객체를 따로 만들고 mask속성에 아까 읽어온 그림의 ndarray타입을 전달한다 
wc = WordCloud(background_color="black", max_words=2000, mask=alice_mask, 
               stopwords=stopwords)
wc.generate(text)
wc.recolor(color_func=image_colors)#색을 다시 한다
wc.to_file(path.join(dir, "alice.png")) #결과 저장
plt.imshow(wc, interpolation='bilinear') #화면출력
plt.show()