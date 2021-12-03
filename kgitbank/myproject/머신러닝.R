
data(anscombe)
attach(anscombe)
anscombe
detach(anscombe)

cor(x1,y1)
cor(x2,y2)
cor(x3,y3)
cor(x4,y4)

par(mfrow=c(2,2))
plot(x1,y1)
plot(x2,y2)
plot(x3,y3)
plot(x4,y4)

install.packages('https://cran.r-project.org/src/contrib/Archive/alr3/alr3_2.0.8.tar.gz',repos = NULL,type='source')
library(alr3)
data(snake)
dim(snake)
head(snake)
str(snake)
summary(snake)

names(snake)<-c('content','yield')
snake

par(mfrow=c(1,1))
attach(snake)
plot(content,yield,xlab='water content of snow',ylab='water yield')
cor(content,yield)

yield.fit<-lm(yield~content)
yield.fit

summary(yield.fit)

yield=0.7254+content*0.4981

plot(content,yield)
abline(yield.fit, lwd=3, col='red')

par(mfrow=c(2,2))
plot(yield.fit)
par(mfrow=c(1,1))

library(ggplot2)
library(car)
qqplot(yield.fit)

test<-data.frame(content=c(12,14,20,19),yield=c(0,0,0,0))
predict(yield.fit, newdata=test, type='response')

library(alr3)

data(water)
head(water)

str(head)
social.water<-water[,-1] #year 필드 제거하기 
head(social.water)

library(corrplot)
water.cor <- cor(social.water)
water.cor

corrplot(water.cor, method="ellipse")


pairs(~., data=social.water)

#lm(종속변수 ~ 독립1+독립2 +독립3...)
#lm(종속변수 ~ . )

fit <- lm(BSAAM~., data=social.water)

fit
summary(fit)

#R은   step 을 사용하면 여러가지 변수를 돌아가면서 
#      최적하된 것을 검색한다 
reduced <- step(fit, direction="backward")

reduced

library("ggvis")  
iris %>% ggvis(~Sepal.Length, ~Sepal.Width, fill = ~Species) %>% layer_points()

#1.데이터를 6:4  또는 7:3 또는 8:2정도로 나누자 
set.seed(1234) #시드를 주어야 항상 같은 데이터로 배분된다 
#R에는 sample함수를 데이터를 나눈다 
#첫번째 인자 - 데이터를 몇개로 분할할까 
#두번째 인자는 데이터 행의 개수 
#세번째 인자는 0 replace=TRUE 나 자신을 바꿔라 
#4번째 인자 - 비율 0.67  ~ 0.33
#데이터 인덱스를 섞어서 인덱를 두그룹으로 만든다 
ind <- sample(2, nrow(iris), replace=TRUE, prob=c(0.67, 0.33)) # 데이터 배분하기
ind[1]
ind[2]

iris.training <- iris[ind==1, 1:4]   #훈련셋 
head(iris.training)
#테스트셋 
iris.test <- iris[ind==2, 1:4]  #데이터셋 
head(iris.test)

#결과를 별도로 
iris.trainLabels <- iris[ind==1,5]    #훈련셋 종류 확인
iris.testLabels <- iris[ind==2, 5]     #데이터셋 종류 확인

iris.trainLabels[1:10]
iris.testLabels[1:10]

install.packages("class")
library(class)

# Build the model
iris_pred <- knn(train = iris.training,    #훈련셋  
                 test = iris.test,           #데이터셋
                 cl = iris.trainLabels,   #훈련셋의 결과값 
                 k=3)                     #k-이웃의 개수 

# Inspect `iris_pred`
iris_pred[1]
iris.testLabels[1]
len = length(iris.testLabels)

print( iris.testLabels == iris_pred)
table(iris.testLabels == iris_pred )


