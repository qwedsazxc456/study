import pandas as pd

diamond=pd.read_csv('./diamonds.csv')
y=diamond.loc[:,'cut']
X=diamond.drop('cut', axis=1)
diamond=pd.get_dummies(diamond)

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()
model.fit(X,y)
print(model.score(X,y))