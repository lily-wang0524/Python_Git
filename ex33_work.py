# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 22:13:34 2023

@author: limin
"""

def while_loop(a):
    numbers = [] #用于存储的空列表
    
    i = 0
    while i < a : #当i小于a时，布尔值为True，运行以下代码块
        print(f"At the top i is {i}") #打印while循环开头的变量
        numbers.append(i)
    
        i = i + 1
        print("Numbers now: ",numbers) #打印while循环结尾值
        print(f"At the bottom i is {i}") #打印while循环结尾值
    return numbers #返回number值,return与while平齐，不然无法执行while循环

a = int(input("The top of numbers is:"))
numbers = while_loop(a)
        
print("The numbers: ")
for num in numbers: #for循环
    print(num)

