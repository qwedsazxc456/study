import pandas as pd, numpy as np

questions = pd.read_csv('./questions.csv')
data = pd.read_csv('./train_until_1m_a.csv')

def make_part(data, questions):
    data['part'] = np.nan

    for num in range(len(data)):
        if data.loc[num, 'content_id'] in questions['question_id']:
            data.loc[num, 'part'] = questions.loc[questions[questions['question_id']==data.loc[num, 'content_id']].index, 'part'].values
            print(num)
    
    return data

new_data = make_part(data, questions)
new_data.to_csv('train_until_1m_part_a.csv', index=False)