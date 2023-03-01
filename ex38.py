ten_things = "Apples Oranges Crows Telephone Light Sugar" #字符串

print("Wait there are not 10 things in that list. Let's fix it.") #打印字符串

stuff = ten_things.split(' ') #按空格拆分字符串，输出为列表（spilt的用法）
more_stuff = ["Day", "Night","Song","Frisbee","Corn","Banana","Girl","Boy"] #字符串列表

#while循环，循环条件stuff列表长度不等于10
# while len(stuff) != 10:
#     next_one = more_stuff.pop() #more_stuff列表的最后一个
#     print("Adding: ",next_one) 
#     stuff.append(next_one) #在stuff列表从后加入next_one变量的字符串
#     print(f"There are {len(stuff)} items now.") #格式化字符串。

#for循环
for i in more_stuff:
    if len(stuff) <= 10:
        next_one = more_stuff.pop() 
        print("Adding: ",next_one) 
        stuff.append(next_one) 
        print(f"There are {len(stuff)} items now.") #格式化字符串。
    else:
        break

print("There we go: ", stuff) #打印

print("Let's do some thing with stuff.")

print(stuff[1]) #打印列表stuff的第2个（基数1，序数2）
print(stuff[-1]) #打印列表stuff的最后一个
print(stuff.pop()) #打印列表stuff的最后一个，pop()的默认移初列表的最后一个。
print(' '.join(stuff)) #join()连接字符串，返回新的字符串，用空格作为分隔符连接列表stuff
print('#'.join(stuff[3:5])) #用#作为分隔符，连接列表stuff的第4个和第5个元素，其中[:]取前不取后。
