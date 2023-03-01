# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:34:11 2022

@author: limin
"""

from sys import argv
from os.path import exists  #引入exists函数，如果文件存在，返回True，不存在返回False

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")  #打印复印文件名称，粘贴的文件名称

#we could do these two on one line, how?
in_file = open(from_file) #打开文件
indata = in_file.read()  #阅读文件（内容）

print(f"The input file is {len(indata)} bytes long") #len（），得到字符串的长度

print(f"Does the output file exist? {exists(to_file)}") #exist（）函数，文件存在返回True，不存在返回False
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input() #input上述字符串内容

out_file = open(to_file, 'w') #只写模式打开文件，若文件存在会被覆盖，不存在会创建
out_file.write(indata) #写入indata变量的内容

print("Alright, all done.")

#关闭，保存文件
out_file.close() 
in_file.close()