import matplotlib.pyplot as plt 
import numpy as np

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

#화면 크기 조정
plt.figure(figsize=(9, 3))

#화면 분할 하기
#subplot 행,열,순서 ex)131 1*3으로 나누고 첫번째
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()