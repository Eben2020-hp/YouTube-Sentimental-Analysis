# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 08:31:13 2021

@author: Eben Emmanuel
"""

#Data processing packages
import pandas as pd
import numpy as np
pd.set_option('display.max_colwidth', 200)

#Visualization packages
import matplotlib.pyplot as plt
import seaborn as sns

#NLP packages
from textblob import TextBlob

import warnings
warnings.filterwarnings("ignore")

##df = pd.read_csv(r'D:\USER\Desktop\PYTHON CLASS\comments.csv') --> For Spyder
df = pd.read_csv('comments.csv')
df.head()

#Calculating the Sentiment Polarity
pol=[] # list which will contain the polarity of the comments
for i in df.comment.values:
    try:
        analysis =TextBlob(i)
        pol.append(analysis.sentiment.polarity)
        
    except:
        pol.append(0)


#Adding the Sentiment Polarity column to the data
df['pol']=pol

#Converting the polarity values from continuous to categorical
df['pol'][df.pol==0]= 0
df['pol'][df.pol > 0]= 1
df['pol'][df.pol < 0]= -1


df.pol.value_counts()

sentiment = ['positive', 'neutral', 'negative']
counts = [88,19,0]


# Passing the parameters to the bar function, this is the main function which creates the bar plot
plt.bar(sentiment, counts, width= 0.9, align='center',color='cyan', edgecolor = 'red')

# This is the location for the annotated text
i = 20
j = 30

# Annotating the bar plot with the values (count)
for i in range(len(sentiment)):
    plt.annotate(counts[i], (-0.1 + i, counts[i] + j))
    
# Creating the legend of the bars in the plot
plt.legend(labels = ['Counts'])

# Giving the tilte for the plot
plt.title("Bar plot representing the Count of each Sentiment")

# Namimg the x and y axis
plt.xlabel('Sentiment')
plt.ylabel('Counts')

# Saving the plot as a 'png'
#plt.savefig('1BarPlot.png')
# Displaying the bar plot
plt.show()