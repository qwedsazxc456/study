library(dplyr)

df_raw <-data.frame(var1=c(1,2,1),
                    var2=c(2,3,2))
df_raw

# 복사본 만들기
df_new <- df_raw
df_new

df_new <- rename(df_new, v2=var2) # var2를 v2로수정 / 새 변수명=기존 변수명
df_new

# 연습
mpg <- ggplot2::mpg
mpg_new <- mpg
mpg_new <- rename(mpg_new, city=cty , highway=hwy)
head(mpg_new)

