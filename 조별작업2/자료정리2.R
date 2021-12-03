train <- read.csv('train_until_1m_1.csv')
View(train)

train_1 <- train %>% 
  group_by(user_id,answered_correctly) %>% 
  filter(answered_correctly==0) %>% 
  summarise(n1=n())

train_2 <- train %>%
  group_by(user_id,answered_correctly) %>% 
  filter(answered_correctly==1) %>% 
  summarise(n2=n())

train_3 <- left_join(train_1,train_2,by='user_id')

train_4 <- train_3 %>% 
  mutate(p=n2/(n1+n2),
         p2=p*1000+30) %>% 
  arrange(p) 

hist(train_4$p, breaks =20)
summary(train_4)

train_4[111]
1112*63/100
train_4$p[701]
1112*96/100
train_4$p[1068]

train_5 <- train %>% 
  group_by(user_id,answered_correctly) %>% 
  filter(answered_correctly==-1) %>% 
  summarise(n1=n())

train_5
sum(train_5$n1)

train_4$user_id[1:31]
train_4$p2[1109]

hist(train_4$p2, breaks =10 )
summary(train_4$p2)


