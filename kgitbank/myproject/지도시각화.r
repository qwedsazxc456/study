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
#changeCode 한글문자 설정함수 / 모든 필드를 문자로 바꿔서 숫자도 문자로 바꿔서 비교어려움
#숫자로 되어야할 필드를 as.integer 사용

str(changeCode(korpop1))
head(changeCode(korpop1),10)
library(dplyr)

#필드명을 영어로 바꿈
korpop1 <- rename(korpop1,
                  pop = 총인구_명,
                  name = 행정구역별_읍면동)


korpop <- rename(korpop,
                 pop = 총인구_명,
                 name = 행정구역별_읍면동)
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

a<- data.frame('name'=c('서울특별시','부산광역시','대구광역시','인천광역시',
                        '광주광역시','대전광역시','울산광역시','세종특별자치시',
                        '경기도','강원도','충청북도','충청남도','전라북도',
                        '전라남도','경상북도','경상남도','제주특별자치도'),
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
                          c('행정구역별_읍면동','총인구_명','code')])

kor2 <- rename(kor2,pop=총인구_명, name=행정구역별_읍면동)
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

b<-changeCode(korpop2[startsWith(korpop2$code,'21'),c('행정구역별_읍면동','총인구_명','code')],)
b<-rename(b,pop=총인구_명, name=행정구역별_읍면동)
b$pop <- as.integer(b$pop)
ggChoropleth(data = b,
             aes(fill=pop,
                 map_id=code,
                 tooltip = name),
             map=map2,
             interactive = T)

b
