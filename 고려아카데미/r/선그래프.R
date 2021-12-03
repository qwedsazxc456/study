ggplot(data=economics, aes(x=date, y=unemploy))+
  geom_line()

# 연습
ggplot(data=economics, aes(x=date, y=psavert))+
  geom_line()
