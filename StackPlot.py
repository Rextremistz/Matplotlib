# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 22:07:28 2020

@author: Andrew
"""


from matplotlib import pyplot as plt
import matplotlib as mpl

plt.style.use('fivethirtyeight')

minutes = [1,2,3,4,5,6,7,8,9]

player1 = [1,2,3,3,4,4,4,4,5]
player2 = [1,1,1,1,2,2,2,3,4]
player3 = [1,1,1,2,2,2,3,3,3]

labels = ['player1','player2','player3']

plt.stackplot(minutes, player1, player2, player3, labels = labels)

plt.legend(loc = (0.05,0.75))

mpl.rcParams['legend.fontsize'] = 8
mpl.rcParams['xtick.labelsize'] = 8
mpl.rcParams['ytick.labelsize'] = 8
# mpl.rcParams.keys()



plt.title('StackPlot')
plt.tight_layout()
plt.show()