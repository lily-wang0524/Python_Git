# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 21:06:20 2022

@author: limin
"""

from sys import argv

script,user_name,first = argv #设定argv对应参数
prompt = '>' #字符串

print(f"Hi {user_name},I'm the {script} script.")
print(f"You are my {first} friend.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt) #用户输入

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
      Alright, so you said {likes} about liking me.
      You live in {lives}. Not sure Where that is.
      And you have a {computer} computer.Nice.
      """)  #不换行字符串