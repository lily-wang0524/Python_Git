# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:46:23 2023

@author: limin
"""

people = 20
cats = 30 
dogs = 15


if people < cats: #如果people小于cats则打印如下内容，否则跳过
    print("Too many cats! The world is doomed!")
    
if people > cats: #如果people大于cats则打印如下内容，否则跳过
    print("Not many cats! The world is saved!")

if people < dogs: #如果people小于dogs 则打印以下内容，否则跳过
    print("The world is drooled on!")
    
if people > dogs: #如果people大于dogs 则打印以下内容，否则跳过
    print("The world is dry!")
    
    
dogs += 5 #变量dogs = dogs + 5

if people >= dogs: #如果people大于等于dogs，则打印以下内容，否则跳过
    print("People are greater than or equal to dogs.")
    
if people <= dogs:  #如果people小于等于dogs，则打印以下内容，否则跳过
    print("People are less than or equal to dogs.")
    
if people == dogs: #如果people等于dogs，则打印以下内容，否则跳过
    print("People are dogs.")
    
