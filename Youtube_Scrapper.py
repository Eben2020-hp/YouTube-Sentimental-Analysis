# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 23:33:55 2021

@author: Eben Emmanuel && Rupal Dsouza
"""

import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

data=[]

with Chrome(executable_path=r'D:\USER\Desktop\chromedriver.exe') as driver:
    wait = WebDriverWait(driver,15)
    driver.get("https://www.youtube.com/watch?v=ugQ2hU92Ffk&t=2s")

    for item in range(2): 
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
        time.sleep(15)

    for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
        data.append(comment.text)
        
import pandas as pd
df = pd.DataFrame(data, columns=['comment'])
df.head()














import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS) 

#convert list to string and generate
unique_string=(" ").join(data)
wordcloud = WordCloud(width = 1000, height = 500, stopwords = stopwords).generate(unique_string)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("your_file_name"+".png", bbox_inches='tight')
plt.show()
plt.close()
