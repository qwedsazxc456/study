library(KoNLP)
library(dplyr)
library(stringr)
library(tm)
library(SnowballC)
library(RColorBrewer)
library(wordcloud)

useNIADic()

nouns<-extractNoun("대한민국의 영토는 한반도와 그 부속도서로 한다") #명사만 추출하기 
nouns 

