#pip install wordcloud  

from wordcloud import WordCloud

cloud = WordCloud(
    font_path="./fonts/HYBDAL.TTF"
)

f=open('./황선우.txt','r',encoding='utf8')
text=f.read()
f.close()
wordcloud = cloud.generate(text)

image = wordcloud.to_image()
image.show()
