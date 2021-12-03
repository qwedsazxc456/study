import pandas as pd
# series(1),dataframe(2), pannel(3차원)-없어짐

member=pd.Series(["홍길동","강감찬","임꺽정","서희","허난설헌"])
#Series: S 대문자로 하기

print(type(member))
print(member)

#인덱싱과 슬라이싱을 지원한다.
print(member[0:2])
print(member[::-1])

print(member=="서희")
print(member[member=="서희"])

import numpy as np

a=np.array(["홍길동","강감찬","임꺽정","서희","허난설헌"])
print(a=="홍길동")

#numpy와 거의 유사하다. 차이는 인덱스를 별도로 부여할 수 있다.
member=pd.Series(["홍길동","강감찬","임꺽정","서희","허난설헌"],
                 index=["1번","2번","3번","4번","5번"])

print(member["1번"])
print(member["2번"])
print(member["3번"])
print(member["4번"])
print(member["1번":"3번"])

print(member[["1번","3번"]])

print(member[0])
print(member[2])
print(member[0:2])
print(member[::-1])

#dict 타입으로 시리즈 만들기
a={"홍길동":90, "임꺽정":80,"장길산":70,"강감찬":100}
b=pd.Series(a)
print(b)
print(b["홍길동"])
print(b[["홍길동","강감찬","임꺽정"]])

