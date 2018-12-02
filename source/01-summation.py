# -*- coding: UTF-8 -*-

# Filename : 01-summation.py
# author by : （学员ID)

# 目的:
# 掌握基本的赋值，加减乘除运算，输入及输出方法


# -------------------------------
# 练习一
# 用户输入两串文字后合并输出
# 注：input() 返回一个字符串
text1 = input('输入第一串文本：')
text2 = input('输入第二串文本：')

# 求和
text3 = text1 + text2

# 显示计算结果
print('新的字符串相加结果为： {0}'.format(text3))

# -------------------------------
# 练习二
# 用户输入数字
# 注：input() 返回一个字符串，所以我们需要使用 float() 方法将字符串转换为数字
num1 = float(input('输入第一个数字：'))
num2 = float(input('输入第二个数字：'))

# 求和
sum = num1 + num2
# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))

# 求差
sum = num1 - num2
# 显示计算结果
print('数字 {0} 和 {1} 相减结果为： {2}'.format(num1, num2, sum))

# 求积
sum = num1 * num2
# 显示计算结果
print('数字 {0} 和 {1} 相乘结果为： {2}'.format(num1, num2, sum))

# 求除
sum = num1 / num2
# 显示计算结果
print('数字 {0} 和 {1} 相除结果为： {2}'.format(num1, num2, sum))
