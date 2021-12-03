#1. 뉴스 목록 가져오기 
import requests   #웹으로부터 문서를 불러온다. 
from bs4 import BeautifulSoup #불러온 문서를 html 태그들로부터 텍스트를 분리하는 파싱을 담당한다 

#브라우저는 자기 정보를 갖고 가는데 , 사파리, 크롬  
#어플리케이션에서 그냥 요청하면 브라우저 정보를 안갖고 가서 막힌다. 

#보안이 걸릴경우 - 속여야 한다 
#정상적인 웹브라우저를 통해서 접근한 것처럼 속인다. 
customer_header = {
    "referer":"https://news.naver.com/main/read.naver",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

"""
https://search.naver.com/search.naver?
where=news&sm=tab_pge&query=%EB%B0%B1%EC%8B%A0&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=37&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=41
"""
#params={"where":"news", } ........

keyword="배구"
"""
1 - 1    (page-1)*10 + 1   (1-1)*10+1 = 1
2 - 11   (2-1)*10 +1        11
3 - 21   (3-1)*10 +1        21  
4 - 31   (4-1)*10 +1        31
5 - 41   (5-1)*10+1        = 41
""" 
def getList(keyword="배구", page_cnt=5, filename="네이버뉴스1.txt"):

#for문 안돌리고 파일에 저장도 안됨 
    file = open(filename, "w", encoding="utf8")
    page=1 
    for page in range(1, page_cnt+1):
        url="https://search.naver.com/search.naver?where=news&sm=tab_pge&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=28&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all"
        url=url+"&query=" + keyword 
        url=url+"&start=" + str((page-1)*10 + 1) 
        print(url)
        response = requests.get(url, headers=customer_header) 
        #request 객체의 get 메서드는 url하고 headers 해당 문서를 불러와서 문서에 대한 정보를 반환한다 
        if response.status_code==200: #status_code 필드에 정보의 전달상황이 저장 200-정보가 정상적으로 왔음을 나타낸다 
            contents = response.content #실제로 문서가 온다 
            soup = BeautifulSoup(contents, 'html.parser') #html과 태그를 분리해서 트리형태로 파싱가능하도록 객체를 반환한다 
            
            alinkList = soup.find_all("a",class_="sub_txt")  #앵커태그 가져옴 find_all 함수는 list 형태로 반환한다 
            title, contents = getDetail(alinkList)
            print(page)
            file.write(title)
            file.write(contents)

    #for문 종료하고나서 
    file.close()      

        # for link in alinkList:
        #     print( link['href'] )

def getDetail(alinkList):
    alltitles=""
    allcontents="" 
    for link in alinkList:
        print(link['href'])
        if "https://news.naver.com/main" in link['href']:
            response = requests.get(link['href'], headers=customer_header) 
            #가짜 헤더 정보를 붙여서 보내야 한다 
            if response.status_code==200:
                soup = BeautifulSoup(response.content, 'html.parser')
                #print(response.content )
                title = soup.find("h3", id="articleTitle")
                if title!=None:
                    alltitles = alltitles + title.text
                contents = soup.find("div", id="articleBodyContents")
                if contents !=None:
                    allcontents = allcontents + contents.text 
                #print(contents.text)
    return alltitles, allcontents  



from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator 


def createWordCloud(filename):
    dir = path.dirname(__file__) #현재 디렉토리를 가져온다 

    # Read the whole text.
    text = open(path.join(dir, filename), "r", encoding="utf8").read()
    #print(text)

    filename = path.join(dir, "./images/stormtrooper_mask.png")
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

    wc.to_file(path.join(dir, "네이버뉴스.png")) #결과 저장
    plt.imshow(wc, interpolation='bilinear') #화면출력
    plt.show() 


if __name__ =="__main__":
    keyword=input("검색 키워드 : ")
    page_cnt = int(input("페이지 카운트 : "))
    filename = input("파일명 ")

    getList(keyword, page_cnt, filename)
    createWordCloud(filename) #이 함수 만들기 


