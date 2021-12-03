mosaicplot(Titanic, color=T)

library(ggplot2)

mpg<-ggplot2::mpg
ggplot(data=mpg,aes(x=displ, y=hwy))+geom_point()+xlim(3,6)+ylim(10,30)

mid<-ggplot2::midwest
ggplot(data=mid, aes(x=poptotal, y=popasian))+geom_point()+xlim(0,500000)+
  ylim(0,10000)

library(dplyr)
df_mpg<-mpg %>% group_by(drv) %>% summarize(mean_hwy=mean(hwy))
df_mpg

ggplot(data=df_mpg,aes(x=reorder(drv,-mean_hwy),y=mean_hwy))+geom_col()

devtools::install_github("ricardo-bion/ggradar")


help(ggradar)








