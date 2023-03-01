# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 16:29:46 2022

@author: limin
"""

from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv
name = input("What's your name?")
age = input("How old are you?")

print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)
print(f"My name is {name}. I'm {age} years old.")

