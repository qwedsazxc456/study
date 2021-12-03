import numpy as np

#데이터를 파일로 부터 읽었을때 데이터가 없으면 자동으로 nan으로 잡힌다.
#데이터가 없는 경우 처리를 하기위해서 필요하다.

a=[1,2,3,np.nan,5]

print(np.isnan(a))