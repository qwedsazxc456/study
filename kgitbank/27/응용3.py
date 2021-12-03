
#차트가  seaborn 차트의 기본은  pyplot의 보충역할을 한다. 디자인적으로 + 가 있다 
#판다스 자체도  따로 차트가 있다. 세가지 섞여 있다. 
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html
#https://seaborn.pydata.org/tutorial.html
#https://matplotlib.org/

# pip install seaborn --upgrade  시본 차트 쓰려면 
# pip install --upgrade pip

import seaborn as sns              #pyplot보다 먼저 import 
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

sns.set(color_codes=True)
sns.set_theme(style="darkgrid")  #테마지정도 먼저{darkgrid, whitegrid, dark, white, ticks}

#한글 지정하기 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

iris = sns.load_dataset("iris")
print( iris.head() )

print(iris.species.value_counts()) #r의 table 

#종류별로 setosa(r), iris_virginica(g), vesicolor(b) 
iris_setosa=iris[iris.species =="setosa"]
iris_versicolor=iris[iris.species =="versicolor"]
iris_virginica=iris[iris.species =="virginica"]
print(iris_setosa.head() )
print(iris_versicolor.head()  )
print(iris_virginica.head()  )

plt.figure(figsize=(8,8))
plt.subplot(2,2,1)
xlabel = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
ylabel = ["sepal_width",  "petal_length", "petal_width", "sepal_length"]


for k in range(1,5):
    plt.subplot(2, 2, k)
    plt.plot(iris_setosa[xlabel[k-1]], iris_setosa[ylabel[k-1]], 'ro')
    plt.plot(iris_versicolor[xlabel[k-1]], iris_versicolor[ylabel[k-1]], 'yo')
    plt.plot(iris_virginica[xlabel[k-1]], iris_virginica[ylabel[k-1]], 'go')
    plt.xlabel( xlabel[k-1])
    plt.ylabel( ylabel[k-1])

plt.show()

#영역을 4개 쪼개서   sepal_length, sepal_width 
#영역을 4개 쪼개서   petal_length, petal_width 
#영역을 4개 쪼개서   petal_length, sepal_width 
#영역을 4개 쪼개서   sepal_length, petal_width 

sns.pairplot(iris, hue='species')
plt.show()

