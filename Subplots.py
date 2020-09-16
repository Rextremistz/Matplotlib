# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 20:42:55 2020

@author: Andrew
"""

import pandas as pd
import requests
import io
from matplotlib import pyplot as plt



plt.gcf()
plt.gca()

plt.style.use('seaborn')

url = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/10-Subplots/data.csv'
r = requests.get(url).content
data = pd.read_csv(io.StringIO(r.decode('utf')))

ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols =2, sharey = True)

ax1.plot(ages, dev_salaries, color= '#444444',
         linestyle='--', label='All Devs')

ax2.plot(ages, py_salaries, label ='Python')
ax2.plot(ages, js_salaries, label ='JavaScript')

ax1.legend()
ax1.set_title('Median Salary by Age')
ax1.set_ylabel('Median Salary')
ax1.set_xlabel('Age')

ax2.legend()
ax2.set_xlabel('Age')


plt.tight_layout()

plt.show()

