# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 14:44:02 2023

@author: limin
"""

def while_loop1(a,n): #定义2个参数，a为最大不超过的数值，n为步长
    numbers = [] #用于存储的空列表
    
    i = 0
    while i < a : #当i小于a时，布尔值为True，运行以下代码块
        print(f"At the top i is {i}") #打印while循环开头的变量
        numbers.append(i)
    
        i = i + n #每次循环i的步长为n
        print("Numbers now: ",numbers) #打印while循环结尾值
        print(f"At the bottom i is {i}") #打印while循环结尾值
    return numbers #返回number值,return与while平齐，不然无法执行while循环

b = int(input("The top of numbers is: "))
m = int(input("The step size is:"))

numbers = while_loop1(b,m)
for num in numbers:
    print(num)