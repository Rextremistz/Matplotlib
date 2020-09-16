# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:01:00 2020

@author: Andrew
"""



%reset -f
%clear

import pandas as pd
import io
import requests
from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')

url = ('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/05-Fill_Betweens/data.csv')
r = requests.get(url).content
data = pd.read_csv(io.StringIO(r.decode('utf-8')))

ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color ='red', linestyle = '--', label = 'All Devs')
plt.plot(ages, py_salaries, color ='green', label = 'Python')


overall_median = 57287


plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries > dev_salaries),
                 interpolate = True, color = 'green',
                 label = 'Above AVG', alpha = 0.25)



plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries <= dev_salaries),
                 interpolate = True, color = 'red',
                 label = 'Below AVG', alpha = 0.25)



plt.legend(prop={'size':8}, loc= 2)


#1st way font size
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

#2nd way font size
# font = {'family' : 'normal',
#         'weight' : 'bold',
#         'size'   : 12}

# plt.rc('font', **font)

#3rd way font size
# mpl.rc()


plt.title('Line Plot')
plt.ylabel('Salary', fontsize = 10)
plt.xlabel('Age', fontsize = 10)
plt.tight_layout()
plt.show()