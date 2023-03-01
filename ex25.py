# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 10:03:33 2023

@author: limin
"""
def break_words(stuff):  #定义函数break_words,作用--返回以空格为分隔符切片后的文字列表
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words): #定义sort_words函数，作用---返回按一定顺序显示的文字列表，并不会实际上改变列表的顺序
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): #打印列表中的第一个字符串
    """prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
    
def print_last_word(words):#打印列表中的最后一个字符串
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
    
def sort_sentence(sentence):  #返回切片后，且完成排序的字符串列表
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    
def print_first_and_last(sentence): #返回切片后的字符串列表的第一个和最后一个字符串
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence): #返回切片完，且排序完后的字符串列表的第一个和最后一个字符串，即一二三四函数的结合
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    