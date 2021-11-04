

# 모듈과 패키지

# 모듈
# -파이썬의 Module == py 파일을 의미
# -같은 폴더에 Module에 해당하는 .py 파일과 사용하는 .py을 저장한 후 
# -import 문을 사용해서 Module을 호출

# 같은 폴더안에 있어야 한다
# __pycache__에 저장된다.

import fah_converter
fah_converter.convert_c_to_f

# namespace
# -모듈을 호출할때 범위 정하는방법
# -모듈 안에는 함수와 클래스등이 존재가능
# -필요한 내용만 골라서 호출할 수 있음
# -from 과 import 키워드를 사용함

# alias 설정하기 
import fah_converter as fah 
fah.convert_c_to_f

# 모듈에서 특정 함수 또는 클래스만 호출하기
from fah_converter import convert_c_to_f #
convert_c_to_f # fah 안써줘도 됨

# 모듈에서 모든 함수 또는 클래스를 호출하기
from fah_converter import *
convert_c_to_f



# Built-in Moduldes
# 1)구글에 물어본다
# 2)모듈을 import후 구글 검색 또는 Help
# 3)공식 문서를 읽어본다



# Package
# -하나의 대형프로젝트를 만드는 코드의묶음
# -다양한 모듈들의합, 폴더로 연결됨
# -__init__ , __main__ 등 키워드 파일명이 사용됨
# -다양한 오픈소스들이 모두 패키지로 관리됨

# 폴더별로__init__.py 구성하기
# -현재 폴더가 패키지임을 알리는 초기화 스크립트
# -없을 경우 패키지로 간주하지 않음(3.3+ 부터는X)
# -하위폴더와 py파일(모듈)을 모두 포함함
# -import와 __all__ keyword 사용

# 처음 init.py 파일에
# __all__ = ['image', 'sound', 'stage']
# from . import image
# from . import sound
# from . import stage

# 각각의 폴더의 init.py 파일에 import

# __main__.py 파일 만들기



# Python Virtual Environment 
# -프로젝트 진행시 필요한 패키지만 설치하는 환경
# -기본 인터프리터+ 프로젝트 종류별 패키지설치
# ex) 웹프로젝트, 데이터분석프로젝트
# 각각 패키지 관리할 수 있는 기능
# -다양한 패키지 관리도구를 사용함



# matplotlib
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()

