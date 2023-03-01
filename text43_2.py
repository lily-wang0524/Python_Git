#类相互之间调用函数
class Car():
    def __init__(self,make,model): #初始化函数，属性make和model
        self.make = make
        self.model =model

    def engine(self,num): #定义Car()函数
        print(f"The car has {num} engine.")

class Dealership():
    def __init__(self,name): #初始化函数，属性为name，调用实例需要填写name属性
        self.name = name
        self.cars = [] #定义新变量，列表

    def add_car(self, make, model): #定义函数，其参数数量由于调用Car()类属性而与其对应参数相同
        new_car = Car(make,model) #调用Car()类属性，即初始化函数
        self.cars.append(new_car)
    
    def show_inventory(self,make,model,num): #定义函数，参数数量由调用Car()类的engine()函数确定，因此参数为3个
        for car in self.cars:
            print(car.make,car.model)
        Car(make,model).engine(num) #调用Car()类中的函数engine()，调用函数依旧需要实例化类

dealership = Dealership("ABC Motors")
dealership.add_car("Toyota","Camry")
dealership.add_car("Honda","Civic")
dealership.show_inventory("ABC","BIG",3)