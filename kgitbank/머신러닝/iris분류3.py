import pandas as pd
iris=pd.read_csv('./iris.csv')
iris=pd.DataFrame(iris)

from sklearn.model_selection import train_test_split 
input_data=iris.iloc[:,:4]
output_data=iris.loc[:,'variety']



X_train, X_test, y_train, y_test = train_test_split(
    input_data, output_data, random_state=0, train_size=0.7
)

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
for i in zip(y_test,y_pred):
    print(i)
   