# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:45:27 2022

@author: limin
"""
#附加练习1
def f(a,b,c):
    return a * b + c

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("a * b + c =", f(a,b,c))

#附加练习4
#求 360/4-3*(2+5)
def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b
    
def subtract(a,b):
    print(f"SUBTRACTUNG {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLY {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

what = subtract(divide(360,4),multiply(3,add(2,5)))

print("360/4-3*(2+5) = ", what)

#常见问题2
def f(a,b,c):
    return a * b + c

a = float(input("a: ",end = " "))
b = float(input("b: ",end = " "))
c = float(input("c: ",end = " "))

print("a * b + c =", f(a,b,c))