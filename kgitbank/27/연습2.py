
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


sns.set_theme(style="whitegrid")  #테마지정도 먼저 

#한글 지정하기 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

score = pd.read_csv("./score.csv")

#파이썬은 데이타 프레임 자체에 차트가 있어서   pandas  chart 
score.plot.bar()

# print(score)

# # Draw a nested barplot by species and sex
# g = sns.catplot(
#     data=score, kind="bar",
#     x="name", y="kor", hue="kor",
#     ci="sd", palette="dark", alpha=.6, height=6
# )
# g.despine(left=True)
# g.set_axis_labels("", "한글을 지원해보자")
# #g.legend.set_title("")

plt.show()