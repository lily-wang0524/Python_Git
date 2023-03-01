# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 20:46:19 2022

@author: limin
"""

print("I am 6'2\" tall.") #\转义'，说明'是字符串一部分，而不是字符串最外面的单引号
print('I am 6\'2" tall.')

tabby_cat = "\tI'm tabbed in." #\t相当于Tab键，空两格
persian_cat = "I'm split\non a line."  #\n 换一行
backslash_cat = "I'm \\ a \\ cat." #\\转义\,可输出反斜杠

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""    #"""...""""多行字符串输出

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


#附加练习
question = 'What\'s your name? \n{}'
name = "Lily"
age = 25
answer_age = 'I\'m {} years old.'

print(question.format(name))
print(answer_age.format(age))