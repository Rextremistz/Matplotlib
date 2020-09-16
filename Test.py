# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 09:14:12 2020

@author: Andrew
"""

import pandas as pd
import csv
from urllib.request import urlopen
import codecs


url = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/02-BarCharts/data.csv'

with urlopen(url) as csv_file:
    csvfile = csv.reader(codecs.iterdecode(csv_file, 'utf-8'))
    for line in csvfile:
        print(line) #do something with line
