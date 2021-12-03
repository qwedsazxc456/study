df <- data.frame(var1=c(4,3,8),
                 var2=c(2,6,1))
df

# 새로운 열 생성
df$var_sum <- df$var1 + df$var2
df

df$var_mean <- (df$var1 + df$var2)/2
df

#mpg로 해보기
mpg<-ggplot2::mpg

mpg$total <- (mpg$cty+mpg$hwy)/2
mean(mpg$total)

summary(mpg$total)
hist(mpg$total)

# 조건
mpg$test <- ifelse(mpg$total >=20, 'pass', 'fail')
head(mpg,20)

#빈도수 알아보기
table(mpg$test)


library(ggplot2)
qplot(mpg$test) #막대그래프

