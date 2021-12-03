
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

sns.set(color_codes=True)
sns.set_theme(style="darkgrid")  #테마지정도 먼저{darkgrid, whitegrid, dark, white, ticks}

#한글 지정하기 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

plt.plot([1,2,3,4])

plt.show()