# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:03:38 2022

@author: limin
"""

cars = 100  #cars变量
space_in_a_car = 4 #每辆车有4个座位
drivers = 30 #drivers司机变量
passengers = 90 #乘客变量
cars_not_driven = cars - drivers #不能开的车变量=车的数量-司机的数量
cars_driven = drivers #能够开的车=司机数量
carpool_capacity = cars_driven * space_in_a_car #车的承载量= 可以开的车数量*每个车的座位
average_passengers_per_car = passengers / cars_driven #平均每辆车的乘客= 乘客的数量/可以开的车


print("There are", cars,"cars available.")
print("There are only",drivers, "drivers available.")
print("There will be", cars_not_driven,"empty cars today.")
print("We can transport",carpool_capacity,"people today.")
print("We have",passengers,"to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
