from scipy import misc

img_gray=misc.face(gray=True)
print(type(img_gray))

import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(img_gray[:20,:20],
            annot=True, #숫자형태
            fmt='d', #정수형태
            cmap=plt.cm.bone)
plt.axis('off')
plt.show()

sns.heatmap(img_gray[:20, :20], cmap='RdYlGn_r')
plt.title('colormap of cmap=RdYlGn_r', fontsize=20)
plt.show()



