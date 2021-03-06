# -*- coding: utf-8 -*-
"""Movie_Reccomendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YEofzunmJi8BpHxjaXAzXlJHPOUCx-8h

# **Lets Build Anime Reccomendation System**
"""

#import the libraries
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('/content/movie_data.csv')

df.head(3)

df.shape

columns = ['Actors','Director','Genre','Title']

df[columns].head(3)

df[columns].isnull().values.any()

def get_important_features(data):
  important_features = []
  for i in range(0, data.shape[0]):
    important_features.append(data['Actors'][i]+ ' '+ data['Director'][i] + ' ' + data['Genre'][i] + ' '+ data['Title'][i])

  return important_features

df['important_features'] = get_important_features(df)
df.head(3)

cm = CountVectorizer().fit_transform(df['important_features'])

cs = cosine_similarity(cm)
print(cs)

cs.shape

title = 'The Amazing Spider-Man'
movie_id = df[df.Title == title]['Movie_id'].values[0]

scores = list(enumerate(cs[movie_id]))

sorted_scores = sorted(scores, key=lambda x:x[1], reverse=True)
sorted_scores = sorted_scores[1:]
sorted_scores

j = 0
print("The 7 most recommended movies to ", title , " are:\n ")
for item in sorted_scores:
  movie_title = df[df.Movie_id == item[0]]['Title'].values[0]
  print(j+1,movie_title)
  j = j + 1
  if j > 6:
    break