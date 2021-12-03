import requests  #이 라이브러리가 브라우저처럼 
                 #서버로 정보를 전송하고 그 결과를 받는 라이브러리 
                 #웹서버에 있는 문서를 불러온다 
                 #ajax 통신과 open api(구글, 카카오톡, 공공포탈(www.data.go.kr), https://www.kaggle.com/)
from bs4 import BeautifulSoup
                 #html로 부터 값만 추출하기 위한 파서, ajax 의 경우에는 json 형태의 문자열로 온다 
                 #그래스 dict객체 = json.load(문자열) 
import json 
url="https://finance.daum.net/api/market_index/days"
#"https://finance.daum.net/api/market_index/days?page=1&perPage=10&market=KOSDAQ&pagination=true"

# fieldName=changeRate&order=desc&perPage=10&symbolCode=D0011001&market=KOSPI&intervalType=TODAY
# &changeType=RISE
#물음표 뒤에부터가 부가적인 정보로 파라미터라고 부른다 
#"?symbolCode=US.COMP&page=1&perPage=10&pagination=true
#?키1=값1&키2=값2&키3=값3
#{"키1":"값1", "키2":"값2", "키3":"값3"}

info ={"page":1, "perPage":"10", "market":"KOSDAQ", "pagination":"true"}

#마치 브라우저로 접근한듯한 
customer_header = {
    "referer":"https://finance.daum.net/",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


#상승종목
#서버로 가서 정보를 읽어온다 

import pandas as pd 

dfList=pd.DataFrame()

for i in range(1,30):
    info["page"]=i
    response = requests.get(url, params=info, headers=customer_header)
    if response.status_code==200: #성공적일때 
        data = json.loads(response.content ) #bytes 배열을 -> dict 타입으로 전환 
        print( data )
        dataList = data["data"]
        for item in dataList:
            dfList= dfList.append( item, ignore_index=True )

print( dfList )

dfList.to_csv("일간주식.csv", encoding="cp949", index=False)