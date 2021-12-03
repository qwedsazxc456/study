library(KoNLP)
library(dplyr)
library(stringr)
library(tm)
library(SnowballC)
library(RColorBrewer)
library(wordcloud)

#사전을 사용하는데 useNIADic() 사전을 불러와서 
#명사를 추출할때 사용하겠다 
useNIADic()

twitter <- read.csv("../data/twitter.csv",
                    header=T, 
                    stringsAsFactors = F,
                    fileEncoding = "UTF-8")
class(twitter)
head(twitter)


#변수명 수정 
twitter <- rename(twitter,
                  no = 번호,
                  id = 계정이름,
                  date = 작성일,
                  tw = 내용)

head(twitter)
#특수문자 제거 
twitter$tw = str_replace_all(twitter$tw, "\\W", " ")
twitter$tw
#명사만 추출하기 
nouns <- extractNoun(twitter$tw)
nouns[1:10]
# 추출한 명사 list를 문자열 벡터로 변환, 단어별 빈도표 생성
wordcount <- table(unlist(nouns))
wordcount[1:10]
# 데이터 프레임으로 변환
df_word <- as.data.frame(wordcount, stringsAsFactors = F)
head(df_word)


# 변수명 수정
df_word <- rename(df_word,
                  word = Var1,
                  freq = Freq)


# 두 글자 이상 단어만 추출

df_word <- df_word[length(df_word$word)>=2,]
head(df_word)

pal<- brewer.pal(8,'Dark2')
set.seed(1234) #랜덤값 고정
wordcloud(words = df_word$word, 
          freq = df_word$freq,
          min.freq = 2,
          max.words = 200,
          random.order = F, #고빈도 단어 중앙 배치
          rot.per = .1, #회전 비율
          scale = c(4, 0.3), #크기 범위
          colors = pal)
