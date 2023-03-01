# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 19:47:42 2023

@author: limin
"""

elements = range(0,6)

for i in elements:
    print(f"elements was: {i}")


a = [1,2,3,5]
b = [6,8,9,0]
a.extend(b)

print("a + b = ",a)

c = [1,2,4,5]
c.append(6)
print(c)
c.append("num")
print(c)