# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 22:29:18 2020

@author: Andrew
"""

%reset -f
%clear

import pandas as pd
import requests
import io
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

url = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/06-Histograms/data.csv'
r = requests.get(url).content
data = pd.read_csv(io.StringIO(r.decode('utf-8')))

ids = data['Responder_id']
ages = data['Age']


print(data)


bins = [10,20,30,40,50,60,70,80,90,100]


plt.hist(ages, bins = bins, edgecolor='black',log=True)


median_age = 29
color = '#fc4f30'

plt.axvline(median_age,color=color)

plt.legend()

plt.title('Histogram')
plt.xlabel('Age',fontsize=6)
plt.ylabel('Total Respondents',fontsize=6)
plt.tight_layout()

plt.rcParams['xtick.labelsize'] = 6
plt.rcParams['ytick.labelsize'] = 6