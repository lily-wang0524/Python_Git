# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 20:47:03 2023

@author: limin
"""

animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']
for i in range(6):
    print(f"The animal is at {i} and is a ", animals[i] ) #各动物的位置索引
    print(f"the sort of animal is {i+1} and is a ", animals[i]) #各动物的排序位置，即序数
    
    
vegatable = 'tomato'    
list1 = ['apple',23,"pear","egg",4,vegatable,9]
print(list1[-1])
print(list1[-2])
print(list1[0])
print(list1[5])