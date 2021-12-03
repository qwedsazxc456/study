import pandas as pd 
import numpy as np
from scipy.sparse.construct import random 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 

#.1데이터를 우선 읽어본다 
data = pd.read_csv("./data/중고자동차시세/train-data.csv")

print(data.head())
print( data.columns )

def initial_data(data):
    data = data.drop( columns=['Unnamed: 0', 'New_Price', 'Name', 'Location'], axis=1)
    # print(data.head())
    # print( data.columns )

    #Fuel_Type Transmission Owner_Type - 범주형 타입은 문자열을 범주형으로 전환시켜야 한다. 아직 안배웠음 

    #2. 단위가 들어가있는 데이터는 단위를 없애야 한다 
    #Mileage  kmpl 을 포함하지 않는건 NaN  으로 바꾸고 나서 

    #힌트 
    #np.logical_not -벡터연산수행   numpy와 pandas 는 파이썬이 아니다. 
    #print(  np.logical_not(data.Mileage.str.contains("kmpl") )  )

    data.Mileage[ np.logical_not(data.Mileage.str.contains("kmpl", na=False) ) ] = np.NaN 
    data.Power [ data.Power.str.contains("null", na=False)  ] = np.NaN 
    #데이터 자체에 NaN값이 있을때  True 또는 False 처리가 안되고 NaN 값을 반환한다 

    data.Mileage = data.Mileage.str.replace("kmpl", "").astype(float) #kmpl을 공백으로 
    data.Engine = data.Engine.str.replace("CC", "").astype(float) #CC을 공백으로 
    data.Power = data.Power.str.replace("bhp", "").astype(float) #bhp을 공백으로 


    #print(data.head())
    #print(data.isna().sum())
    #print( data.describe() )

    # #NaN값을 삭제할까 아니면 바꿀까?
    data = data.dropna(axis=0)
    #print( data.shape )
    #print( data.isna().sum() )
    #print( data.info() )
    return data 

    
#학습하기