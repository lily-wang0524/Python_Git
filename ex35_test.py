# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 21:34:23 2023

@author: limin
"""
from sys import exit
def gold_room(): 
    print("This room is full of gold. How much do you take?")
    
    choice = int(input("> "))
    # if "0" in choice or "1" in choice: #choice变量中的字符串含有字符串“0”或者字符串“1”时成立
    #     how_much = int(choice) #将字符串转化为数字
    # else:
    #     dead("Man,learn to type a number.")  #调用代码后段的自定义函数dead（）
        
    if choice < 50: 
        print("Nice, you're not greedy, you win!")
        exit(0) #无错误退出.
    else:
        dead("You greedy bastard!") #调用代码后段的自定义函数dead（）

def dead(why):
    print(why, "Good job!")
    exit(0)

x = 2
y = 3
xy = lambda x, y: x * y
print(xy(2,3))

print(type(18))
print(type(True))
print(type(16.8))

print("%d"%45)