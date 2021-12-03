questions <-read.csv('questions_PCA_cut_diff (1).csv')
students <- read.csv('students_ll (1).csv')

View(questions)
View(students)

library(dplyr)

df<-data.frame()

for (i in seq(1:277)){
  for (j in seq(1:11160)){
    b <- questions$diff2[j]*(-1)
    a <- exp(b)/4
    theta <- students$learning_level2[i]
    df[j,i] <- 0.75/(1+exp(-a*(theta-b)))+0.25
    
  }
  
}


# rownames(df)<-questions$question_id
colnames(df)<-students$user_id


write.csv(df, file = '정답률예측_5.csv')


df2<-data.frame()
for (i in seq(1:277)){
  for (j in seq(1:11160)){
    df2[j,i]<-ifelse(df[j,i]<0.5,0,1)}
}

# rownames(df2)<-questions$question_id
colnames(df2)<-students$user_id

write.csv(df2, file = '정답(0,1)_5.csv')

# df3<-read.csv('questions_by_students.csv')
# View(df3)

# df3 <- df3[,-1]

df4 <- data.frame()

for (i in seq(1:11160)){
  for (j in seq(1:277)){
    df4[i,j] <-ifelse(df3[i,j] != -1, ifelse(df3[i,j]==df2[i,j],1,0), NaN)
  }
}

df6 <- data.frame()

df5 <- df4

for (i in seq(1:277)){
  df6[i,1]<-sum(na.omit(df5[,i]))/(11160-sum(is.na(df5[,i])))
}

View(df6)

mean(df6[,1])
