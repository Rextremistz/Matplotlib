# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 23:29:58 2020

@author: Andrew
"""



from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# import data_gen 



plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data['total_1']
    y2 = data['total_2']

    plt.cla()
    
    plt.plot(x, y1, label = 'Channel 1')
    plt.plot(x, y2, label = 'Channel 2')
    
    plt.legend(loc='upper left')
    plt.tight_layout()
    
    
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.tight_layout()
plt.show()

