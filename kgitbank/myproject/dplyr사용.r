library('dplyr')

setosa=iris %>% filter(Species=='setosa')
versinica=iris %>% filter(Species=='versinica')
iris %>% filter(Species=='setosa')

exam<-read.csv("../Data/csv_exam.csv")

class1=exam%>%filter(class==1)
class2=exam%>%filter(class==2)
class3=exam%>%filter(class==3)
class4=exam%>%filter(class==4)
class1
class2
class3
class4

#1반하고 2반
exam %>% filter(class==1|class==2)

#1반하고 2반 아닌것
exam %>% filter(class!=1 & class !=2)

exam %>% filter(class ==1 & math >= 80)

exam %>% filter(math >=80)

exam %>% filter(class %in% c(1,3,5))

#mtcars 데이터에서 실린더 개수가 8개인거 추출하기

summary(mtcars)

mtcars %>% filter(cyl==8)

mtcars %>% filter(cyl==4 & mpg >=20)

exam %>% select(math)
exam %>% select(-math)
exam %>% filter(class==1) %>% select(class,math)

exam %>% arrange(math)
exam %>% arrange(desc(math))

#반별로 정렬하고 같은 반일때는 수학성적을 내림차순으로
exam %>% arrange(class,desc(math))

exam %>% arrange(class, desc(math)) %>% head(2)

exam %>% mutate(total = math+english+science) %>% 
         mutate(avg=total/3) %>% arrange(desc(total))

#통계 요약정보 summarise
exam %>% summarise(mean_math=mean(math),
                   mean_english=mean(english),
                   mean_science=mean(science))

exam %>% group_by(class) %>% summarise(mean_math=mean(math),
                             mean_english=mean(english),
                             mean_science=mean(science))

exam %>% group_by(class) %>% summarise(mean_math=mean(math),
                                       sum_math=sum(math),
                                       median=median(math),
                                       n=n()) #n() 카운트

mpg <- read.csv("../Data/mpg.csv")
summary(mpg)
str(mpg)
head(mpg)

mpg %>% group_by(manufacturer,drv) %>% 
  summarise(mean_cty=mean(cty)) %>% head()

mpg %>% select(class,cty) %>%
  filter(class=='suv'|class=='compact') %>% 
  group_by(class) %>% summarise(mean(cty))

mpg%>% filter(manufacturer=='audi')%>% 
  arrange(desc(hwy)) %>% head(5)

summary(exam)

exam %>% mutate(test=ifelse((math+english+science)/3>=60&
                              math>=40&english>=40&science>=40
                            ,'pass','false'))

mpg %>% mutate(avg=cty+hwy/2) %>% arrange(desc(avg)) %>% head(3)
mpg$class
mpg %>% filter(class=='suv')%>% group_by(manufacturer) %>%
  mutate(avg=(cty+hwy)/2) %>% summarise(mavg=mean(avg)) %>%
  arrange(desc(mavg)) %>% head(5)

mpg %>% group_by(class) %>% summarise(m_cty=mean(cty)) %>% 
  arrange(desc(m_cty))

mpg %>% group_by(manufacturer) %>% summarise(m_hwy=mean(hwy)) %>% head(3)

mpg %>% group_by(manufacturer) %>% filter(class=='compact') %>%
        summarise(n=n()) %>% arrange(desc(n))

#가로로 합치기
test1 <- data.frame(id=c(1,2,3,4,5),midterm=c(60,80,70,90,85))
test2 <- data.frame(id=c(1,2,3,4,5),final=c(70,83,65,95,80))

total <- left_join(test1, test2, by='id')
total

name <- data.frame(class=c(1,2,3,4,5),teacher=c('kim','lee','park','choi','jung'))

name

exam_new <- left_join(exam, name, by ='class')
exam_new

group_a <- data.frame(id=c(1,2,3,4,5),test=c(60,80,70,90,85))
group_b <- data.frame(id=c(6,7,8,9,10),test=c(70,83,65,95,80))

group_all<-bind_rows(group_a,group_b)
group_all

fuel<-data.frame(fl=c('c','d','e','p','r'),
                 price_fl=c(2.35,2.38,2.11,2.76,2.22),
                 stringsAsFactors = F)
fuel

mpg

left_join(mpg,fuel,by='fl')


library('ggplot2')

ggplot2::mpg

mpg<-as.data.frame(ggplot2::mpg)

midwest<-as.data.frame(ggplot2::midwest)

str(midwest)
head(midwest)

midwest %>% mutate(미성년=(poptotal-popadults)/poptotal*100) %>% 
  arrange(desc(미성년)) %>%
  head(5)

midwest %>% mutate(미성년=(poptotal-popadults)/poptotal*100)%>%
  mutate(등급=ifelse(미성년>=40 , 'large', 
                     ifelse(미성년>=30,'middle','small')))

midwest %>% 
  mutate(등급=ifelse((poptotal-popadults)/poptotal*100>=40 , 'large', 
                      ifelse((poptotal-popadults)/poptotal*100>=30,'middle','small')))

midwest %>% mutate(아시아=popasian/poptotal*100)%>%select(state,county,아시아) %>%
  arrange((아시아)) %>% head(10)

iris %>% filter(Species=='setosa') %>% summarise(mean(Sepal.Length),mean(Sepal.Width))

table(iris$Species)
                     