a<-c(1,2,3,4,5)
b<-c(1,3,5,7,9)

c<-a+b
c


d<-list(x=c(1,2,3,4,5),y=c(5,6,7,8,9))
d$x
d[[1]]
d[[2]]
d[1]

x<-matrix(1:12,4,byrow=T)

x[1:2,1:2]
x[3:4,2:3]


d<-data.frame(name=c('a','b','c','d'),score=c(200,300,400,500))

plot(d$score)

d[d$name=='a'| d$name=='c',]
d[d$score>=300,]
d[1:2,1:2]

d<-data.frame(name=c('a','b','c','d'),score=c(200,300,400,500),grade=c('a','b','c','a'))

str(d)
d[3,3]='d'
d

d$grade <- as.factor(d$grade)
