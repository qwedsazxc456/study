library(ggplot2)
library(dplyr)

#t-test
mpg <- as.data.frame(ggplot2::mpg)

mpg_diff <- mpg %>% 
  select(class, cty) %>% 
  filter(class %in% c('compact', 'suv'))

head(mpg_diff)

table(mpg_diff$class)

t.test(data=mpg_diff, cty~class, var.equal= T)

mpg_diff %>% group_by(class) %>% summarize(mean_cty=mean(cty))

mpg_diff2 <- mpg %>% select(fl,cty) %>% filter(fl %in% c('r','p'))

table(mpg_diff2$fl)

t.test(data=mpg_diff2, cty~fl, var.equal=T)

mpg_diff3 <- mpg %>% select(fl,hwy) %>% filter(fl %in% c('r','p'))
t.test(data=mpg_diff3, hwy~fl, var.equal=T)

#상관분석
e <- ggplot2::economics

cor.test(e$unemploy,e$pce)

plot(e$unemploy,e$pce)
help("economics")

#상관행렬
car_cor<-cor(mtcars)
car_cor

library(corrplot)
corrplot(car_cor,method='number')
corrplot(car_cor,method='color',type='lower',
         order='hclust',addCoef.col = 'black',tl.col='black',tl.srt=45,
         diag=F)

#분할표 
table(c('a','b','c','d','e'))

prop.table(table(iris$Species))

fw <- cut(mpg$cty, breaks=4)

table(fw)

Ctable<-data.frame(x=c(3,7,9,10),
                   y=c('a1','b2','a1','b2'),
                   num=c(4,6,2,9))

Ctable

xtabs(num~x,data=Ctable)
xtabs(num~y,data=Ctable)
xtabs(x~y,data=Ctable)
xtabs(num~x+y,data=Ctable)

temp <- xtabs(num~x+y,data=Ctable)

margin.table(temp,1)
margin.table(temp,2)

child1<-c(5, 11, 1)
child2<-c(4, 7, 3)
toy <- cbind(child1, child2)
rownames(toy)<-c("car", "truck", "doll")
toy

chisq.test(toy) #카이제곱 검정 

#Pearson's Chi-squared test( Chi-squared 카이제곱) 



#경고메시지(들): In chisq.test(toy) : 카이제곱 approximation은 정확하지 않을수도 있습니다

data_matrix<-matrix(c(7,13,9,12,13,21,10,19,11,18,12,13),byrow = T, nrow=3)
dimnames(data_matrix) <- list('class'=c('class_1','class_2','class_3'),
                              'score'=c('score_H','score_M','score_L','fail'))
addmargins(data_matrix)
prop.table(data_matrix)
addmargins(prop.table(data_matrix))

barplot(t(data_matrix),beside=T, legend=T,
        ylim=c(0,30),ylab='Observed frequencies in sample',
        main='Frequency of math score by class')

chisq.test(data_matrix)

#적합성 검정
obs <- c(19, 41, 40)
null.probs <- c(2/10, 3/10, 5/10) #인자가 하나이다. 비율을 만든다 
chisq.test(obs, p=null.probs) 
#Chi-squared test for given probabilities

#t-test
score1<-read.csv('../data/score.csv',header=T)
score1

result <- t.test(score1$score, alternative = c('greater'),mu=75)
result

score2 <- data.frame(id=c(1,2,3,4,5,6,7,8,9,10),score=c(85,95,75,88,83,95,99,72,80,88))
score2

t.test(score2$score, alternative = 'greater' , mu=75)

df<-data.frame(a=c(1,2,1,1,1,2,2,1,1,1,2,2,1,2,1),b=c(163,157,161,162,158,160,165,170,162,172,165,165,159,161,168))
t.test(df$b , alternative = 'greater' , mu=160)

