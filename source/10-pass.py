# -*- coding: UTF-8 -*-

# Filename : 10-pass.py
# author by : （学员ID)

# 目的:
# 汇总掌握01-09的知识点

# 导入 random(随机数) 模块
import random
import datetime


# 生成第一个人物 ID，武力值，并准备成字符串
id = random.randint(1000, 1999)
force_value = random.randint(10, 100)
character = "第一个角色id=" + str(id) + " 武力值=" + str(force_value) + "\n"

# 写文件
filename = "test.txt"
f = open(filename, 'w')  # write 方式第一次写一行
text2write = character
f.write(text2write)
f.close()

#生成 n 个人物ID及武力值
# 打开文件准备写入
filename = "test.txt"
f = open(filename, 'a')  # 追加方式一次加一行

# 生成 n 个 人物并写入文件
for i in range(1, 100):
    # 生成第 i 个人物 ID，武力值，并准备成字符串
    id = random.randint(2000, 2999)
    force_value = random.randint(10, 100)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #character = "日期时间：" + str(now) + "角色id=" + str(id) + " 武力值=" + str(force_value) + "\n"
    character = "日期时间：" + now + " 角色id=" + str(id) + " 武力值=" + str(force_value) + "\n"

    # 写入一个人物
    text2write = character
    f.write(text2write)

# 关闭文件
f.close()
