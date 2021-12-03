train <- read.csv('train_until_1m_part.csv')

train_2 <- train %>% 
  filter(part %in% seq(1,7))

train_3<- train_2 %>% 
  group_by(user_id,part) %>% 
  summarise(n1=n()) %>% 
  arrange(user_id)

View(train_3)

train_4 <- train_3 %>% 
  filter(n1<10)

View(train_4)

write.csv(train_5$user_id, file='id4.csv')

table(train_4$user_id)

train_5 <- train_4 %>% 
  group_by(user_id) %>% 
  summarise(n=n())

train_5


