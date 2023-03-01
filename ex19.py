# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 21:12:49 2022

@author: limin
"""

#创建函数cheese_and_crackers，其中参数为cheese_count和boxes_of_crackers.
def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")   #打印，字符串化cheese_count参数
    print(f"You have {boxes_of_crackers} boxes 0f crackers!")  #打印, 字符串格式化参数boxes_of_crackers
    print("Man that's enough for a party!") #打印
    print("Get a blanket.\n") #打印，\n转义字符，换行
    
    
print("We are just give the function numbers directly:")
cheese_and_crackers(20,30)  #直接写入参数的方式调用函数

print("OR,we can use variables from our script:")
amount_of_cheese = 10  #定义变量
amount_of_crackers = 50  #定义变量

cheese_and_crackers(amount_of_cheese,amount_of_crackers) #定义变量作为参数调用函数


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)  #参数可以进行数学计算


print("And we can combine the two, variables and math:") 
#参数可以同时使用变量与数字
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) 

