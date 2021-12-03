import numpy as np
import pandas as pd

#1번
a=pd.DataFrame()
a['번호']=['1번','2번','3번']
a['이름']=['홍길동','전우치','강감찬']
a['생일']=[1975,'',1982]

print(a)

#2번
b=pd.read_excel("./부품구입대장.xlsx",header=3)
print(b.head())
print(b.info())

b2=b[['신청날짜','품목','수량','금액']]
b2.columns=['날짜','품목','수량','금액']
print(b2)

#3번
b3=b2[b2['금액']>100000]
print(b3.sort_values(by='금액',ascending=False))

#4번
b4=b3[['품목','금액']]
print(b4)

#5번
b2['코드']=''
b2.loc[b2['품목']=='백관','코드']='a1'
b2.loc[b2['품목']=='절연편','코드']='b1'
b2.loc[b2['품목']=='실리콘','코드']='c1'

print(b2)



