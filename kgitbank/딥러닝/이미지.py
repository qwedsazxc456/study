import PIL.Image as pilling
import numpy as np

#image읽기
im=pilling.open('./images/cat1.png')

#image 출력
im.show()

#image -> ndarray
pix=np.array(im)

print(pix)
print(pix.shape)
for i in range(0, pix.shape[0]):
    for j in range(0, pix.shape[1]):
        print('{0}'.format(pix[i,j]), end=' ')
    print()    