from sklearn.datasets import load_digits
digits = load_digits()  #숫자 0~9 까지인데  숫자 이미지도 
print(digits.data.shape)
print(digits.keys())

# import matplotlib.pyplot as plt 
# plt.gray() 
# plt.imshow(digits.images[2]) 
# plt.show() 

print(digits["target"][:20])
print(digits["data"][:2]) #흑백이미지를 -> ndarray 타입으로 전환  7:3으로 이웃을 3으로 했을때 적중률 구하기 

