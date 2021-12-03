# 연습

library(dplyr)

welfare <- read.csv('welfare.csv')
welfare <- data.frame(welfare)

welfare <- rename(welfare, birth=h10_g4)
welfare <- welfare %>% 
  mutate(age=2021-birth+1)

welfare %>% 
  mutate(age=2021-birth+1) %>% 
  summarise(mean_age=mean(age),
            min_age=min(age),
            max_age=max(age))

welfare <- rename(welfare, income=p1002_8aq1)

welfare %>% 
  group_by(age) %>% 
  summarise(mean(income))

welfare <- welfare %>% 
  mutate(age_1=ifelse(age>=20&age<30,20,ifelse(age<40,30,40)))

welfare %>% 
  group_by(age_1) %>% 
  summarise(n=n(),
            mean_income=mean(income))
