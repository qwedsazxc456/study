#url이랑 파라미터 값 통해서 각 연도별 데이터 가져오는 함수

import requests
import json
import pandas as pd

def get_data(year, url, info):
        info['searchYear'] = year

        response = requests.get(url, params=info)
        data = json.loads(response.content)
        
        info['numOfRows'] = data['totalCount']

        response = requests.get(url, params=info)
        data = json.loads(response.content)

        result = pd.DataFrame(data['items']['item'])

        return result

#url과 파라미터 값, 그리고 for문으로 get_data함수 통해서 데이터 가져와서 저장하는 코드

url = 'http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath'
info = {'ServiceKey': 'Key', #key값에 개인이 받은 키값
        'searchYear': '', 'siDo': '', 'guGun': '', 'type': 'json', 'numOfRows': '1', 'pageNo': '1'}

accident = pd.DataFrame()
for year in range(2012, 2021):
        result = get_data(year, url, info)
        accident = pd.concat([accident, result], ignore_index=True)

accident.to_csv('accident.csv', index=False)

