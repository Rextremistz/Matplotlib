# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:22:40 2020

@author: Andrew
"""

%reset -f
%clear

from matplotlib import pyplot as plt
import matplotlib as mpl


plt.style.use("fivethirtyeight")

slices = [5833, 7201, 7331, 7920, 18017,
          18523, 20524, 23030, 27097, 31991, 
          35917, 36443, 47544, 55466, 59219]
labels = ['Assembly', 'Go', 'Ruby', 'Other(s):', 'C',
          'TypeScript', 'C++', 'PHP', 'C#', 'Bash/Shell/PowerShell', 
          'Java', 'Python', 'SQL', 'HTML/CSS', 'JavaScript']
# colors = ['#008fd5','#fc4f30','#e5ae37','#6d904f']


slices.reverse()
labels.reverse()
# sorted(range(len(slices)), key=lambda i: slices[i])[5:]

# sorted(range(len(labels)), key=lambda i: slices[i])[5:]

explode = [0,0,0,0.5,0]

mpl.rcParams['font.size'] = 8

plt.pie(slices[0:5], labels=labels[0:5], explode = explode, shadow=True,
        startangle=90,autopct='%1.1f%%', wedgeprops = {'edgecolor':'black'})

plt.title('Pie Chart')
plt.tight_layout()
plt.show()

# print(plt.style.available)

# mpl.rcParams.keys()
