# mutate로 새로운 열을 만들면 $를 여러번 쓰지 않아도 된다

# 연습
library(dplyr)
mpg_1 <- mpg %>% 
  mutate(total=cty+hwy,
         mean=(cty+hwy)/2) %>% 
  arrange(desc(mean)) %>% 
  head(3)
head(mpg_1,3)
