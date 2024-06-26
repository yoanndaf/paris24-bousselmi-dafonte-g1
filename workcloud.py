# -*- coding: utf-8 -*-
"""workcloud.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aRgRLw6lx296_zx5nEur8ViMp1kT9gzt
"""

#exercice 1
# author : Da Fonte
# state : ongoing

#exercice 2
# author : TD
# state : ongoing

!pip install pillow
import numpy as np 
from PIL import Image,ImageOps
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
from scipy.ndimage import gaussian_gradient_magnitude 

# Download the Shakespeare text from the desktop
file=open("desktop/WC/romeo.txt",'r')
text=file.read()

# Create the WordCloud
canvas_ _____=1920
canvas_ ____=1080 

# Generate wordcloud
wordcloud = ________ (width=canvas_width,height=canvas_height).generate(text)
wordcloud.to_file("simple_wordcloud.png") 
plt.figure(figsize = (10, 10), facecolor=None)

# Save the output wordcloud in png format
plt.imshow(wordcloud, interpolation='bilinear')

# Show the image output 
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.show() 

#--------additional tricks----
# By default wordcloud generates random patterns but you can fix the seed
# Generate wordcloud
# Replace 1 with any number to get different result
canvas_width=1920
canvas_height=1080 
wordcloud = WordCloud(width=canvas_width,height=canvas_height).generate(text)
wordcloud = WordCloud(random_state=1).generate(text) 
wordcloud.to_file("simple_wordcloud.png") 
plt.figure(figsize = (10, 10), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off") 
plt.tight_layout(pad = 0)
plt.show() 
