# -*- coding: UTF-8 -*-

# Filename : 03-random.py
# author by : www.runoob.com

# 生成 0 ~ 9 之间的随机数

# 导入 random(随机数) 模块
import random

# 产生 0 到 1 之间的随机浮点数
print( "随机数 0-1 是：" )
x = random.random()
print (x)

# 产生 1 到 10 的一个整数型随机数
print( "随机数 1-10 是：")
print ( random.randint(1,10) )

# 产生  a 到 b 之间的随机浮点数，区间可以不是整数
a = 3.3
b = 10.7
c = random.uniform(a,b)
print( "在 %f - %f 之间的随机数是：%f" %(a, b, c) )

# 从序列中随机选取一个元素
d = "tomorrow"
e = random.choice(d)
print( "在字符串 %s 中随机挑选的字符是：%s" %(d, e)  )
