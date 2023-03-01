# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 10:32:46 2023

@author: limin
"""

from sys import exit  #sys.exit是退出程序的方法

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
        
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False #先给变量bear_moved赋值布尔值False
    
    while True:  #while True 需要有能够跳出循环的方法，如break，否则会一直循环
        choice = input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face") #熊看着你并攻击你的脸
        elif choice == "taunt bear" and not bear_moved: #taunt bear辱骂熊并且not bear_moved（False）同时为True是成立
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True #熊移动了
        elif choice == "taunt bear" and bear_moved: #同上，区别为bear_moved为True时，条件成立
            dead("The bear gets pissed off and chews your leg.") #熊生气了，咬你的腿
        elif choice == "open door" and bear_moved: #当open door且bear_moved = True时，成立
            gold_room() #调用自定义函数
        else:
            print("I got no idea what that means.")

def cthulhu_room(): #克苏鲁-美国小说家创造的克苏鲁神话中的存在
    print("Here you see the great evil Cthulhu.")
    print("He,it,whatever stares at you and you gou insane.") #无论什么盯着你看，你都会发疯。
    print("Do you flee for your life or eat your head?")#你是逃命还是吃你脑袋？
    
    choice = input("> ")
    
    if "flee" in choice: #输入值的值包括flee（逃命）时条件成立
        start() #自定义函数，又重新开始
    elif "head" in choice: 
        dead("Well that was tasty!")
    else:
        cthulhu_room() #进入该函数的起始位置，再一次运行该函数
        
        
def dead(why):
    print(why, "Good job!")
    exit(0)
    
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input("> ")
    
    if choice == "left":  #输入的choice变量为left时成立
        bear_room() #调用自定义函数bear_room()
    elif choice == "right": #输入的choice变量为right时成立
        cthulhu_room() #调用自定义函数cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")#你在房间里跌跌撞撞，直到饿死
    
    
start()