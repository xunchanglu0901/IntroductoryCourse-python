# -*- coding: utf-8 -*-
# 时间    : 2018/10/29 13:26
# 作者    : xcl

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

#作业一
df1 = pd.read_csv('AAPL_intraday_data.csv')
#print(df1.head())#前几行,默认为5
#print(df1.tail())#后几行
day1=df1.iloc[:390,:]
#作业二
#方法一
'''
day1.columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
day1.index=day1["Date"]
print(day1.index)
del day1["Date"]
day1["Close"].plot()
plt.show()
'''
#方法二
'''
day1.columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
day1.index=day1["Date"]
#print(day1.index)
k=list(range(0,390,30))
plt.plot(day1.index,day1["Close"])
plt.xticks(day1.index[k],day1["Date"][k])
plt.show()
'''
#方法三
'''
day1.columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
day1.index=day1["Date"]
day1["Date"]=pd.to_datetime(day1["Date"],format="%H:%M:%S").dt.time
plt.plot(day1["Date"],day1["Close"])
plt.show()
'''

#作业三
day1.columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
day1.index=day1["Date"]
day1["Date"]=pd.to_datetime(day1["Date"],format="%H:%M:%S").dt.time
fig = plt.figure()
ax = fig.add_subplot(4,2,1)#尺寸4*2 位置1
day1["High"].plot(label = 'High')
plt.legend()
plt.ylabel('Price')
ax = fig.add_subplot(4,2,1)
day1["Low"].plot(label = 'Low')
plt.legend()
plt.ylabel('Price')
#plt.show()

ax = fig.add_subplot(4,2,2)
day1["profit"]=day1["High"]-day1["Low"]
#print(day1["profit"])
plt.bar(range(len(day1)),day1["profit"],label="profit")
plt.legend()
plt.ylabel("profit")
plt.show()
