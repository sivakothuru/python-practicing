# animal is a object
class Animal(object):
    
    def __init__(self):
        print "This is a Animal"

class Dog(Animal):

    def __init__(self, name):
        self.name = name
        print self.name

class Cat(Animal):

    def __init__(self, name):
        self.name = name

class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None
        print self.name
        print self.pet

class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary
        print "Employee name is:", self.name
        print "Employee salary is:", self.salary


class Fish(object):
    
    def __init__(self):
        print "This is a water animal"

class Salmon(Fish):
    
    def __init__(self):
        print "This is a kind fish, which is inherited from Fish"

class Halibut(Fish):
    
    def __init__(self):
        print "This is another fish, which is inherited from Fish family "

rover = Dog("Rover")

satan = Cat("satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()