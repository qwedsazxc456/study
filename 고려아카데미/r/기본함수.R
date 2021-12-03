head(exam) # 앞에서 부터 6개
head(exam, 10) # 앞에서부터 10개
tail(exam) # 뒤에서 부터
tail(exam, 10) # 

View(exam) # V대문자 주의
dim(exam) # 행,열
str(exam) # 데이터 속성 structure
summary(exam) # 요약 통계량

# mpg만 불러오기
mpg <- ggplot2::mpg