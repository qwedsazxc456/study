# install.packages('readxl')
library(readxl)

# 엑셀파일 불러오기
df_finalexam <- read_excel('finalexam.xlsx', sheet=1 , col_names = T)
df_finalexam

# csv파일 불러오기
exam <-read.csv('csv_exam.csv', header = T)

exam

# csv로 저장하기
write.csv(df_finalexam, file='output_newdata.csv')