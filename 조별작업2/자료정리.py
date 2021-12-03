import pandas as pd
import numpy as np

train = pd.read_csv('./train_until_10t.csv')
lectures =  pd.read_csv('./lectures.csv')
questions = pd.read_csv('./questions.csv')

content_id=np.unique(train.loc[:,'content_id'])
lecture_id=np.unique(lectures.loc[:,'lecture_id'])
question_id=np.unique(questions.loc[:,'question_id'])

id_1=[]
id_2=[]

for i in lecture_id:
    for j in content_id[i == content_id].shape:
        if j == 1:
            id_1.append(content_id[i == content_id][0])     

for i in question_id:
    for j in content_id[i == content_id].shape:
        if j == 1:
            id_2.append(content_id[i == content_id][0])
        
print(id_1)   
         
print(id_2)

# 10000
questions[questions['question_id'] == 10000]