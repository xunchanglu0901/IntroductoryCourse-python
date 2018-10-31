# -*- coding: utf-8 -*-
# 时间    : 2018/10/23 13:43
# 作者    : xcl

# 数据类型
# int  float  string   bool
# type 查看数据类型
'''
x = 1
x = 1.2
x = "hello"
x = True
print(type(x))
'''
# 赋值
'''
#x =1 #把1赋给x
x,y= 15,1.5
x,y=[1,22]
x,y="24","22"
print(x,y)
'''
# 逻辑变量
'''
B = 3 == 4
print(B)
'''
# 数据类型之间的变换
'''
x = 1.7
y = str(x)
y = float(x)
y = int(x)#向下取整
print(y)

# 变量的基本运算
x = 2
y = 3
# + - * /
x = "hello"
y = ",python"
#print(x+y,x*3)
x = 2
x += 7#累加 再加七
      #加号在左边
print(x**2)
#等价于
print(pow(x,2))
# 取几位小数
print(round(x+1.2324,3))
# int 向下取整
# abs 取绝对值

# 部分特殊运算
import math
print(math.log(12,24),math.sqrt(15),math.atan(24),math.e,math.pi)
'''
import math
print(sum([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]))
print(math.fsum([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]))
'''
