library(plotly)
library(ggplot2)

mpg<-ggplot2::mpg
p<-ggplot(data=mpg, aes(x=displ,y=hwy,col=drv))+geom_point()
ggplotly(p)

a<-ggplot(data=iris, aes(x=Petal.Width, y=Petal.Length, col=Species))+geom_point()
ggplotly(a)

str(iris)

options(scipen=999)  # turn-off scientific notation like 1e+48
library(ggplot2)
theme_set(theme_bw())  # pre-set the bw theme.
data("midwest", package = "ggplot2")
# midwest <- read.csv("http://goo.gl/G1K41K")  # bkup data source

# Scatterplot
gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
  geom_point(aes(col=state, size=popdensity)) + 
  geom_smooth(method="loess", se=F) + 
  xlim(c(0, 0.1)) + 
  ylim(c(0, 500000)) + 
  labs(subtitle="Area Vs Population", 
       y="Population", 
       x="Area", 
       title="Scatterplot", 
       caption = "Source: midwest")

plot(gg)
ggplotly(gg)

p<- ggplot(data=diamonds,aes(x=cut,fill=clarity))+geom_bar(position='dodge')
ggplotly(p)



#시계열차트
library(dygraphs)
library(dplyr)
library(ggplot2)

economics <- ggplot2::economics
head(economics)

library(xts)
eco<-xts(economics$unemploy,order.by = economics$date)
head(eco)

dygraph(eco)

dygraph(eco) %>% dyRangeSelector()

# 저축률 
eco_a <- xts(economics$psavert, order.by = economics$date)

# 실업자 수
eco_b <- xts(economics$unemploy/1000, order.by = economics$date)

eco2 <- cbind(eco_a, eco_b)                 # 데이터 결합
colnames(eco2) <- c("psavert", "unemploy")  # 변수명 바꾸기
head(eco2)

dygraph(eco2) %>% dyRangeSelector()

a<-read.csv('C:/Users/Administrator/Desktop/python/일간주식.csv')
a$date<-as.Date(a$date)
b<-xts(a$tradePrice,order.by=a$date)
dygraph(b) %>% dyRangeSelector()

