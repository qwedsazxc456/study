library(dplyr)
exam <- read.csv('csv_exam.csv')
exam

exam %>% filter(class == 1)
exam %>% filter(class == 2)
exam %>% filter(class != 1) #1반제외
exam %>% filter(math > 50)
exam %>% filter(math < 50)
exam %>% filter(english >= 80)
exam %>% filter(english <= 80)
exam %>% filter(class==2 & english <= 80)
exam %>% filter(math >= 90 | english >= 90)
# & | 여러개 사용가능

exam %>%filter(class %in% c(1,3,5))
# | 반복을 줄일 수 있다.

# 추출한 행을 데이터 만들기
class1 <- exam %>% filter(class==1)

# mpg로 연습
d4 <- mpg %>% filter(displ<=4)
d5 <- mpg %>% filter(displ>=5)
mean(d4$hwy)
mean(d5$hwy)

audi <-mpg %>% filter(manufacturer=='audi')
toyota <-mpg %>% filter(manufacturer=='toyota')
mean(audi$cty)
mean(toyota$cty)

