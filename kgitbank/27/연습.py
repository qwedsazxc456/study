import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 


score = pd.read_csv("./score.csv")
print(score)

score['total'] = score.kor + score.eng + score.mat 
score['avg']=score['total']/3

print(score)

#한글지원 1
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="./fonts/BSSYM7.TTF").get_name()
rc('font', family=font_name)


# Fixing random state for reproducibility
np.random.seed(19680801)

#plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people =score.name
y_pos = np.arange(len(people))
performance = score.avg

ax.barh(y_pos, performance, align='center', color="red")
ax.set_yticks(y_pos) # 눈금 
ax.set_yticklabels(people) #눈금의 제목

ax.invert_yaxis()  #y축 데이터를 뒤집어서
ax.set_xlabel('실적')
ax.set_title('오늘 최고의 실적은?')

plt.show()