# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 21:13:15 2023

@author: limin
"""
people = 30
cars = 15 #原数值为40
trucks = 15


if cars > people: #条件不成立
    print("We should take the cars.")
elif cars < people: #条件成立
    print("We should not take the cars.")
else: #其中一个条件成立，不会转到这一步。
    print("We can't decide.")
    
if trucks > cars: #条件不成立
    print("That's too many trucks.")
elif trucks < cars: #条件不成立
    print("Maybe we could take the trucks.")
else: #以上条件都不成立，则运行以下内容
    print("We still can't decide.")
    
if people > trucks: #条件成立
    print("Alright,let's just take the trucks.")
else: #以上条件成立，不运行以下内容。
    print("Fine,let's stay home then.")
    
#附加练习3
if cars > people or trucks < cars:
    print("We could take the cars or trucks.")
elif cars < people or trucks > cars:
    print("There are too many trucks.")
else:
    print("We can't decide.")
 
#常见问题
if people < cars: #条件不成立
    print("We should take the cars.")
elif people > cars: #条件成立
    print("We should not take the cars.")
elif people > trucks: #条件成立，当elif只运行第一个成立的条件。
    print("Alright,let's just take the trucks.")
else: 
    print("Fine,let's stay home then.")
    
    
    