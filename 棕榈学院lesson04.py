# -*- coding: utf-8 -*-
# 时间    : 2018/10/25 15:46
# 作者    : xcl

#作业1 三角形
d = "*\n"
for i in {2,3,4,5}:
    c = "*"*i+"\n"
    d += c
print(d)

d = "******\n"
for i in [4,3,2,1]:
    c = "*"*i+"\n"
    d += c
print(d)

#作业2.1 列表元素交换位置
'''
L = [7,3,2,6,4,0,1,5]
n = len(L)

for l in range(0,n-1):
    if L[l] > L[l+1]:
        print("大于")
    #elif：
        # 条件
    else:
        print("小于")

'''

'''
for l in range(0,n-1):
    for j in range(0,n-1):
        if L[l] <  L[j]:
            print(L[l])

#方法一
import pandas as pd
L=pd.Series(L)
print(L[L.idxmin()])
#方法二
#xx=pd.DataFrame(L)
#print(xx.loc[xx.idxmin()])


#作业2.2
L2 =[7,3,2,6,4,0,1,5]

'''
'''
for l in range(0,n-1):
    if L2[l] > L2[l+1]:
       L2[l],L2[l+1]= L2[l+1],L2[l]
       #print(L2)
    #elif：
        # 条件
    else:
        print("符合题目条件,不交换")
print(L2)
#作业2.3 冒泡排序
#方法一
L2 =[7,3,2,6,4,0,1,5]
for l in range(0,n):
    for j in range(l+1,n):
        if L2[l] > L2[j]:
            L2[l],L2[j]= L2[j],L2[l]
    #elif：
        # 条件
print(L2)
#方法二
def bubble_sort(x):
    return sorted(x)
OUTCOME=bubble_sort(L2)
print(OUTCOME)
'''
'''
#作业3.1
'''
'''
for i in range(1,10):
 if i%2 == 0: #这里指的是 i 除以 2 是不是有余数
    break #结束整个循环,不执行print也不继续执行for，因此只print出上一个i
 print(i)

for i in range(1,10):
 if i%2 == 0: #这里指的是 i 除以 2 是不是有余数
    pass # do nothing 什么也不做
 print(i)

for i in range(1,10):
 if i%2 == 0: #这里指的是 i 除以 2 是不是有余数
    continue #结束本次循环,不执行本次的print
 print(i)
'''
'''
#作业3.2 冒泡排序
L2 =[7,3,2,6,4,0,1,5]
for l in range(0,n):
    for j in range(l+1,n):
        if L2[l] > L2[j]:
            L2[l],L2[j]= L2[j],L2[l]
        else:
            continue
    #elif：
        # 条件
print(L2)
'''
