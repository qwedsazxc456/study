library(dplyr)
library(ggplot2)
mpg <- ggplot2::mpg 

#첫번째문제
mpg2 <- mpg %>% 
  filter(class=="suv") %>%
  group_by(manufacturer) %>% 
  summarize(mean_cty=mean(cty)) %>%
  arrange(desc(mean_cty)) %>%
  head(5)

ggplot(data=mpg2, aes(x=reorder(manufacturer, -mean_cty), y=mean_cty)) + 
  geom_col()

#두번째문제 
ggplot(data=mpg, aes(x=class)) + geom_bar()



e<-ggplot2::economics 
head(e)

help(economics)

#시계열차트
ggplot(data=e, aes(x=date, y=unemploy)) + geom_line()

ggplot(data=e, aes(x=date, y=psavert)) + geom_line()

#boxplot
ggplot(data = mpg, aes(x = drv, y = hwy)) + geom_boxplot()

#각 종류별로 몇개씩 있나
table(mpg$class)

cmpg <- mpg %>% filter(class %in% c("compact", "subcompact", "suv"))

ggplot(data=cmpg, aes(x=class, y=cty)) + geom_boxplot()


library(foreign)             
library(dplyr)               
library(ggplot2)             
library(readxl)    #설치필요함 

welfare<- read.spss(file = "../data/Koweps_hpc10_2015_beta1.sav",
                    to.data.frame = T)

head(welfare)
dim(welfare)
summary(welfare)
str(welfare)

welfare <- rename(welfare,
                  gender = h10_g3,  
                  birth = h10_g4,  
                  marriage = h10_g10,  
                  religion = h10_g11,      
                  income = p1002_8aq1,     
                  code_job = h10_eco9,     
                  code_region = h10_reg7) 
head(welfare)
wel <- welfare %>% select(gender, birth, marriage, religion,income,code_job,  code_region  )
head(wel)

#각 데이터의 빈도표(분할표)를 작성해서 잘못된 데이터가 입력되었는지 확인하기 위한 용도로 많이 사용된다. 
table(wel$gender)
class(wel$gender)

#강제로 결측치를 만들고 있음
wel$gender[1]=9
table(wel$gender)

#결측치 - 데이터가 없는 경우나 존재하면 안되는 데이터도 결측치다
#1.문제가 있는 값을 NA 로 바꿔치기 한다 
wel$gender <- ifelse(wel$gender==9, NA, wel$gender)
table(wel$gender)
table(is.na(wel$gender))

#NA값을 대체값으로 대체하거나 또는 그 행을 삭제시키거나 
wel$gender <- ifelse(wel$gender==NA, 2, wel$gender)
table(is.na(wel$gender))

#성별이 1 male  2 female로 바꾸고 
#factor 타입으로 전환해야 한다 

wel <- welfare %>% select(gender, birth, marriage, religion,income,code_job,  code_region  )
wel$gender <-ifelse(wel$gender==1, "male", "female")
wel$gender <- factor(wel$gender)
str(wel)
head(wel)

qplot(wel$gender)

class(wel$income)

summary(wel$income)

qplot(wel$income) + xlim(0, 1000)

table(is.na(wel$income))

#결측치를 어떻게 할것인가를 생각해봐야한다 
#무시할까? 평균치로 대체할까? 중간값으로 대체할까?

ggplot(data=wel, aes(x=income)) + geom_boxplot()

#1.NA값을 무시하고 
gender_income <- wel %>% filter(!is.na(income)) %>%
  group_by(gender) %>%
  summarize(mean_income = mean(income))

gender_income 

ggplot(data = gender_income, aes(x = gender, y = mean_income)) + geom_col()
"""
1. 장기근무자가 많고 
2. 
"""

class(wel$birth)
summary(wel$birth)

table(is.na(wel$birth))


#생년월일, 나이 
wel$age <- 2015 - wel$birth + 1
qplot(wel$age)


age_income <- wel %>% filter(!is.na(income)) %>%
  group_by(age) %>%
  summarize(mean_income = mean(income))

age_income 

ggplot(data = age_income, aes(x = age, y = mean_income)) + geom_col()

ggplot(data = age_income, aes(x = age, y = mean_income)) + geom_line()


#연령대를 나눠어서 분석해보자(young, middle, old)

wel$age2 <- ifelse(wel$age<30, "young", ifelse(wel$age<=59, "middle", "old"))
head(wel, 20)

table( wel$age2)
qplot(wel$age2)



age2_income <- wel %>% filter(!is.na(income)) %>%
  group_by(age2) %>%
  summarize(mean_income = mean(income))

age2_income
ggplot(data = age2_income, aes(x = age2, y = mean_income)) + geom_col()


gender_age <- wel %>% filter( !is.na(income )) %>%
  group_by(gender, age2) %>%
  summarize(mean_income = mean(income) )

gender_age


ggplot(data=gender_age, aes(x=age2, y=mean_income, fill=gender)) + 
  geom_col(position = "dodge")













