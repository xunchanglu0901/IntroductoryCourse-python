# python入门课程
### lesson03
##### 　　zip()函数起到拉链作用，对两个或多个列表同位置元素进行对应匹配
##### 　　zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
##### 　　如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表
###### >>>a = [1,2,3]
###### >>> b = [4,5,6]
###### >>> c = [4,5,6,7,8]
###### >>> zipped = zip(a,b)     # 打包为元组的列表
###### [(1, 4), (2, 5), (3, 6)]
###### >>> zip(a,c)              # 元素个数与最短的列表一致
###### [(1, 4), (2, 5), (3, 6)]
###### >>> zip(*zipped)          # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
###### [(1, 2, 3), (4, 5, 6)]
###### for循序写字典，字典添加内容的方式比较特别，需要注意
###### B = [4, 7, 2, 6, 6, 8, 8, 10, 4]
###### C ={}
###### for i in set(B):
######     C[str(i)] = [B.count(i)]
######     #print([B.count(i)])
###### print(C)

### lesson04
##### 　　列表元素交换位置; 冒泡排序; "\*"三角形

### lesson05
##### 　　表格的创建,修改列名和索引
##### 　　按照条件切片,选择数据

### lesson06
##### 　　多种合并表格的方法;两种创建数据框的方法
##### 　　修改列名;插入新列
##### 　　替换内容格式:字符串,整数,浮点数,值

### lesson07
##### 　　画图的基本方法;seaborn样例

### lesson08
##### 　　更改数据的时间格式;并且使用.dt.time和dt.date进行时间和日期的分割
###### 如将 2018-08-08 12：12：12 分割为 2018-08-08 和 12：12：12
###### apple.index = pd.to_datetime(apple.index, format="%Y-%m-%d %H:%M:%S")
###### apple["Date"] = apple.index.date
###### apple["Time"] = apple.index.time
###### 其中apple.index = apple["index"]
##### 　　画图的高级方法;同一张图上多项指标;多幅图展示在同一张画板上
###### fig = plt.figure()
###### ax = fig.add_subplot(4,2,1)#尺寸4*2 位置1
##### 1)同一张图上多项指标
###### day1["High"].plot(label = 'High')
###### plt.legend()
###### plt.ylabel('Price')
###### ax = fig.add_subplot(4,2,1)
###### day1["Low"].plot(label = 'Low')
###### plt.legend()
###### plt.ylabel('Price')
###### plt.show()
##### 2)多幅图展示在同一张画板上
###### ax = fig.add_subplot(4,2,2)
###### day1["profit"]=day1["High"]-day1["Low"]
###### plt.bar(range(len(day1)),day1["profit"],label="profit")
###### plt.legend()
###### plt.ylabel("profit")
###### plt.show()

### lesson09
##### 　　apply;map;lamba用法
##### 　　使用.rolling(window=2)来配合apply,解决了lamba在一个/行/格变量下的限制
##### 　　注意:x[1]-x[0]等同于差分
##### 　　从网站API接口获取股票数据

### lesson10
##### 　　如何绘制蜡烛图
##### 　　蜡烛图常用于股票走势
