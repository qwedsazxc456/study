# 예상 가능한 예외
# -발생 여부를 사전에 인지할 수 있는 예외
# -사용자의 잘못된 입력, 파일 호출 시 파일 없음
# -개발자가 반드시 명시 해야함

# 예상 불가능한 예외
# - 인터프리터 과정에서 발생하는 예외, 개발자 실수
# - 리스트의 범위를 넘어가는 값 호출, 정수 0으로 나무
# - 수행 불가시 인터프리터가 자동 호출

# 파이썬의 예외 처리
# try~ except 문법
# try:
#     예외 발생 가능 코드
# except <Exception Type>:
#     예외 발생시 대응하는 코드
# if~ else로 가능

# 0으로 나눌때 예외 처리
for i in range(10):
    try:
        print(10/i)
    except ZeroDivisionError:
        print('Error')
        print('Not divided by 0')
# 다른 에러가 들어가 있다면 except 안된다

a = [1,2,3,4,5]
for i in range(10):
    try:
        print(i, 10//i)
        print(a[i])
    except ZeroDivisionError:
        print('Error')
        print('Not divided by 0')   
    except IndexError as e:
        print(e)
    except Exception as e: # 특별한거 지정하지 않아도 모두 / 권장하지는 않음 - 어떤 에러인지 알 수 없음
        print(e)    

# try ~ except ~ else
for i in range(10):
    try:
        result = 10//i
    except ZeroDivisionError:
        print('Not divided by 0')
    else:
        print(10//i)
        
# try ~ except ~ finally
# finally - 예외 발생 여부와 상관없이 실행됨



# raise
# -필요에 따라 강제로 Exception 발생
while True:
    value = input('정수값')
    for digit in value:
        if digit not in '0123456789':
            raise ValueError('숫자값을 입력하지 않으셨습니다')
    print('정수값-', int(value))

# assert 
# -특정 조건에 만족하지 않을 경우 예외 발생
# assert 예외조건




# 파일의 종류
# Binary
# -컴퓨터만 이해할 수 있는 형태인 이진형식으로 저장된 파일
# -메로장으로 열면 내용이 깨져 보임
# -엑셀파일, 워드 파일 등등
# Text
# -인간도 이해할 수 있는 문자열 형식
# -메모장으로 확인 가능
# -메모장, HTML파일, 파이썬 코드

# 파이썬은 파일 처리를 위해 'open'키워드 사용
f = open('i_have_a_dream.txt','r')
contents = f.read()
print(contents)
f.close

# with 구문과 함께 사용하기
with open('i_have_a_dream.txt','r') as my_file:
    contents = my_file.read()
    print(type(contents), contents)

# 한줄씩 읽어오기 - readlines 사용

# File Write
# mode는 'w' , encoding='utf8'
# mode 'a'는 append 기존 파일에 추가



# os module
import os
 
os.mkdir('log') # 폴더 만들기

try:
    os.mkdir('abc')
except:
    print('Already created')
    
# os.path.exists('abc') # 폴더나 파일 존재하는지 확인
# os.path.isfile() # 파일확인

import shutil

source = 'i_have_a_dream.txt'
dest  = os.path.join('abc','1.txt')
shutil.copy(source, dest)  

# pathlib 모듈 사용 - path를 객체로 다룸
import pathlib
print(pathlib.Path.cwd())
cwd=pathlib.Path.cwd()
print(cwd.parent)
print(cwd.parent.parent)
print(list(cwd.parents))
print(list(cwd.glob('*')))



# Pickle
# - 파이썬의 객체를 영속화하는 built-in 객체
# - 데이터, object등 실행중 정보를 저장 -> 불러와서 사용
# - 저장해야하는 정보, 계산 결과등 활용이 많음

import pickle
#저장
f=open('list.pickle', 'wb') # wb는 이진으로 저장 / write binary?
test = [1,2,3,4,5]
pickle.dump(test, f) # test를 f에 저장
f.close()

#불러오기
f = open('list.pickle', 'rb') # read binary?
test_pickle = pickle.load(f)
print(test_pickle)
f.close

# class도 저장가능



# 로그 남기기
# - 프로그램이 실행되는 동안 일어나는 정보를 기록을 남기기
# - 유저의 접근, 프로그램의 Exception , 특정 함수의 사용
# - Console 화면에 출력, 파일에 남기기, DB에 남기기
# - 기록된 로그를 분석하여 의미있는 결과를 도출 할 수 있음
# - 실행시점에서 남겨야 하는 기록, 개발시점에서 남겨야하는 기록

# print / logging
# -기록을 print로 남기는 것도 가능
# -그러나 Console 창에만 남기는 기록은 분석시 사용불가
# -때로는 레벨(개발, 운영)별로 기록을 남길 필요도 있음
# -모듈별로 별도의 logging을 남길 필요도 있음
# -이러한 기능을 체계적으로 지원하는 모듈이 필요함

# logging 모듈
import logging

logging.debug('틀림')
logging.info('확인')
logging.warning('조심')
logging.error('에러')
logging.critical('프로그램 끝..?')

# DEBUG / INFO / WARNING / ERROR / CRITICAL 보통 WARNING 부터 사용자가 확인
# WARNING 부터 나온다

# configparser

# argparser
