# -*- coding: utf-8 -*-
# 时间    : 2018/10/24 18:58
# 作者    : xcl

# 随机数

import numpy as np
'''
#生成相同随机数
np.random.seed(0)
data1=np.random.randn(40)
np.random.seed(0)
data2=np.random.randn(40)
print(data1,"\n",data2)
#生成正太分布
data2=np.random.normal(50,1,26)#均值 标准差 数量
print(data2)
'''

# 作业1
'''
#方法一
a = np.random.randn(40)
a.sort()
print(a)
print(a[-10:40])
#方法二
b=sorted(a,reverse=True)
print(b[0:10])#切片中到十但是不输出十
'''

#作业2
B = [4,7,2,4,8,8,10,4] #修改成 B = [4,7,2,6,6,8,8,10,4]
B[3]=6
B.insert(4,6)#插入
#print(B)

#作业3
c=[]
import pandas as pd
B=[str(i) for i in B]
for i in B:
    d = B.count(i)#统计B中元素频数
    c.append([d])
c = zip(B,c)
c = dict(c)#转换成字典格式
print(c)
