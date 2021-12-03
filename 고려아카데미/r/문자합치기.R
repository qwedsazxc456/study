e<-c('hello','word','is','good')
# 문자끼리 +는 안됨
paste(e, collapse = ' ')
# "hello word is good"
e_paste <-paste(e, collapse = ' ')
e2_paste <- paste(e, collapse = ',')
e2_paste
# "hello,word,is,good"