import pandas as pd

lectures = pd.read_csv('./lectures.csv')
questions = pd.read_csv('./questions.csv')
data = pd.read_csv('./train_until_1m_d.csv')

def make_haveInfo(data):
    lecture_id = lectures['lecture_id']
    question_id = questions['question_id']

    train_new = pd.DataFrame()
    for num in range(len(data)):
        if data.iloc[num, 3] in lecture_id | question_id:
            train_new = train_new.append(data.iloc[num, :], ignore_index=True)
        print(num)
    
    return train_new

data_new_haveInfo = make_haveInfo(data)
print(data_new_haveInfo.shape)
data_new_haveInfo.to_csv('train_until_1m_haveInfo_d.csv', index=False)