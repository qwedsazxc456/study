train <- read.csv('train_until_10m_noDupl.csv')

View(train)

train_1 <- train %>% 
  group_by(content_id) %>% 
  summarise(n1=n()) %>% 
  arrange(n1)

hist(train_1$n1,breaks = 100)
  

hist(train_1$n1[1:10000],breaks = 100)

summary(train_1$n1)

train_2 <- train %>% 
  filter(part %in% seq(1,7))

train_3 <- train_2 %>% 
  group_by(content_id) %>% 
  summarise(n1=n()) %>% 
  arrange(n1)

hist(train_3$n1[1:10523])

summary(train_3$n1)

train_4<-train_2 %>% 
  group_by(content_id) %>% 
  count(part)

View(train_1)

a<-train_1$content_id[0:2189]

write.csv(a, file='id2.csv')

a<-train_1$content_id[1:2086]

train_3<- train_2 %>% 
  group_by(user_id,part) %>% 
  summarise(n1=n()) %>% 
  arrange(user_id)
  
train_4 <- train_3 %>% 
  filter(n1<10)

View(train_4)

write.csv(train_4$user_id, file='id5.csv')


train_4 <- train2 %>% 
  filter(part==1) %>% 
  filter(answered_correctly==0) %>% 
  group_by(user_id) %>% 
  summarise(n0=n())

train_5 <- train_2 %>% 
  filter(part==1) %>% 
  filter(answered_correctly==1) %>% 
  group_by(user_id) %>% 
  summarise(n1=n())

train_6_1 <- full_join(train_4, train_5, by='user_id') %>% 
  mutate(p1=n1/(n0+n1))

train_6_1 <- train_6_1 %>% 
  select(user_id, p1)

train_6 <- full_join(train_6,train_6_1, by='user_id')       
View(train_6)

write.csv(train_6, file = 'part.csv')
