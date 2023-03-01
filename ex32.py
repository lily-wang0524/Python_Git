# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 21:00:15 2023

@author: limin
"""

#for-loop,for循环以及存储容器列表[]
the_count = [1,2,3,4,5] #列表内容可以是数字
fruits = ['apples', 'oranges', 'pears','apricots']#列表内容为字符串
change = [1, 'pennies',2, 'dimes', 3, 'quarters'] #列表内容可以为字符串和数字

# this first kind of for-loop goes through a list
for number in the_count: #for循环的值the_count列表中，变量number依次遍历列表中的内容
    print(f"This is count {number}") #打印表中内容
    
# same as above
for fruit in fruits:  #原理同上
    print(f"A fruit of type: {fruit}")
    
# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change: #原理同上
    print(f"I got {i}")
    
# we can also build lists, first start with an empty one
elements = [] #新建空列表变量

# then use the range function to do 0 to 5 counts
for i in range(0, 6): # (0,6)是指0<=i<6循环，循环6次
    print(f"Adding {i} to the list.")
# append is a function that lists understand
    elements.append(i) #向列表elements添加元素
    
# now we can print them out too
for i in elements:
    print(f"Elements was: {i}")
