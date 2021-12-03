import pandas as pd

data1={'kor':90,'eng':70, 'mat':80}
data2={'kor':99,'eng':75, 'mat':70}
data3={'kor':85,'eng':80, 'mat':60}

data=pd.DataFrame() #비어있는 Dataframe 객체만들기

data=data.append(data1,ignore_index=True) #데이터추가
data=data.append(data2,ignore_index=True) #데이터추가
data=data.append(data3,ignore_index=True) #데이터추가
data=data.append({'kor':100,'eng':100,'mat':100},ignore_index=True) #데이터추가

print(data)

data['total']=data['kor']+data['eng']+data['mat']
data['total2']=data.kor+data.eng+data.mat
data['avg']=data.total/3

print(data)

#특정 필드 삭제 : 