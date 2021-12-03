train <- read.csv('train_until_1m_part_noDupl.csv')
id <- read.csv('id5.csv')

'%!in%' <- Negate('%in%')

View(train2)

train2 <- train %>% 
  filter(user_id %!in% id$x)

write.csv(train2, file = '겹치는거 제거 정리.csv')

View(train3)
train3 <- train2 %>% 
  group_by(user_id) %>%
  filter(answered_correctly==0) %>% 
  summarise(n0=n())
  
train4 <- train2 %>% 
  group_by(user_id) %>%
  filter(answered_correctly==1) %>% 
  summarise(n1=n())

train5 <- train3 %>% 
  select(user_id) %>% 
  mutate(diff2=train4$n1/(train3$n0+train4$n1))
  
View(train5)

write.csv(train5, file='학생정답률.csv')
