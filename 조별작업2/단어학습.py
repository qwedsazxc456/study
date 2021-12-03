import pandas as pd
import random
import time

words = pd.read_csv('./words_1stWeek.csv')
wordsList = []

def study(wordsList):
    while(True):
        temp = random.sample(range(900), 1)
        isSame = False
        for num in temp:
            if num in wordsList:
                isSame = True
        if isSame == False:
            break

    wordsList += temp

    for num in wordsList[-1:]:
        print(words.loc[num, :].values[0] + '\t\t' + words.loc[num, :].values[1])
    input('단어를 외운 뒤 엔터 키를 눌러주세요.')
    print('\n' * 50)
    random.shuffle(wordsList)
    for num in wordsList:
        print(words.loc[num, :].values[0] + '\t\t', end='')
        answer = input()
        if answer.replace(' ', '') in words.loc[num, :].values[1].replace(' ', '').replace('…', '').split(','):
            print('정답입니다.')
        else:
            print(f'오답입니다. 해당 단어의 뜻은 {words.loc[num, :].values[1]} 입니다.')

def test():
    print('\n' * 50)
    result = pd.DataFrame(columns=['Words', 'Answered_correctly'])
    random.shuffle(wordsList)
    for num in wordsList:
        print(words.loc[num, :].values[0] + '\t\t', end='')
        answer = input()
        if answer.replace(' ', '') in words.loc[num, :].values[1].replace(' ', '').replace('…', '').split(','):
            result.loc[len(result)] = [words.loc[num, :].values[0], 1]
        else:
            result.loc[len(result)] = [words.loc[num, :].values[0], 0]
    now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    result.to_csv(f'{now}.csv', index=False, encoding='utf-8')

if __name__ == '__main__':
    while(True):
        print('1. 단어 학습')
        print('0. 테스트 후 저장하고 종료')

        sel = input('선택: ')
        if sel == '1':
            study(wordsList)
        elif sel == '0':
            test()
            break
        else:
            continue