a<-c(1,2,3,4,5)
a

mean(x<-c(1,2,3))

mean(x=c(1,2,3))
x

a<-3
b<-4.5
c<-a+b
c

one<-90
two<-80
three<-75
four<-NA

is.na(one)
is.na(two)      
is.na(three)
is.na(four)

is.null(five)

a<-'hello'
b<-'안녕하세요'

a
b

#벡터일경우 -배열의 경우에는 &와 &&는 차이가 있다.
a<-c(T,T,F,F)
b<-c(T,F,T,F)
c<-a&b
c

gender<-factor(c('m','f'))
nlevels(gender)
levels(gender)
levels(gender)[1]
levels(gender)[2]
gender[1]<-'f'
gender[2]<-"g"

help(factor)

a<-c(4,9,2,6,7,8,11,10,5)
a[order(a)]

seq(2,10,2)

rep(1:3,5)
rep(1:3,,,5)

alist<-list(key1=c(1,2,3,4,5),key2=c('red','green','blue'))
alist

alist$key1

a=1
alist=list(key1=c(1,2,3,4,5),key2=c('red','green','blue'))
alist['key1']
alist$key3<-c('홍길동','임꺽정')
alist


x<-list(name='foo',height=c(1,2,3))
x<-list(a=list(val=c(1,2,3,4)),b=list(val=c(5,6,7,8)))
x

m1<-matrix(1:9,3)

m2<-matrix(seq(1,18,2),3)

m3<-matrix(rep(1:3,3),3)

