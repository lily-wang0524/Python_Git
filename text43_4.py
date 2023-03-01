from text43_3 import ClassA  #调用模块

class ClassB():  #定义类
    def __init__(self):  #定义属性
        self.name = 'ClassB'  

    def greet(self): #定义函数
        return 'Hello from ' + self.name #返回值

    def call_class_a(self): #定义函数，返回class_a类
        a = ClassA() #调用class_a实例
        return a.greet() #返回值

