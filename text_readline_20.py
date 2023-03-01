# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:39:42 2022

@author: limin
"""

print("What's this?",end = " ")
print("This is an apple.")

print("What's this?")
print("This is an apple.")

print("What's this?\n")
print("This is an apple.")

#不加end=""
file = open("test.txt",'r') #打开文件
read_a_line = file.readline() #逐行阅读
print(read_a_line)
read_a_line = file.readline()
print(read_a_line)

#加end=""
file = open("test.txt",'r') #打开文件
read_a_line = file.readline() #逐行阅读
print(read_a_line, end = "")
read_a_line = file.readline()
print(read_a_line)