#创建父类Human
class Human(object):
    def __init__(self, name, sex): #人类属性
        self.name = name
        self.sex = sex

#创建子类
class Student(Human):
    def __init__(self, name, sex, score): #学生包含属性，姓名，性别，分数
        self.name = name
        self.sex = sex
        self.score = score
        print("child")

student_1 = Student("Rose","female",89)
print(student_1.name)

#使用super()函数
#创建父类Human
class Human(object):
    def __init__(self, name, sex): #人类属性
        self.name = name
        self.sex = sex

#创建子类
class Student(Human):
    def __init__(self, name, sex, score): #学生包含属性，姓名，性别，分数
        super().__init__(name,sex) #使用super()函数直接调用
        self.score = score
        print("child")

student_1 = Student("Rose","female",89)
print(student_1.name)

#staticmethod()函数
class C(object):
    @staticmethod  #静态方法
    def f():
        print('Hello')

C.f() #静态方法无需实例化
cobj = C()
cobj.f() #也可实例化后调用


#多重继承，具体使用不会
class A(object):
    def __init__(self):
        print('A')
        super().__init__()
    
class B(object):
    def __init__(self):
        print('B')
        super().__init__()

class C(A,B):
    def __init__(self):
        super().__init__()
        print("C")

cobj = C()
print(cobj)