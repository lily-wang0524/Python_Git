class Mystuff(object): #创建类

    def __init__(self): #函数__init__,初始化类
        self.tangerine = "And now a thousand years between"
    
    def apple(self): #创建函数apple
        print("I AM CLASSY APPLES!")

thing = Mystuff() #实例化类，对象thing,具有这个类的所有函数，变量等
thing.apple() #该对象可以调用类中包含的函数。
print(thing.tangerine) #该对象可以调用类中包含的变量。