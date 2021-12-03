import pandas as pd
import matplotlib.pyplot as plt

train=pd.read_csv('./타이타닉/train.csv')
test=pd.read_csv('./타이타닉/test.csv')

print(train.columns)
print(test.columns)

train['Cabin']=train['Cabin'].fillna('?')
test['Cabin']=test['Cabin'].fillna('?')
train['Cabin']=train['Cabin'].str[0]
test['Cabin']=test['Cabin'].str[0]

index=train[train['Cabin']=='T'].index
train=train.drop(index, axis=0)

train=train.dropna(axis=0)
test=test.dropna(axis=0)

from CommonUtil import outfliers_iqr
lower, upper = outfliers_iqr(train.Fare)
train.Fare[ train.Fare < lower] = lower 
train.Fare[ train.Fare > upper] = upper 
test.Fare[ test.Fare < lower] = lower 
test.Fare[ test.Fare > upper] = upper 

X_train=train.drop(['Survived','PassengerId','Name','Ticket'], axis=1)
test=test.drop(['PassengerId','Name','Ticket'], axis=1)
y_train=train.loc[:,'Survived']

X_train=pd.get_dummies(X_train)
X_test=pd.get_dummies(test)

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()
scaler.fit(X_train)
X_train_scaled=scaler.transform(X_train)
scaler.fit(X_test)
X_test_scaled=scaler.transform(X_test)


from sklearn.linear_model import LogisticRegression

model=LogisticRegression()
model.fit(X_train_scaled,y_train)
print(model.score(X_train_scaled,y_train))

y_pred = model.predict(X_test_scaled)
print(model.score(X_test_scaled,y_pred))