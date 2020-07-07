import wikipedia
import sys
import numpy as np
from PIL import Image
from wordcloud import WordCloud  , STOPWORDS
import cv2

x=str(input('Enter the title : '))
title=wikipedia.search(x)[0]
page=wikipedia.page(title)
text=page.content

#print(text)

background = np.array(Image.open('cloud.png'))
stopwords = set(STOPWORDS)

wc = WordCloud(background_color = 'white',max_words=244,mask=background,
               stopwords = stopwords)

wc.generate(text)
wc.to_file('word_cloud.png')

img=cv2.imread('word_cloud.png')
cv2.imshow("Word Cloud",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
