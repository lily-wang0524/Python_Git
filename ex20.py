# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:51:52 2022

@author: limin
"""

from sys import argv  #调用argv函数

script, input_file = argv  #定义argv函数的列表中第0个参数为script，第二个参数为input_file

#创建函数，函数功能是阅读文件
def print_all(f):
    print(f.read())
    
#创建函数，功能：文件中的光标位于文件首位
def rewind(f):
    f.seek(0)

#创建函数，功能：按行阅读文件   
def print_a_line(line_count,f):
    print(line_count,f.readline())
    
current_file = open(input_file)  #打开文件，并赋值给current_file

print("First let's print the whole file:\n")

print_all(current_file) #调用函数，阅读文件

print("Now let's rewind,kind of like a tape.") #打印，像磁带一样倒带

rewind(current_file) #调用函数，将光标移到文件首位

print("Let's print three lines:")

current_line = 1  #创建变量，并赋值
print_a_line(current_line, current_file)  #调用函数，按行阅读文件

current_line = current_line + 1 #函数赋值，在原来的值上做计算
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

