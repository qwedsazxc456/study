library(ggiraphExtra)
library(maps)
library(mapproj)

str(USArrests)
head(USArrests)

library(tibble)

crime <- rownames_to_column(USArrests,var='state')
crime$state <- tolower(crime$state)

str(crime)

library(ggplot2)
states_map <- map_data('state')
str(states_map)

ggChoropleth(data=crime,
             aes(fill=Murder,map_id=state),
             map=states_map,)

ggChoropleth(data=crime,
             aes(fill=Assault,map_id=state),
             map=states_map,
             interactive=T)

library(RColorBrewer)
display.brewer.all()

library(kormaps2014)
library(ggiraphExtra)
library(maps)
library(mapproj)
library(tibble)
library(stringi)
library(ggplot2)
#changeCode �ѱ۹��� �����Լ� / ��� �ʵ带 ���ڷ� �ٲ㼭 ���ڵ� ���ڷ� �ٲ㼭 �񱳾����
#���ڷ� �Ǿ���� �ʵ带 as.integer ���

str(changeCode(korpop1))
head(changeCode(korpop1),10)
library(dplyr)

#�ʵ���� ����� �ٲ�
korpop1 <- rename(korpop1,
                  pop = ���α�_��,
                  name = ����������_���鵿)


korpop <- rename(korpop,
                 pop = ���α�_��,
                 name = ����������_���鵿)
korpop$pop <- as.integer(korpop$pop)

ggChoropleth(data = korpop,
             aes(fill=pop,
                 map_id=code,
                 tooltip = name),
             map=kormap1,
             interactive = T)

changeCode(korpop1)

korpop <- changeCode(korpop1)
head(korpop)

help("ggChoropleth")

a<- data.frame('name'=c('����Ư����','�λ걤����','�뱸������','��õ������',
                        '���ֱ�����','����������','��걤����','����Ư����ġ��',
                        '��⵵','������','��û�ϵ�','��û����','����ϵ�',
                        '���󳲵�','���ϵ�','��󳲵�','����Ư����ġ��'),
                        'pop'=c(as.integer(runif(17,100,200))),'code'=c(11,21,22,23,24,25,26,29,31,32,33,34,35,36,37,38,39))
a

ggChoropleth(data = a,
             aes(fill=num,
                 map_id=code,
                 tooltip = name),
             map=kormap1,
             interactive = T)

str(korpop)
str(kormap1)
korpop

a<-data.frame('name'=korpop$name,'num'=c(as.integer(runif(17,100,200))),'code'=korpop$code)

changeCode(korpop2)

kor2 <-changeCode(korpop2[startsWith(korpop2$code,'11'),
                          c('����������_���鵿','���α�_��','code')])

kor2 <- rename(kor2,pop=���α�_��, name=����������_���鵿)
kor2$pop <- as.integer(kor2$pop)
ggChoropleth(data = kor2,
             aes(fill=pop,
                 map_id=code,
                 tooltip = name),
             map=map2,
             interactive = T)

temp<-kormap2
temp$code <- as.character(temp$code)

map2<-temp[startsWith(temp$code,'21'),]

changeCode(korpop2)
view(changeCode(korpop2))

b<-changeCode(korpop2[startsWith(korpop2$code,'21'),c('����������_���鵿','���α�_��','code')],)
b<-rename(b,pop=���α�_��, name=����������_���鵿)
b$pop <- as.integer(b$pop)
ggChoropleth(data = b,
             aes(fill=pop,
                 map_id=code,
                 tooltip = name),
             map=map2,
             interactive = T)

b
