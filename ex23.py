# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:17:48 2022

@author: limin
"""

#encode编码-----decode解码
import sys
script, encoding,error = sys.argv


def main(language_file, encoding,errors):
    line = language_file.readline()     #按行阅读文件
    
    if line:    #当line有内容时会返回True
        print_line(line,encoding,errors)    #运行自定义的print_line函数
        return main(language_file, encoding,errors) #返回main（）函数
    
def print_line(line, encoding, errors):
    next_lang = line.strip()   #strip（）函数：删除字符串前导和后面的空格
    raw_bytes = next_lang.encode(encoding, errors = errors) #encode（）函数编码。
    cooked_string = raw_bytes.decode(encoding, errors = errors) #decode（）函数解码
    
    
    print(raw_bytes, "<===>", cooked_string)
    
    
languages = open("C:\\Users\limin\Desktop\Python3_exercises\ex23.txt", encoding = "utf-8")

main(languages,encoding,error)