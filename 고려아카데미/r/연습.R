#문제풀어보기
library(dplyr)
library(ggplot2)

welfare <- read.csv('welfare.csv')
welfare <- data.frame(welfare)

str(welfare)
dim(welfare)

welfare <-rename(welfare, income=p1002_8aq1)

hist(welfare$income)

summary(welfare$income)

welfare_test <- ifelse(welfare$income > mean(welfare$income),'high','low')

table(welfare_test)
qplot(welfare_test)
