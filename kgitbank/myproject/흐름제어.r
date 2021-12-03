x<-1:10
ifelse(x%%2==0,'even','odd')

x<-as.integer(runif(20,1,100))
x

sum(ifelse(x%%7==0,1,0))

for (i in 1:20) {print(i[i%%2==0])}
for (i in 1:20) {print(i[i%%2==1])}
for (i in 1:70) {print(i[i%%7==0])}

i<-1
while(i<10){
  print(i)
  i<-i+1
}

while(i<=5){
  print(3*i)
  i<-i+1
}

i<-1
while(i<11){
  print(7*i)
  i<-i+1
}

x<-c(1,2,3,NA,5,6,7,NA,8)

x<-na.omit(x)

x
sum(x)
mean(x,na.rm=T)
median(x,na.rm=T)

df<-data.frame(x=1:5, y=seq(2,10,2))
df[3,2]=NA
df

resid(lm(y~x,data=df,na.action = na.omit))
resid(lm(y~x,data=df,na.action = na.exclude))

fibo <- function(n){
  if(n==1|n==2){
    return(1)
  }
  return(fibo(n-1)+fibo(n-2))
}

myfunc1 = function(x,y,z){
  cat('x=',x,'\n')
  cat('y=', y, '\n')
  cat('z=',z,'\n')
}

myfunc1(1,2,3)
myfunc1(z=10,y=20,x=30)

?print

rm(list=ls())
ls()


