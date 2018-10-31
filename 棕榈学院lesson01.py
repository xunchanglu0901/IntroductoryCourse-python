# -*- coding: utf-8 -*-
# 时间    : 2018/10/22 14:18
# 作者    : xcl

# 安装库
# CMD里运行代码 pip3 install pandas
# pandas为库名

data="C:\\Users\\Administrator\\Desktop\\data_all.txt"#设置文件路径
# 读取文件
'''
#方法一 open 方法
file = open(data,"r")#打开文件
print(file.read())
print(file.readlines()[2])
#方法二 使用for循环
file = open(data,"r")#r i.e. read
i=1
for line in file:
    print("read line",i)
    i=i+1
    print(line)
#上述方法同理可以用于csv格式的文件


# 写入文件
file = open(data,"w")#w i.e. write
file.write("hello world\n")#写入短语并换行
file.close()#关闭文件
file = open(data,"r")#w i.e. write
for line in file:
    print(line)
'''

'''
# 使用pandas读取文件
import pandas as pd#载入所需库
df = pd.read_csv("data.csv",index_col=0)#读取csv且设置索引列，从0开始数，0即第一列。
print(df)#输出表格
#同理有read_excel、read_table分别对应xlsx(xls)、txt文件

# 使用pandas存储文件
df.to_excel("路径")
'''

# 读取复杂txt数据
import pandas as pd
df = pd.read_table(data,sep=",",skiprows=[1,2,3],header=None,names=["a","b","c"],index_col=["index"],nrow=5)
#sep是分隔符设置
#skiprows跳过某几行，从0起数
#header则表示数据是否包含列名
#names重新设置列名
#index_col设置索引列
#nrows每几行每几行的读
print(df)#输出
