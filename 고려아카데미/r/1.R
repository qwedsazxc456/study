library(dplyr)
library(ggplot2)

head(mpg)
dim(mpg)
str(mpg)
summary(mpg)
View(mpg)

mpg %>% group_by(manufacturer) %>%
  summarise(mean_hwy=mean(hwy)) %>%
  arrange(desc(mean_hwy))

lm_mpg <- lm(data=mpg, hwy~displ)
summary(lm_mpg)

qplot(data=mpg,x=displ,y=hwy)
