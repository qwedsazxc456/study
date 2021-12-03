exam %>% arrange(math) #오름차순
exam %>% arrange(desc(math)) #내림차순
exam %>% arrange(class, math) #class math로 오름차순

# 연습
mpg %>% 
  filter(manufacturer=='audi') %>% 
  arrange(desc(hwy)) %>% 
  head(5)

mpg %>% 
  filter(manufacturer=='audi') %>% 
  arrange(hwy) %>% 
  tail(5)

