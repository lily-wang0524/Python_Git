# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:12:47 2023

@author: limin
"""

numbers = []

for i in range(0,6):
    print(f"At the top i is {i}") #打印while循环开头的变量
    numbers.append(i)
    print("Numbers now: ",numbers) #打印while循环结尾值
    #若不去掉增加值
    i = i+1
    print(f"At the bottom i is {i}") #打印while循环结尾值

print("The numbers: ")

for num in numbers: #for循环
    print(num)