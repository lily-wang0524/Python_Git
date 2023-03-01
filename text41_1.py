import random

for i in range(4):
    num = random.randint(3,7) #随机生成整数
    print(num)

a =[]
for n in range(2,8):
    a.append(n+1)
print(a)
print(random.sample(a,4)) #截取序列a的4个随机数，序列a不变

str = ['you','are','a','beautiful','girl']
random.shuffle(str) #随机打乱列表顺序
print(str)

#sys模块
#from sys import argv
# Script, name = argv #定义函数argv列表参数，则外部输入时，参数数量是固定的
# print(Script,name)
import sys

print(f"the first argv is ", sys.argv[0])
print(f"other argv is/are ",sys.argv[1:])

words = ['drug', 'drum', 'duck', 'dust']
words_c1 = [word.capitalize() for word in random.sample(words, len(words))] 
print(words_c1)

#上面的编写方法是下面编写方法的变种
words_c2 = []
for w in random.sample(words,len(words)): #截取words列表的长度的随机数列表
    words_c2.append(w.capitalize())
print(words_c2)

#count()函数
PHRASES = {
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self,***)":
    "class %%% has-a __init__ that takes self and ***params.",
    "class %%%(object):\n\tdef ***(self,@@@)":
    "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
    "Set *** to a instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, call it with params self @@@.",
   " ***.*** = '***'":
   "From *** get the *** attribute and set it to '***'."
   } #创建字典

snippets = list(PHRASES.keys()) #转化为列表
print(snippets) #打印列表
num_list = [] #空列表，存储snippets列表中每个字符串元素snippet的'%%%'数量
for snippet in snippets:
    num_count = snippet.count('%%%')
    num_list.append(num_count)
print(num_list)

a= "qbcd"
b = "What's you name?"

for sentence in a,b :  #
    result = sentence[:]
    print(result)

#replace()函数用法
ws = ["123","word","apple","pc"] #列表
result ="class %%%(%%%):"#字符串
#for循环的简写，并随机获取ws列表中同%%%数量相同的词汇
names = [w for w in random.sample(ws,result.count('%%%'))] 
#使用for循环替换result中的%%%字符串
for n in names:
    result = result.replace("%%%", n, 1) 
print(result)

a, b  = ['ss', 'rr']
print(a)


