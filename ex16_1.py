# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 21:41:49 2022

@author: limin
"""

from sys import argv

script,filename = argv #定义2个参数

print(f"We're going to erase {filename}")  #函数filename格式化为字符串
print("If you don't want that,hit CTRL-C(^C).") #打印字符串
print("IF you do want that,hit RETURN.")#打印字符串

input("?") #input函数，根据上面提示操作

print("Opening the file...")
target = open(filename,'w') #打开文件，写入

print("Truncating the file.Goodbye!")
target.truncate()  #清空目标文件

print("Now I'm going to ask you for three lines.") 

#输入数据
line1 = input("line 1: ") 
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
line = [line1,"\n",line2,"\n",line3]
target.writelines(line)   #writelines 可以传入字符串也可以传入一个字符序列（不能是数字序列）


print("And finally,we close it.")
target.close() #关闭文件，类似保存