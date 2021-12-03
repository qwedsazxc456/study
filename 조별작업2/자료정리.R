library(dplyr)
library(ggplot2)

train <- read.csv('train_until_10m.csv')

View(train)

train_1 <- train %>% 
  group_by(user_id,answered_correctly) %>% 
  filter(answered_correctly==0) %>% 
  summarise(n1=n())

train_2 <- train %>%
  group_by(user_id,answered_correctly) %>% 
  filter(answered_correctly==1) %>% 
  summarise(n2=n())
  
train_1
train_2  

train_3 <- left_join(train_1,train_2,by='user_id')

train_4 <- train_3 %>% 
  mutate(p=n2/(n1+n2)) %>% 
  arrange(p) 

train_4$user_id=seq(1,9752)
ggplot(data=train_4, aes(x=p,y=n3))+geom_point()

hist(train_4$p, breaks = 100)

dim(train)

summary(train_4) 

train_5 <- train %>% 
  group_by(user_id) %>% 
  summarise(n=n())

hist(train_5$n,breaks = 1000, xlim=c(0,1000))

summary(train_5)
