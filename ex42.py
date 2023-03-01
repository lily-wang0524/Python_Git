## Animal is-a object(yes, sort of confusing) look at the extra credit(附加练习)
class Animal(object):
    pass

##Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ##Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    
    def __init__(self,name):
        ##Cat has-a name
        self.name = name

##Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name.
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

##Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ##?? hmm what is this strange magic?
        super(Employee,self).__init__(name) #python2的写法，超类，继承父类属性，不重复描述super().__init(name),Employee has-a name
        ##Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

##Salmon is-a Fish.
class Salmon(Fish):
    pass

## Halibut is-a Fish.
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan") 

##mary is-a Person
mary = Person("Mary")

##mary has-a pet called satan
mary.pet = satan

## frank is-a Employee, he has-a salary of 120000
frank = Employee("Frank", 120000)

#frank has-a pet, rover is-a pet
frank.pet = rover

##flipper is-a Fish
flipper = Fish()

##crouse is-a Salmon
crouse = Salmon()

##harry is-a Halibut
harry = Halibut()