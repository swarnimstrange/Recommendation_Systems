# -*- coding: utf-8 -*-
"""manga_reccomendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/150WtH8gw86T0RZmDTTcmeDtZZRCgkEnf
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df=pd.read_csv("/content/manga_data.csv")

df.head(3)

df.shape

columns =['English Title' , 'Synonims Titles', 'Type' , 'Genres', 'Author', 'Serialization' ]

df[columns].head()

df.isnull().values.any()

def similar(data):
  features = []
  for i in range(0,data.shape[0]):
    features.append( data['English Title'][i] + ' ' + data['Synonims Titles'][i] + ' ' + data['Type'][i] + ' ' + data['Genres'][i] + ' ' + data['Author'][i] + ' ' + data['Serialization'][i] )

  return features

df['features'] = similar(df)

df.head(3)

cm = CountVectorizer().fit_transform(df['features'])

cs = cosine_similarity(cm)
cs.shape

print(cs)

name = 'Fullmetal Alchemist'
manga_id = df[df['English Title'] == name]['Manga ID'].values[0]
manga_id

scores = list(enumerate(cs[manga_id]))
print(scores)

sorted_scores = sorted(scores, key=lambda x:x[1], reverse= True)
sorted_scores = sorted_scores[1:]
sorted_scores

j=0
print("\nTop 7 Reccomended Movie to " + name + " are: \n")
for item in sorted_scores:
  manga_title = df[df['Manga ID'] == item[0]]['English Title'].values[0]
  print(j+1, manga_title)
  j = j + 1
  if j > 6:
    break