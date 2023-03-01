from other import Other #从模块Other中调用Other类

class Child(): #创建类Child()

    def __init__(self): #创建初始化函数
    #创建Other()类与Child()之间的桥梁,也可以没有，但是调用Other()类中的函数方式会有所不用
        self.other = Other() 

    def implicit(self): #创建函数implicit()
        self.other.implicit() #对应第一种，调用Other()类中的implicit()函数
        # Other().implicit() #对应第二种，调用Other()类中的implicit()函数

    def override(self): #创建函数override()
        print("Child override()")

    def altered(self): #创建altered()函数
        print("Child, Before Other altered()")
        self.other.altered() #第一种，调用Other()类中的altered()函数
        # Other().altered() #第二种，调用Other()类中的函数altered()
        print("Child, After Other altered()")

son = Child() #实例化Child类

son.implicit() #调用函数implicit()
son.override() #调用函数override()
son.altered() #调用函数altered()
    