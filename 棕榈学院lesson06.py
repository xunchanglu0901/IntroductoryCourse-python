# -*- coding: utf-8 -*-
# 时间    : 2018/10/27 7:38
# 作者    : xcl

#多种合并表格的方法
#修改列名
#插入新列
#替换内容格式:字符串,整数,浮点数,值
#两种创建数据框的方法

#作业1
import pandas as pd
import numpy as np
d1=np.array([[1,2,3,4,"H"],[5,6,7,8,"J"],[9,10,11,12,"K"],[13,14,15,16,"L"]])
d1=pd.DataFrame(d1,columns=["A","B","C","D","E"],index=[0,1,2,3])
#print(d1)
d2={"1":["H","L","J","J"],"2":["S","S","S","T"],"3":["6","2","5","3"]}
d2=pd.DataFrame(d2,index=[0,1,2,3])

d1["key_0"]=(["H","J","J","K"])
d1=pd.DataFrame.append(d1,other=d1.loc[1],ignore_index=True)#插入一列
#print(d1)
d2["key_0"]=(["H","J","J","K"])
#print(d1,"\n",d2)
d3=pd.concat([d1,d2],sort=True,ignore_index=True,axis=1)
#print(d3)
d3.columns=["A"]+["B"]+["C"]+["D"]+["E"]+["key_0"]+["1"]+["2"]+["3"]+["del"]
#d3 = d3.astype({"A":'float','age':'int'})
#d3['A'] = d3["A"].map(lambda x:float(x))
d3['A'] = d3["A"].map(lambda x:int(x))
d3['3'] = d3["3"].map(lambda x:float(x))
d3=d3.sort_values(by="A")
del d3["del"]
print(d3)
'''
d3=pd.concat([d1,d2],axis=1,join="outer")
print(d3)
#参数join="inner"均有数据行 join="outer"全部行,无数据行用NaN替换
#join_axes=[d2.index]新合并的表格包含d2表中的索引行
#ignore_index=True忽略索引名
'''
d3=pd.merge(d1,d2,on="key_0")
#按key_0的值合并，非共有部分则舍弃

d3=pd.merge(d1,d2,on="key_0",how="outer")
#保留全部数据



#作业2
d1=np.array([[1,2,3,4,"H"],[5,6,7,8,"J"],[9,10,11,12,"K"],[13,14,15,16,"L"]])
d1=pd.DataFrame(d1,columns=["A","B","C","D","E"],index=[0,1,2,3])
d2={"1":["H","L","J","J"],"2":["S","S","S","T"],"3":["6","2","5","3"]}
d2=pd.DataFrame(d2,index=[0,1,2,3])

d3=d1.join(d2)
d3.loc[2]=d3.loc[1]
d3.index=["01","02","03","04"]
d3["3"]=([6.0,5.0,3.0,2.0])#可用for循环批量修改
#print(d3)


#print(d3.loc["02"]["2"])


#作业3
'''
L=[]
for i in ["01","02","03","04"]:
    if d3.loc[i]["2"]=="S":
        p1= d3.loc[i]["B"]
        p2=d3.loc[i]["C"]
        p3=d3.loc[i]["3"]
        p1=float(p1)
        p2 = float(p2)
        p3 = float(p3)
        p = p1+p2-p3
        L.append(p)
    elif d3.loc[[i], ["2"]].values == "T":
        p1 = d3.loc[i]["B"]
        p2 = d3.loc[i]["C"]
        p3 = d3.loc[i]["3"]
        p1 = float(p1)
        p2 = float(p2)
        p3 = float(p3)
        p = p1 - p2 + p3
        L.append(p)
L=pd.DataFrame(L)
d3=d3.reset_index()
result=pd.concat([d3["2"],L],axis=1,ignore_index=True)
result.columns=["type"]+["value"]#修改列名
print(result)
'''
