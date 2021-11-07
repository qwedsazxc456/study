# csv(comma separate Value)
# -csv, 필드를 쉼표(,)로 구분한 테긋트 파일
# -엑셀 양식의 데이터를 프로그램에 상관없이 쓰기 위한 데이터 형식
# -notepad로 열림

# csv 객체로 csv 처리
# - Text파일 형태로 데이터 처리시 문장 내에 들어가 있는','등에 대해 전처리 과정이 필요
# - 파이썬에서는 간단히 csv파일을 처리하기 위해 csv파일 제공

import csv 
seoung_nam_data = [] 
header = [] 
rownum = 0 
with open("전국+유동인구+현황.csv","r", encoding="cp949") as p_file: 
    csv_data = csv.reader(p_file) #csv 객체를 이용해서 csv_data 읽기 
    for row in csv_data:    #읽어온 데이터를 한 줄씩 처리 
        if rownum == 0: 
            header = row #첫번째 줄은 데이터 필드로 따로 저장 
        location = row[7] 
        #“행정구역”필드 데이터 추출, 한글 처리로 유니코드 데이터를 cp949로 변환 
        if location.find(u"성남시") != -1: 
            seoung_nam_data.append(row) 
        #”행정구역” 데이터에 성남시가 들어가 있으면 seoung_nam_data List에 추가 rownum +=1 
with open("seoung_nam_floating_population_data.csv","w", encoding="utf8") as s_p_file:
    writer = csv.writer(s_p_file, delimiter='\t', quotechar="'", quoting=csv.QUOTE_ALL)
    # csv.writer를 사용해서 csv 파일 만들기 delimiter 필드 구분자
    # quotechar는 필드 각 데이터는 묶는 문자, quoting는 묶는 범위 
    writer.writerow(header) #제목 필드 파일에 쓰기 
    for row in seoung_nam_data:
        writer.writerow(row) 



        
# HTML
# - 웹 상의 정보를 구조적을 표현하기 위한 언어
# - 제목, 단락, 링크 등 요소 표시를 위해 Tag를 사용
# - 모든 요소들은 꺾쇠 괄호 안에
# - 트리구조

# 정규식
# - 복잡한 문자열 패턴을 정의하는 문자 표현 공식
# - 특정한 규칙을 가진 문자열의 집합을 추출

# 정규식 in 파이썬
# - re 모듈을 import 하여 사용
# - 함수: serrch - 한 개만 찾기, findall - 전체 찾기
# - 추출된 패턴은 tuple로 반환

import re

# XML
# - 데이터의 구조와 의미를 설명하는 TAG를 사용하여 표시하는 언어
# - HTML과 문법이 비슷, 대표적인 데이터 저장 방식

# 가장 많이 쓰이는 parser인 beautifulsoup

from bs4 import BeautifulSoup
with open("books.xml", "r", encoding="utf8") as books_file:
    books_xml = books_file.read()  
soup = BeautifulSoup(books_xml, "lxml") 
for book_info in soup.find_all("author"):
    print (book_info)
    print (book_info.get_text())

import urllib.request
from bs4 import BeautifulSoup
with open("US08621662-20140107.XML", "r", encoding="utf8") as patent_xml:
    xml = patent_xml.read()  
soup = BeautifulSoup(xml, "lxml") 
invention_title_tag = soup.find("invention-title")
print (invention_title_tag.get_text())

# json
# - java script의 데이터 객체 표현 방식

