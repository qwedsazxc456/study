import pandas as pd
data=pd.read_csv("C:/Users/Administrator/Desktop/수업/데이터분석/10차시_백현숙/uni_10/data/score_header.csv",header=3)

print(data)

print("컬럼명:",data.columns)
print("인덱스:",data.index)

#excel이 인코딩을 cp949를 사용한다. 한글 안깨지고 엑셀에서 열어보려면 cp949로 인코딩을 해야한다.
#index=False 옵션이 없으면 index까지 저장되면서 필드가 늘어난다.

data.to_csv("score_result1.csv", mode='w')
data.to_csv("score_result")