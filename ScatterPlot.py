# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 14:07:51 2020

@author: Andrew
"""

%reset -f
%clear

import pandas as pd
import requests
import io
from matplotlib import pyplot as plt

plt.style.use('seaborn')

url = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/07-ScatterPlots/2019-05-31-data.csv'
r = requests.get(url).content
data = pd.read_csv(io.StringIO(r.decode('utf-8')))

view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, c = ratio, cmap = 'summer',
            edgecolor='black',linewidth = 1, alpha = 0.75)

cbar = plt.colorbar()
cbar.set_label = ('like/dislike ratio')

plt.xscale('log')
plt.yscale('log')


plt.title('Trending Youtube')
plt.xlabel('view counts')
plt.ylabel('likes')

plt.tight_layout()