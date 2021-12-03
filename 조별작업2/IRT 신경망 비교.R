pred <- read.csv('pred.csv')

View(pred)
View(df2)

pred

df3 <- data.frame()

View(df3)

cor(pred$X0,df2$V1)^2
