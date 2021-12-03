# pip install seaborn --upgrade  시본 차트 쓰려면 
# pip install --upgrade pip
import seaborn as sns              #pyplot보다 먼저 import 
import matplotlib.pyplot as plt
import pandas as pd

sns.set_theme(style="whitegrid")  #테마지정도 먼저 

#한글 지정하기 
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

penguins = sns.load_dataset("penguins")
penguins.head()
penguins.info()
penguins.describe()

# Draw a nested barplot by species and sex
g = sns.catplot(
    data=penguins, kind="bar",
    x="species", y="body_mass_g", hue="sex",
    ci="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("", "한글을 지원해보자")
g.legend.set_title("")

plt.show()