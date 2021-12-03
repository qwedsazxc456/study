library(ggplot2)

ggplot(data=mpg, aes(x=displ, y=hwy))+
  geom_point()+
  xlim(3,6)+
  ylim(10,30)

# 연습
ggplot(data=mpg, aes(x=cty, y=hwy))+
  geom_point()

ggplot(data=midwest, aes(x=poptotal, y=popasian))+
  geom_point()+
  xlim(0,500000)+
  ylim(0,10000)
