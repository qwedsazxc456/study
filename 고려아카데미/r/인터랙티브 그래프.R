library(plotly)
library(ggplot2)
library(dplyr)


# 산점도
ggplot(data=mpg, aes(x=displ, y=hwy))+
  geom_point()

# 샐깔
p <- ggplot(data=mpg, aes(x=displ, y=hwy, col=drv))+
  geom_point()

ggplotly(p)

# 막대그래프
table(diamonds$cut)
table(diamonds$clarity)

df <- diamonds %>% 
  group_by(cut, clarity) %>% 
  summarise(n = n())

ggplot(data=df, aes(x=cut, y=n))+
  geom_col()

# 색깔
ggplot(data=df, aes(x=cut, y=n, fill=clarity))+
  geom_col()

# dodge
ggplot(data=df, aes(x=cut, y=n, fill=clarity))+
  geom_col(position = 'dodge')

p <- ggplot(data=df, aes(x=cut, y=n, fill=clarity))+
  geom_col(position = 'dodge')
           
ggplotly(p)
