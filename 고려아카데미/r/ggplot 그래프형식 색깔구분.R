library(ggplot2)

qplot(data=mpg , x = hwy) 

qplot(data=mpg, y=hwy, x=drv, geom='point') # geom 그래프형식
qplot(data=mpg, y=hwy, x=drv, geom='boxplot', colour=drv) # colour 색깔 구분
