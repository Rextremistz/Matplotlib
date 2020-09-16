# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 08:58:03 2020

@author: Andrew
"""

%reset -f
%clear

import csv
import pandas as pd
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
language_responses = data['LanguagesWorkedWith']

    
    # row = next(csv_reader)
    # print(row['LanguagesWorkedWith'].split(';'))
    
language_counter = Counter()
    
        
for response in language_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])
    
languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title('Most Popular Language')
# plt.ylabel('Language')
plt.xlabel('Popularity')

plt.tight_layout()

print(languages)
print(popularity)


# print(language_counter)

