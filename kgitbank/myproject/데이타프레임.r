a<-data.frame(x=c(1,2,3,4),y=c(1,2,3,4))
a

df1<-data.frame(name='',kor='',eng='',mat='')
df1[nrow(df1),]<-c('조승연',90,90,100)
df1

df2<-data.frame(no=c(1,2,3),name=c('홍길동','일지매','강감찬'),qty=c(10,30,20))
df2
df3<-df2[-2,]
df3
df4<-cbind(df2,date=c(2018,2017,2016))
df4

d<-data.frame(x=c(1,2,3,4,5),y=c(2,4,6,8,10),
              z=c('m','f','f','m','m'),
              stringsAsFactors = T)
d
d$z[1]='g'
d

#열 추가
d$w<-c('a','b','c','d','e')
str(d)
d
#형전환 함수
d$w<-as.factor(d$w)
str(d)

d[,'w',drop=F]
d[,names(d) %in% c('b','c')]

d<-data.frame(x=1:1000)
head(d)
tail(d)
head(d,10)
tail(d,10)

View(d)
d<-edit(d)
head(d)


