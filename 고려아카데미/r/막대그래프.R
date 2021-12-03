library(dplyr)
df_mpg <- mpg %>% 
  group_by(drv) %>% 
  summarise(mean_hwy=mean(hwy))

df_mpg

ggplot(data=df_mpg, aes(x=drv, y=mean_hwy))+
  geom_col()

# 내림차순
ggplot(data=df_mpg, aes(x=reorder(drv,-mean_hwy), y=mean_hwy))+
  geom_col()

# 연습
mpg_1 <- mpg %>% 
  filter(class=='suv') %>% 
  group_by(manufacturer) %>% 
  summarise(mean_cty=mean(cty)) %>%
  arrange(desc(mean_cty)) %>% 
  head(5)
mpg_1

ggplot(data=mpg_1, aes(x=reorder(manufacturer,-mean_cty), y=mean_cty))+
  geom_col()
