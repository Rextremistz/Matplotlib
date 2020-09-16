# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 18:49:38 2020

@author: Andrew
"""

%reset -f
%clear

import pandas as pd
import io
import requests
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

url = 'https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/08-TimeSeries/data.csv'
r = requests.get(url).content
data = pd.read_csv(io.StringIO(r.decode('utf-8')))

data['Data'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace = True)


price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle = 'solid')

# date_format = mpl_dates.DateFormatter('%b, %d %Y')

#get current format = gcf
plt.gcf().autofmt_xdate()

# plt.gca().xaxis.set_major_formatter(date_format())


print(data)

