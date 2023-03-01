#l老式字符串格式化
n = 45.25
m = 1000
a = "world"
print("%d"%n) #十进制整数（不含浮点数）
print("%i"%n) #	同 %d
print("%o"%m) #	转化为八进制数
print("%u"%n) #无符号十进制整数,无符号的没有负数
print("%x"%m)#十六进制数小写
print("%X"%m)#十六进制数大写
print("%e"%m)#指数计数法小写
print("%E"%m)#指数计数法大写
print("%f"%n)#浮点数
print("%F"%n)#同%f
print("%g"%n)#浮点数同%f，更短的浮点数
print("%G"%n)#同%g,但是大写
print("%c"%m)#符号格式化，转化为ASCII码
print("%r"%n)#rper()方法处理对象
print("hello %r !"%a) #对比%s，%r打印时能够重现它所代表的对象，有时候输出一致。
print("hello %s !"%a)#	字符串格式化, str()适于人阅读的形式
print("%s"%n) #输出同("%r"%n)
print("%d%%"%n)#百分号，但是需要转化变量的类型

#运算符
x = 3
y = 5
print(x + y) #加
print(x - y) #减
print(x * y) #乘
print(x ** y) #乘方
print(x / y) #除
print(x // y) #地板除（商向下取整）
print(x % y) #字符串插入符；取模；取余数
print(x < y) #小于
print(x > y) #大于
print(x <= y) #小于等于
print(x >= y) #大于等于
print(x == y) #等于
print(x != y) #不等于
print(len("hi")) #()括号
print([1,3,4]) #[]列表中括号
print({'x':5,'y': 10}) #｛｝字典大括号
