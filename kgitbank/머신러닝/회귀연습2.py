import pandas as pd 
import numpy as np
from scipy.sparse.construct import random 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.read_csv("./중고자동차시세/train-data.csv")

print(data.columns)
print(data.head())

data=data.drop(columns=['Unnamed: 0', 'Name', 'Location','New_Price','Fuel_Type', 'Transmission', 'Owner_Type'],axis=1)

print(data['Mileage'].str.contains('kmpl',na=False))

data=data[data['Mileage'].str.contains('kmpl',na=False)]
data=data[data['Engine'].str.contains('CC',na=False)]
data=data[data['Power'].str.contains('bhp',na=False)]

print(data.columns)
print(data.head())

data.Mileage=data.Mileage.str.replace('kmpl','').astype(float)
data.Engine=data.Engine.str.replace('CC','').astype(float)
data.Power.replace('null bhp',np.nan, inplace=True)
data.Power=data.Power.str.replace('bhp','')
data.Seats.replace('',np.nan,inplace=True)
data.dropna(axis=0, inplace=True)
data.Power=data.Power.astype(float)

print(data.columns)
print(data.head())

print(data.info())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X=data.iloc[:,:6]
y=data.iloc[:,6]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, train_size=0.7)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print( model.score(X_train, y_train))
print( model.score(X_test, y_test))