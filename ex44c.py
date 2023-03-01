#子类上的操作会更改父类上的操作
#修改类中函数前后
class Parent(): #创建父类

    def altered(self): #创建父类函数
        print("Parent altered()")

class Child(Parent): #创建子类

    def altered(self): #创建与父类函数同名的子类函数，覆盖父类函数
        print("Child, Before Parent altered()") #打印
        super().altered() #利用super(超类)调用父类中的函数
        print("Child, After Parent altered()") #继续打印

dad = Parent() #实例化父类
son = Child() #实例化子类

dad.altered() #调用父类函数
son.altered() #调用子类函数