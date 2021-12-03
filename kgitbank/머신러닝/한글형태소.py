#pip install konlpy -- 반드시 관리자 권한으로 

#konlpy   오류생길때 
#주의사항 - 자바와 버전이 맞아야 한다 
#https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype
#위 경로에서 본인 버전에 맞는 jpype 를 다운받는다 
#python 버전 맞추기 python --version 확인하기 
#JPype1-1.1.2-cp38-cp38-win_amd64.whl
#cd C:\Users\user\Downloads  
#C:\Users\user\Downloads/> pip install JPype1-1.1.2-cp38-cp38-win_amd64.whl

from konlpy.tag import Kkma
from konlpy.utils import pprint
text="""
동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라만세 
무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세
남산위에 저소나무 철갑을 두른듯 바람서리 불변함은 우리기상일세
무궁화 삼천리 화려강산 대한사람 대한으로 길이 보전하세
"""
kkma = Kkma()
# print(kkma.sentences(text)) #문장
# print(kkma.nouns(text)) #명사 

from konlpy.tag import Hannanum
hannanum = Hannanum()
print(hannanum.nouns(text))

#Twitter -> Okt(젤 많이 사용한다 )
from konlpy.tag import Okt  
okt = Okt()
print( okt.nouns(text))

#말뭉치 가져오기 
from konlpy.corpus import kolaw #한국법률 말뭉치
fids = kolaw.fileids()
print(fids)
fobj = kolaw.open(fids[0])
constitution=fobj.read()
print(constitution)

from konlpy.corpus import kobill 
fids = kobill.fileids()
print(fids)
i=1
for filename in fids:
    file = kobill.open(filename)
    text=file.read()
    print(text)
    i+=1
    if i>=10:
        break


from os import path
from wordcloud import WordCloud
from matplotlib import font_manager, rc, matplotlib_fname
import matplotlib.pyplot as plt


#font_path 가 절대경로로 지정했음, 상대경로로도 가능하다 
wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf").generate(constitution)
wordcloud.to_file("result1.png")

#pyplot 이 이미지 출력을 한다. imshow 이미지 출력함수 
plt.imshow(wordcloud)
plt.show()
