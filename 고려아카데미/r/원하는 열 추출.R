exam %>% select(math)
exam %>% select(class, math, english)

#변수제외
exam %>% select(-math)
exam %>% select(-math,-english) # 영어,수학 제외

# class가 1인 english 추출
exam %>% filter(class==1) %>% select(english)

exam %>% 
  select(id, math) %>% 
  head(10)

#연습
mpg %>% 
  select(class, cty) %>% 
  head()

suv <- mpg %>% 
  select(class, cty) %>% 
  filter(class=='suv')
mean(suv$cty)  
