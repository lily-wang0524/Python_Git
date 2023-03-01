# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 20:36:41 2023

@author: limin
"""

print("Let's practice everything.") #打印
print('You\'d need to know \'bout escapes with \\ that do:') #转义字符\,\'为',\\为\
print('\n newlines and \t tab.') #转义字符\n，换行；\t,空格等于tab键

#字符串打印，格式不变，其中转义字符\t,\n用法同上
poem = """
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("---------------------")
print(poem)
print("---------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}") #使用f""将变量格式化字符串

#创建函数，started为参数
def secret_formula(started):
    jelly_beans = started * 500 #乘法
    jars = jelly_beans / 1000 #除法
    crates = jars / 100
    return jelly_beans, jars, crates #return使用，结果返回这三个变量


start_point = 10000
beans, jars, crates = secret_formula(start_point) #调用函数，输出结果按顺序对应的变量

# remember that this is another way to format a string
 #｛｝，字符串.format(变量)的方式将变量格式化为字符串
print("With a starting point of : {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point) #调用函数，结果输出为formula变量
print(formula) #输出为元组，tuple
#this is an easy way to apply a list to a format string
# format函数，格式化列表和元组时，使用*对列表和元组拆分，使用**对字典拆分。
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))