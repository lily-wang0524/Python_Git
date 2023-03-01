# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 23:19:37 2023

@author: limin
"""

people = 30
cars = 40
trucks = 15


if cars > people: #如果变量cars大于变量people，则运行以下内容，否则跳过。
    print("We should take the cars.")
elif cars < people: #如果变量cars小于变量people，则运行以下内容，否则跳过。
    print("We should not take the cars.")
else: #如果以上条件都不成立，则打印以下内容
    print("We can't decide.")
    
if trucks > cars: #如果变量trucks大于变量cars，则运行以下内容，否则跳过。
    print("That's too many trucks.")
elif trucks < cars: #如果变量trucks小于变量cars，则运行以下内容，否则跳过。
    print("Maybe we could take the trucks.")
else: #如果以上条件都不成立，则运行以下内容
    print("We still can't decide.")
    
if people > trucks: #如果变量people大于变量trucks，则运行以下内容，否则跳过。
    print("Alright,let's just take the trucks.")
else: #如果以上条件不成立，则运行以下内容。
    print("Fine,let's stay home then.")
    