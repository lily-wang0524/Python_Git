# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:04:00 2023

@author: limin
"""

print("""
Welcome to the Game world!
There are two doors in front of you.
So, which door do you want to choose?""" )

door = input("input the door number: ")

if door == "1":
    print("You get two dollars.")
    print("Good job!")
    
elif door == "2":
    print("There are two boxes you can choose!")
    print("box#1: a red box.")
    print("box#2: a yellow box.")
   
    box = input("Please, Choose a box > ")
    
    if box == "1":
        print("You get one dollars.")
        print("Good!")
    elif box == "2":
        print("You get Ten dollars.")
        print("Excellent!")
    else:
        print("Game over!")
else:
    print("You don't get anything.")
        