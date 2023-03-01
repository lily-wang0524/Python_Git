from textwrap import dedent

#不使用dedent函数
text = """
    How are you?
    I'm fine, thank you."""
print(text)

#不符合python的缩进原则
text = """
How are you?
I'm fine, thank you."""
print(text)

#使用dedent函数,删除三引号中的前导空格
text = """
    How are you?
    I'm fine, thank you."""
print(dedent(text))

a = 2
print(dedent(f"""
there  are {a} apples. 
"""))

#类内部调用
class Animal():
    def __init__(self, name,age): #类初始化属性
        self.name = name
        self.age = age
    
    def feed(self,num,food): #feed()函数，参数为num和food
        num += 1
        print(f"It needs {num}g {food}.")

    def water(self, n, food): #water()函数，参数为n和food，因为要调用内部函数，该函数的参数需要与调用函数一致
        #内部调用函数feed()，使用self.函数名(参数)调用，注意参数数量与之前一致
        water_num = self.feed(n,food) 
        return water_num

AM = Animal("Lily",2) #实例化类时，需要定义类的属性，若无，则不需要
AM.water(2,'apple') #类的函数外部调用，将类实例化后使用.调用
Animal.water(1,"meat") #会报错

