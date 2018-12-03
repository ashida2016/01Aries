# -*- coding: UTF-8 -*-

# Filename : 02-switching.py
# author by : （学员ID)

# 目的:
# 掌握基本的赋值，输入及输出方法
# 掌握 print 代入模式


# -------------------------------
# 练习一
# 用户输入
x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 创建临时变量，并交换
temp = x
x = y
y = temp

print('交换后 x 的值为: ')
print (x)
print('交换后 y 的值为: ')
print (y)
