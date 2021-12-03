# import requests
# url='http://www.naver.com'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
# res=requests.get(url, headers=headers)
# with open('naver.html','w',encoding='utf8') as f:f.write(res.text)


#-------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

# url='https://comic.naver.com/webtoon/weekday'
# res=requests.get(url)
# res.raise_for_status #정상적으로 되지않을경우 멈춤

# soup=BeautifulSoup(res.text,'lxml')


# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.attrs) #a element의 속성정보
# print(soup.a['href']) #a element의 href

# print(soup.find('a',attrs={'class':'Nbtn_upload'}))
# print(soup.find(attrs={'class':'Nbtn_upload'}))

# print(soup.find('li',attrs={'class':'rank01'}))
# rank1=(soup.find('li',attrs={'class':'rank01'}))
# print(rank1.a)

# rank2=rank1.next_sibling.next_sibling
# rank3=rank2.next_sibling.next_sibling
# rank2=rank3.previous_sibling.previous_sibling

# print(rank1.parent)

# rank2=rank1.find_next_sibling('li')
# print(rank2.a.get_text())
# rank3=rank2.find_next_sibling('li')
# print(rank3.a.get_text())
# rank2=rank3.find_previous_sibling('li')
# print(rank2.a.get_text())

# print(rank1.find_next_siblings('li'))

# webtoon=soup.find('a',text='약한영웅-157화')
# print(webtoon)

#----------------------------------------------------------------

#네이버 웹툰 전체 목록
# cartoons=soup.find_all('a', attrs={'class':'title'})
# for cartoon in cartoons:
#     print(cartoon.get_text())
    
#--------------------------------------------------------------

url='https://comic.naver.com/webtoon/list?titleId=758037&weekday=mon'
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,'lxml')
cartoons=soup.find_all('td',attrs={'class':'title'})
# title=cartoons[0].a.get_text()
# link=cartoons[0].a['href']
# print(title)
# print('https://comic.naver.com'+link)

for cartoon in cartoons:
    title=cartoon.a.get_text() 
    link='https://comic.naver.com'+cartoon.a['href']
    print(title,link)
    
