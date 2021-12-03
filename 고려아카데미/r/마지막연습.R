welfare<-read.csv('welfare.csv')
welfare <- rename(welfare,
                  income = p1002_8aq1,
                  birth = h10_g4,
                  code_job = h10_eco9)

welfare <- welfare %>% 
  mutate(age = 2015-birth+1)

list_job <- read.csv('list_job.csv')
head(list_job)

welfare <- left_join(welfare, list_job, by='code_job')

job_10 <- welfare %>% 
  group_by(job) %>% 
  summarise(n=n()) %>% 
  arrange(desc(n)) %>% 
  head(10)

ggplot(data=job_10, aes(x=reorder(job,n),y=n))+
  geom_col()+
  coord_flip()

welfare <- welfare %>% 
  mutate(age_1=ifelse(age<30,'20s',ifelse(age<40,'30s','40s')))

job_20_10<-welfare %>% 
  filter(age_1=='20s') %>% 
  group_by(job) %>% 
  summarise(n=n()) %>% 
  arrange(desc(n)) %>% 
  head(10)

ia <- ggplot(data=job_20_10, aes(x=reorder(job,n),y=n,fill=job))+
  geom_col()+
  coord_flip()

ggplotly(ia)
