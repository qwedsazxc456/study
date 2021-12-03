a<- data.frame(id=c(1,2,3,4,5),name=c('a','b','c','d','e'))
a

a<- rbind(a,c(6,'f'))
a

a['kor']<-c(1,1,1,1,1,1)
a

b<-matrix(1:9,3)

#행추가
b<- rbind(b,c(4,7,10))
b

#열 추가
b<- cbind(b,c(11,12,13,14))
b

#행들의 합계
a<-apply(b,1,sum)
a

#열들의 합계
a<-apply(b,2,sum)
a

#각 행에서 제일 큰 값
a<- apply(b,1,max)
a

head(iris)
apply(iris[,1:4],2,sum) #행을 생략하면 전체행
apply(iris[,1:4],1,sum)

rowSums(iris[,1:4])
rowMeans(iris[,1:4])
colSums(iris[,1:4])
colMeans(iris[,1:4])

#벡터: 파이썬의 list, 다른언어의 배열
#리스트: 파이썬의 dict, 자바의 HashTable, c#의 Dictionary


a <- lapply(1:3 , function(x){x*2})
a

a[1]
a[2]
a[3]

a[[1]]

#apply에 사용자 정의 함수 적용하기
apply(matrix(1:9,3),2,function(x){x*2})

lapply(matrix(1:9,3), function(x){x*2})

d<-as.data.frame(matrix(unlist(lapply(iris[,1:4], mean)),ncol=4,byrow=T))
names(d)=names(iris[,1:4])
d

#do.call 

data.frame(do.call(cbind,lapply(iris[,1:4],mean)))

x<-list(data.frame(name='foo',value=1),data.frame(name='boo',value=2))
unlist(x)

do.call(rbind,x)

x<-(t(sapply(iris[,1:4],mean)))
y<-(t(sapply(iris[,1:4],max)))
z<-(t(sapply(iris[,1:4],min)))
m<-rbind(x,y,z)

rownames(m)<-c('mean','max','min')
m

#도시연비 고속도로연비 평균
library(ggplot2)
mpg<-ggplot2::mpg

str(mpg)
sapply(mpg[,'cty'&'hwy'],mean)

#
y <- sapply(iris[,1:4],function(a){a>3})
y

tapply(iris$Sepal.Length, iris$Species, mean)

#
cty<-tapply(mpg$cty,mpg$manufacturer,mean)
hwy<-tapply(mpg$hwy,mpg$manufacturer,mean)
cbind(cty,hwy)

a<-as.data.frame(HairEyeColor)
tapply(a$Freq,a$Sex,sum)


help(hist)












