# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:12:04 2023

@author: limin
"""
from sys import argv
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input() #缺少变量height
print("How much do you weigh?", end=' ')  #缺少右边括号
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv #未调用argv模块

txt = open(filename) #filename缺少a

print(f"Here's your file {filename}:") #缺少转换字符串格式的f
print(txt.read()) #少写t

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read()) #多出了（）两个括号,read()函数用点连接

print("Let's practice everything.")  #多个单引号，修改为双引号
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') #print()不能换行

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------") #缺少右边的双引号
print(poem)
print("--------------") #缺少左边的双引号


five = 10 - 2 + 3 - 6 #减号后面少数字6
print(f"This should be five: {five}") #缺少右边的括号

def secret_formula(started):  #缺少冒号
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100  #缺少运算符号
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point) #缺少变量crates

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) #参数名缺少下划线_
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30 #cates变量与后面的cats变量不符
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!") #缺少两边括号

if people > cats:
    print("Not many cats! The world is saved!") #对比符号错误，不应该与上面的符号相同

if people < dogs:
    print("The world is drooled on!")

if people > dogs:  #缺少冒号
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs: #缺少冒号
    print("People are less than or equal to dogs.") #缺少右边的双引号


if people == dogs: #等于对比，用==。
    print("People are dogs.")
