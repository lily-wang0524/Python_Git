# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 20:48:50 2022

@author: limin
"""

from sys import argv

script, filename = argv   #argv导入参数

txt = open(filename)  #open（）函数，相当于鼠标点击文件

print(f"Here's your file {filename}:") #打印，变量filename变量格式化为字符串。
print(txt.read()) #read（）阅读文件

#print("Type the filename again:")
#file_again = input("> ")  #input输入文件名及路径
#
#txt_again = open(file_again) 
#
#print(txt_again.read())