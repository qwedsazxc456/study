ggplot(data=mpg, aes(x=drv, y=hwy))+
  geom_boxplot()

# 연습
mpg_2 <- mpg %>% 
  filter(class %in% c('compact','subcompact','suv'))

ggplot(data=mpg_2, aes(x=class, y=cty))+
  geom_boxplot()


