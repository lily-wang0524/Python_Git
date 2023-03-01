# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 10:36:43 2023

@author: limin
"""

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")  #输入选择

if door == "1": #如果变量door等于1
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1.Take the cake.")
    print("2.Scream at the bear.")
    
    bear = input("> ") #输入字符串
    
    if bear == "1": #如果door==1且bear==1时，条件成立
        print("The bear eats your face off. Good job!")
    elif bear == "2": #如果door==1且bear==2时，条件成立
        print("The bear eats your legs off. Good job!")
    else:  #如果door==1且bear不等于1且不等于2时，条件成立
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
        
elif door == "2":  #如果变量door等于2成立
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1.Blueberries.")
    print("2.Yellow jacket clothespins.")
    print("3.Understanding revolvers yelling melodies.")
    
    insanity = input("> ") #输入字符串
    
    if insanity == "1" or insanity == "2": #如果door等于2成立，且变量insanity等于1或者等于2成立
        print("You body survives powered by a mind of jello.")
        print("Good jobs!")
    else: #以上条件都不成立时
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
        
else: #door不等于1也不等于2时，成立
    print("You stumble around and fall on a knife and die. Good job!")