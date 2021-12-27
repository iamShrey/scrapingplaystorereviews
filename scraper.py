from google_play_scraper import app
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

from google_play_scraper import Sort, reviews_all


us_reviews = reviews_all(
    'io.chingari.app',
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.MOST_RELEVANT
)

df_busu = pd.DataFrame(np.array(us_reviews),columns=['review'])


df_busu = df_busu.join(pd.DataFrame(df_busu.pop('review').tolist()))


df_busu
df = df_busu.content
 
comment_words = ''
stopwords = set(STOPWORDS).union({'App','taxes','tax'})
 
# iterate through the csv file
for val in df:
     
    # typecaste each val to string
    val = str(val)
 
    # split the value
    tokens = val.split()
     
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    comment_words += " ".join(tokens)+" "
 
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
 
# plot the WordCloud image                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()
