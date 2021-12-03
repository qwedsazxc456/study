import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

t=pd.read_csv('./train_and_test2.csv')
t=pd.DataFrame(t)
input_data=t.iloc[:,1:4&12&21]
output_data=t.iloc[:,27]

X_train, X_test, y_train, y_test = train_test_split(
    input_data, output_data, random_state=0, train_size=0.7
)

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
for i in zip(y_test,y_pred):
    print(i)