#원핫인코딩 단어를 수치화 한다
import numpy as np
samples= ['The cat sat on the mat',
         'The dog ate my homework',
         'The cat is very cute',
         'The fox if very smart and very beatiful and follow people well']

token_index={}
for sample in samples:
    token=sample.split()
    print(token)
    for word in token:
        if word not in token_index:
            token_index[word]=len(token_index)+1

print(token_index)

#한 문장을 열개의 단어 구성으로 생각
max_length=10

#문장 하나당 2차원 형태
results=np.zeros((len(samples), max_length, max(token_index.values())+1))

print(results.shape)
print(results)

for i, sample in enumerate(samples):
    for j, word in list( enumerate(sample.split()))[:max_length]:
        index = token_index.get(word)
        results[i,j,index]=1
        
print(results)