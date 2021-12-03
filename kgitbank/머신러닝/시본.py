import seaborn as sns              #pyplot보다 먼저 import 
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

sns.set(color_codes=True)
sns.set_theme(style="darkgrid")  #테마지정도 먼저{darkgrid, whitegrid, dark, white, ticks}

#한글 지정하기 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

mpg = sns.load_dataset("mpg")
print(mpg.head())

sns.pairplot(mpg) #시본에서 제공하는 산포도 행렬 
plt.show()