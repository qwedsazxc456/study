m1<-matrix(1:12,3,byrow = T,dimnames = )
m2<-matrix(1:12,,3)

m1<-matrix(1:9,3)
m1%*%m1

#역행렬
m1<-matrix(c(1,0,0,0,1,0,0,0,1),3)
solve(m1)

A=matrix(c(1,3,4,2,5,1,4,2,3),nrow=3)
solve(A)

det(m1)

m1<-matrix(c(1,1,1,1),2)
solve(m1)

