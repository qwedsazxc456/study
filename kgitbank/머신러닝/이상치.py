import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

titanic = pd.read_csv("./data/train_and_test2.csv")
#필요없는 컬럼을 지우자 , 엑셀가서 지우고 와도 된다.
titanic= titanic.drop(columns=["Passengerid"], axis=0)#컬럼 삭제후 

#확인중 
print( titanic.shape )
print( titanic.columns )

#1.결측치를 찾아서 처리하자 
print( titanic.isna().sum()) #결측치 확인
#각 필드별로 결측치가 많았다면 fillna 함수를 이용해서 평균값이나 중앙값 또는 최빈값으로 대체를 한다 
#한필드에 na 두개 있었음 삭제를 선택

titanic = titanic.dropna(axis=1) #두개밖에 안되니까 행을 삭제

print( titanic.isna().sum())#결측치 확인
print(titanic.shape)#데이터개수 확인 

#2.이상치제거 
#이상치를 확인 효과적인 차트가 boxplot
titanic.boxplot() #데이터프레임 자체에 왠만한 차트 
plt.show()

def outfliers_iqr(data):
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3-q1 #3/4 분위수 - 1/4분위수  
    
    lower_bound = q1 - (iqr*1.5)
    upper_bound = q3 + (iqr*1.5) 

    return lower_bound, upper_bound

print( outfliers_iqr(titanic.Fare)) #(-27.172999999999995, 66.34379999999999)

lower, upper = outfliers_iqr(titanic.Fare)
titanic.Fare[ titanic.Fare < lower] = lower 
titanic.Fare[ titanic.Fare > upper] = upper 

titanic.boxplot() #데이터프레임 자체에 왠만한 차트 
plt.show()

# historgram -  데이터의 분포도 확인
# boxplot - 이상치제거
# scatterplot(산포도) - 데이터의 데이터의 관계