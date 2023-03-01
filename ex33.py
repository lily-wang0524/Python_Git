# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 21:25:10 2023

@author: limin
"""

i = 0 #初始值
numbers = [] #用于存储的空列表

while i < 6 : #当i小于6时，布尔值为True，运行以下代码块
    print(f"At the top i is {i}") #打印while循环开头的变量
    numbers.append(i)
    
    i = i + 1
    print("Numbers now: ",numbers) #打印while循环结尾值
    print(f"At the bottom i is {i}") #打印while循环结尾值
    
print("The numbers: ")

for num in numbers: #for循环
    print(num)