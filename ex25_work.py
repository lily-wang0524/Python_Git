# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 11:00:12 2023

@author: limin
"""
#split函数
a = "It's ***a cute dog."
b = "1+2+34+567+89"

print(a.split()) #分隔符为空格，分割所有
print(a.split("***",5)) #分隔符为***，分割成6个字符串，但是分隔符就一个，按分隔符数量分割

print(b.split())# 分隔符为空格，分割所有
print(b.split("+",3)) #分隔符为+，分割成4个字符串

#pop函数
c = ["apple","Cat","dog","pear","water","coka cola"]

print(c.pop()) #默认移除最后一个
print(c.pop(0))  #根据索引移除第一个
print(c.pop(-2)) #根据索引移除倒数第二个，在移除最后一个的基础上

#sorted函数
d = (1,5,3,2,6,9,7,0,5)
e = ["apple","Cat","dog","pear","water","juice"]
print(sorted(d)) #按顺序排序
print(sorted(e)) #按字母顺序排序
print(sorted(d,reverse = True)) #按逆序排序
print(sorted(e,reverse = True)) #按字母逆序排序

import ex25
help(ex25)
help(ex25.break_words)