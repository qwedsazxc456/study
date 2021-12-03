import numpy as np 
import os 
import random 
import PIL.Image as pilimg 
import imghdr
import pandas as pd 


#데이터 만드는 수 
def makeData(folder, label):
    path = "./archive/PetImages/" + folder
    data = []
    labels = []
    #고양이 사진을 읽어서 넘파이 바꾸고 
    i=1 
    for filename in os.listdir(path):
        if i%1000==0:
            print(i)
        i += 1
        try: 
            #print(filename)
            kind = imghdr.what(path + "/" + filename)
            #print(kind)
            if kind in ["gif", "png", "jpeg", "jpg"]:
                img = pilimg.open(path + "/" + filename) #이미지 크기가 다 달라서 이미지 크기를 변형한다 
                resize_img = img.resize( (150, 150 )) 
                pixel = np.array(resize_img) #이미지가 -> ndarray타입으로 전환된다. 
                if pixel.shape==(150, 150, 3):
                    data.append(pixel)
                    labels.append(label) #고양이를 0 으로 본다 
        except:
            print(filename + " error ")

    #print( data )
    np.savez("imagedata{}.npz".format(label), data=data, targets=labels)
    print("파일저장완료")

makeData("Cat", 0)
makeData("Dog", 1)

a = np.load("imagedata0.npz")
b = np.load("imagedata1.npz")


data1 = a["data"]
target1 = a["targets"]

data2 = b["data"]
target2 = b["targets"]

data = np.concatenate((data1, data2), axis=0)
print(data.shape)

target =np.concatenate((target1,target2), axis=0)
print(target.shape)
