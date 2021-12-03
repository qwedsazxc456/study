import re
 
zipcode = input("우편번호를 입력하세요")
pattern = r'\d{5}$'
regex = re.compile(pattern)
result = regex.match(zipcode) #일치안하면 None반환 일치하면 match객체 반환
if result != None:
    print("형식이 일치합니다.")
else:
    print("잘못된 형식입니다.")