#显式继承——子类中定义一个与父类同名的函数，以替换父类中的函数功能
class Parent(): #创建父类

    def override(self): #创建父类的函数
        print("Parent override()")

class Child(Parent): #创建子类Child继承至父类Parent

    def override(self): #创建与父类中函数同名的函数，但功能与其不同
        print("Child override()")

dad = Parent() #实例化父类
son = Child() #实例化子类

dad.override() #调用父类中的函数override()
son.override() #调用子类中的函数override()