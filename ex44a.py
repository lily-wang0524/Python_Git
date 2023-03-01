#隐式继承
class Parent(object): #创建父类

    def implicit(self): #创建函数
        print("PARENT implicit()")

class Child(Parent): #创建子类Child，继承至父类Parent
    pass

dad = Parent() #Parent()类实例化
son = Child() #Child()类实例化

dad.implicit() #调用父类内部函数
son.implicit() #调用函数继承至父类