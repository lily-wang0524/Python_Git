# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:38:13 2023

@author: limin
"""

import ex25  #调用自定义模块ex25
sentence = "All good things comes to those who wait." #原始字符串
words = ex25.break_words(sentence)  #将字符串变量以空格为分隔符切片成字符串列表
print(words) #打印字符串列表
sorted_words = ex25.sort_words(words)  #字符串列表按字母排序
print(sorted_words) #打印排序后的字符串列表
ex25.print_first_word(words) #打印字符串列表的第一个字符串
ex25.print_last_word(words) #打印字符串列表的最后一个字符串
print(words)  #打印字符串列表
ex25.print_first_word(sorted_words) #打印排序后的字符串列表的第一个字符串
ex25.print_last_word(sorted_words) #打印排序后的字符串列表的最后一个字符串
print(sorted_words) #打印排序后的字符串列表
sorted_words = ex25.sort_sentence(sentence) #切片且排序后的字符串列表
print(sorted_words) #打印切片且排序后的字符串
ex25.print_first_and_last(sentence) #打印字符串的第一个和最后一个字符串
ex25.print_first_and_last_sorted(sentence) #打印切片且排序后的字符串的第一个和最后一个字符串