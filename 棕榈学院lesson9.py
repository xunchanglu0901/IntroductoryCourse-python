# -*- coding: utf-8 -*-
# 时间    : 2018/10/30 8:53
# 作者    : xcl

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import urllib.request
import json

# apply;map;lamba用法
# 从网站API接口获取股票数据

# 作业一
# 无法获得APIkey

# 作业二
df1 = pd.read_csv('AAPL_intraday_data.csv')
#print(df1.head())#前几行,默认为5
#print(df1.tail())#后几行
day1=df1.iloc[:390,:]
day1["hour"]=pd.to_datetime(day1["Unnamed: 0"],format="%H:%M:%S").dt.time
day1["Volume"] = day1["Volume"].apply(pd.to_numeric, errors = 'coerce')
#print(day1.head(10))#前几行,默认为5

#作业三
day1["Volume_pct1"] = day1["Volume"].pct_change()

day1["Volume_pct2"] = day1["Volume"].shift(1)/day1["Volume"]

day1["Volume_pct3"] =day1["Volume"].rolling(window=2).apply(lambda x:(x[1]-x[0])/x[0])

f = lambda x,y:x/y
#print(f(day1["Volume"],day1["Volume_pct2"] ))
day1["Volume_pct4"]=f(day1["Volume"],day1["Volume_pct2"] )

