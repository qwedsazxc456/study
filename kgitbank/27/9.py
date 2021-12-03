import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import pandas as pd 

#한글지원 2번째 방식 

#파이썬에서 지원하는 글꼴 목록 확인하기 
import matplotlib.font_manager as fm
font_list = [font.name for font in fm.fontManager.ttflist]
print(font_list)

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'


score = pd.read_csv("./score.csv")
print(score)

labels = score.name 
kor = score.kor
eng =  score.eng
mat =  score.mat 

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()

#width/3  x   x-중심축 
ax.bar(x - 3*width/3, kor, width, label='kor')
ax.bar(x, eng, width, label='eng')
ax.bar(x + 3*width/3, mat, width, label='mat')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.show()