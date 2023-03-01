fruit = ['apple','orange','pear','watermelon'] #列表
string = "There are so many fruit." #字符串
tuple1 = ('cat','dog','pig') #元组
dict1 = {'Good':1,'night':2} #字典

print(','.join(fruit)) #列表按元素分隔，生成字符串
print('/'.join(string)) #字符串按字母分隔，生成新字符串
print('、'.join(tuple1)) #同列表
print(' '.join(dict1)) #按key分隔，生成新的字符串

#学生名单
student_list = [] #空列表
student_num = 10 #学生数量
for i in range(student_num):
    name = input("what your name? > ") #学生名字
    student_list.append(name) #加入到名单中

print(student_list) #打印学生名单
list_sort = student_list.sort() #按字母开头从小到大正向排序
print(student_list)
print(student_list[5])#学生名单中的第六个学生
