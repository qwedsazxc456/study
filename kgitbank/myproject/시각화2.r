head(mtcars)
plot(mtcars$mpg,mtcars$wt)
lines(lowess(mtcars$mpg,mtcars$wt))

#선형회귀분석
model1<- lm(wt~mpg,data=mtcars)
model1
abline(model1, col='red')
abline(a=37.285,b=-5.344,col='red')

library(ggplot2)
mpg<- ggplot2::mpg

lm(displ~cty,data=mpg)
lm(displ~hwy,data=mpg)

library(mlbench)
data(Ozone)

plot(Ozone$V8,Ozone$V9)
Ozone2<-na.omit(Ozone)
lines(lowess(Ozone$V8,Ozone$V9))
abline(lm(V8~V9,data=Ozone))

str(Ozone)

help(lowess)

help(boxplot)

boxplot(iris$Sepal.Length)
b<-boxplot(iris$Sepal.Length)
b

head(mpg)
str(mpg)
mpg$manufacturer

boxplot(mpg$cty~mpg$manufacturer)

help(hist)

hist(iris$Sepal.Length)


