# -*- coding: utf-8 -*-
# 时间    : 2018/10/26 16:37
# 作者    : xcl


#表格的创建,修改列名和索引
#按照条件切片,选择数据

import pandas as pd
import numpy as np
# 作业1
s1=[1,2,3,4,5]
s1 =pd.Series(s1,index=["h","i","j","k",'l'])
#print(s1)
s1["j"]=8
s1["l"]=np.NAN
s1=pd.DataFrame(s1)
#print(s1)

#作业2
#构建方法一
s2=np.random.seed(108)
s2=np.random.rand(16)
s2=s2.reshape(4,4)
s2=pd.DataFrame(s2,columns=["A","B","C","D"])
#print(s2)
s3=np.random.seed(108)
s3=np.random.rand(16)
s3=s3.reshape(4,4)
s3=pd.DataFrame(s3,columns=["A","B","C","D"],index=["18-1","18-2","18-3","18-4"])
print(s3)
#print(s3[["B","C"]]["18-1":"18-2"])
#构建方法二
s3=np.random.seed(108)
s4=np.array([np.random.random(4),np.random.random(4),np.random.random(4),np.random.random(4)])
s4=pd.DataFrame(s4,columns=["A","B","C","D"],index=["18-1","18-2","18-3","18-4"])
print(s4)
#作业3
df=pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],columns=["A","B","C","D"],index=[0,1,2,3])
#print(df[df["A"]>3])
#print(df[df["A"]<9])
#print(df[(df["A"]<9) & (df["A"]>3)]).
#print(df[(df<9) & (df>3)])

#print(s2[["A","B","C","D"]][2:3])
#print(s2[(s2["A"]>0.5) & (s2["A"]<0.6)])
