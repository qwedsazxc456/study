train <- read.csv('data_for_train.csv')
test <- read.csv('data_for_test_refine.csv')
correct <- read.csv('정답(0,1)_2.csv')

df2 <- data.frame()
for (i in seq(1:224)){
  theta <- test$learning_level2[i]
  b <- test$diff2[i]*(-1)
  a <- exp(b)/3
  df2[i,1] <- 0.75/(1+exp(-1*(theta-b)))+0.25
  df2[i,2] <- ifelse(df2[i,1] <.5,0,1)
  df2[i,3] <- ifelse(df2[i,2]==test$answered_correctly[i],1,0)
}
View(df2)

mean(df2$V3)

View(test)

df2 %>% 
  filter(V3==0)

library(dplyr)

df3 <- data.frame()

for (i in seq(1:224)){
df3[i,1] <-  test$answered_correctly[i]}

View(df3)


df3 %>% filter(V1==1)


