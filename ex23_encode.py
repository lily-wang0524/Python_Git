# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 22:36:45 2022

@author: limin
"""

a = "Python世界"
a_utf8 = a.encode(encoding = 'utf-8',errors = 'strict') #使用utf-8惯例编码
a_gbk = a.encode(encoding = 'GBK',errors = 'strict') #使用gbk惯例编码

print(a)
print("UTF-8编码：",a_utf8)#打印
print("GBK编码：", a_gbk)

print("UTF-8解码：", a_utf8.decode(encoding = "utf-8",errors = "strict")) #使用utf-8解码
print("GBK解码：",a_gbk.decode(encoding = 'GBK',errors = 'strict')) #使用GBK解码