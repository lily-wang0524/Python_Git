#三者结合
class Parent(): #创建父类
    
    def override(self): #创建父类函数override
        print("Parent override()") #函数的行为，打印字符串

    def implicit(self): #创建父类函数implicit()
        print("Parent implicit()") #函数的行为，打印字符串

    def altered(self): #创建父类函数altered()
        print("Parent altered()") #函数的行为，打印字符串

class Child(Parent): #创建子类
    def override(self): #创建与父类中override同名的函数，覆盖父类中该函数的内容
        print("Child override()")

    def altered(self): #创建与父类中altered同名函数，覆盖父类该函数内容
        print("Child, Before Parent altered()")
        super().altered() #调用函数super(超类)，再次继承父类中的函数altered()
        print("Child, After Parent altered()")

dad = Parent() #父类实例化
son = Child() #子类实例化

dad.implicit() #调用父类函数implicit()
son.implicit() #子类中未定义函数implicit(),但隐式继承了父类，也可调用该函数，且内容相同

dad.override() #调用父类override()函数
son.override() #调用子类override()函数

dad.altered() #调用父类altered()函数
son.altered() #调用子类altered()函数
