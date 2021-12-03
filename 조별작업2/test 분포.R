library(ggplot2)
library(plotly)

df2 <- df2 %>% 
  mutate(correctly = test$answered_correctly)

View(df2)

ggplot(data=df2, aes(x=V1, y=correctly, col=V2))+
  geom_point()

ggplotly(p)

as.numeric(df2$V2)
