import numpy as np
samples= ['The cat sat on the mat',
         'The dog ate my homework',
         'The cat is very cute',
         'The fox if very smart and very beatiful and follow people well']

#원핫해싱은 단어와 단어의 관계를 벡터로 저장(거리로 측정)
dimensionality=1000
max_length=10
results=np.zeros((len(samples),max_length,dimensionality))
print(results.shape)
print(results)

for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        index=abs(hash(word))%dimensionality
        results[i,j,index]=1
        
print(results)