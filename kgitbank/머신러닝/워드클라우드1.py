#기본 워드 클라우드 

#pip install wordcloud 
#혹시 설치 안되면 자바 설치하고 할것 
#pip install konlpy 
#pip install pytagcloud 
#pip install pygame 
#pip install simplejson 

nouns = list()

nouns.extend(['korea' for t in range(50)])
nouns.extend(['school' for t in range(100)])
nouns.extend(['vanila' for t in range(50)])
nouns.extend(['icecream' for t in range(500)])
nouns.extend(['chocolate' for t in range(250)])
nouns.extend(['chococake' for t in range(700)])
nouns.extend(['python' for t in range(40)])
nouns.extend(['java' for t in range(40)])
nouns.extend(['chococake' for t in range(240)])
nouns.extend(['cookie' for t in range(140)])
nouns.extend(['rain' for t in range(200)])
nouns.extend(['mintchoco' for t in range(80)])
nouns.extend(['strawberry' for t in range(40)])
nouns.extend(['peach' for t in range(140)])
nouns.extend(['lion' for t in range(140)])
nouns.extend(['tiger' for t in range(270)])
nouns.extend(['elephant' for t in range(240)])
nouns.extend(['crown' for t in range(450)])
nouns.extend(['mango' for t in range(400)])
nouns.extend(['apple' for t in range(340)])
nouns.extend(['rabbit' for t in range(240)])
nouns.extend(['alice' for t in range(270)])
nouns.extend(['icecreamcake' for t in range(390)])
nouns.extend(['머신러닝' for t in range(390)])
nouns.extend(['딥러닝' for t in range(390)])
nouns.extend(['지도학습' for t in range(390)])
nouns.extend(['비지도학습' for t in range(390)])
nouns.extend(['강화학습' for t in range(390)])
nouns.extend(['라쏘' for t in range(390)])
nouns.extend(['퍼셉트론' for t in range(390)])
nouns.extend(['시그모이드' for t in range(390)])
nouns.extend(['relu' for t in range(390)])
nouns.extend(['소프트맥스' for t in range(390)])

print(nouns[1:20])

from collections import Counter #list 형태로 단어 묶음 주면 단어와 단어개수를 반환한다  
import pytagcloud 
import webbrowser 

word_count = Counter(nouns)
print( type(word_count) )
print( word_count)

#Counter  객체에  most_common  이 함수는 최대한 빈도수 많은거를 내림차순해서 원하는 개수만큼 가져온다 

tag = word_count.most_common(50)

#워드 클라우드 표에 그려질 그래픽 표시로 바꾼다 
#글자색정보, 글자크기, 표현할 단어 

taglist = pytagcloud.make_tags(tag, maxsize=50)
print(taglist)

#워드클라우드 차트 그려서 firstwordcloud.jpg로 저장 
pytagcloud.create_tag_image( taglist, 
   "firstwordcloud.jpg", fontname="korea1",
   size=(800, 500),
   rectangular=True) #True면 사각형으로 만든다. 

#저장한 그림 화면에 뿌리기 - 웹브라우저 이용
webbrowser.open( "firstwordcloud.jpg" )

#이게 끝임 