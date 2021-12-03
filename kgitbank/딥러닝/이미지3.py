from sklearn.datasets import load_sample_images
import matplotlib.pyplot as plt
import PIL.Image as pilling
import numpy as np

# dataset = load_sample_images()
# print(len(dataset.images))
# img_rgb=dataset.images[0]
# print(img_rgb.shape)


img_rgb=np.array(pilling.open('./images/cat1.png'))


# pilling.fromarray(dataset.images[0]).save('./images/image1.png')
# pilling.fromarray(dataset.images[1]).save('./images/image2.png')

plt.figure(figsize=(20,5))
plt.subplot(1,4,1)
plt.imshow(img_rgb[50:500,50:500,:])
plt.axis('off')
plt.title('RGB Image')

plt.subplot(1,4,2)
plt.imshow(img_rgb[50:500,50:500,0])
plt.axis('off')
plt.title('RGB Image')

plt.subplot(1,4,3)
plt.imshow(img_rgb[50:500,50:500,1])
plt.axis('off')
plt.title('RGB Image')

plt.subplot(1,4,4)
plt.imshow(img_rgb[50:500,50:500,2])
plt.axis('off')
plt.title('RGB Image')

plt.show()
