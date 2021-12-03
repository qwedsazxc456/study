library(mlbench)
data(Ozone)
plot(Ozone$V8,Ozone$V9)

cor(iris$Petal.Length,iris$Petal.Width)
Ozone

plot(mpg$cty,mpg$hwy,xlab = '도시연비',ylab='고속도로연비',
     main='도시연비와 고속도로연비 비교',pch=19,cex=1.2,
     col='#ff0000' ,col.lab='#00ffff',col.main='#00ff00' )

#색은 color()에서 나온거 혹은 #RRGGBB 16진수로

#데이터안에 NA 있으면 최소값, 최대값 못찾는다. na.rm=True로 할수있다
min(mpg$cty, na.rm=T)
max(mpg$cty, na.rm=T)
min(mpg$hwy, na.rm=T)
max(mpg$hwy, na.rm=T)

#type='l' 꺾은선 그래프
data(cars)
plot(cars,type='l')
plot(cars,type='b')
plot(cars,type='o')

#화면나누기 par
oldpar <- par(mfrow=c(1,2))

par(oldpar)


plot(Ozone$V8,Ozone$V9)

par(mfrow=c(1,1))

x<-seq(0,2*pi,0.1)
y<-sin(x)
plot(x,y, cex=.5)
lines(x,y)
lines(x,cos(x))

#선형회귀모델
m<-lm(dist~speed,data=cars)
m

cars
