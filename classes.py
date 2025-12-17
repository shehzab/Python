# A class is a blueprint for creating objects that have attributes and methods

# creating a SImple class
class Person:
  def him(talk):
    print("Hey am a person")



# Instance/object
jordan = Person()
#jordan.him()



# 2. __init__ is a constructor which allow us to create variables in class

class Man:
  def __init__(self):
    self.name = "Michael"
    self.age = 35
    self.location = "UK"

  def talk(self):
    print(f"Name: {self.name}, Age: {self.age},Location: {self.location}")

m = Man()
#m.talk()


class President:
  def __init__(self, name, age, location):
    self.name = name
    self.age = age
    self.location = location
  
  def blab(self):
    print(f"Name: {self.name}, Age: {self.age},Location: {self.location}")

luttapi = President("Luttapi" , 12, "Kuttoosante veed")
#luttapi.blab()

muthu = President("Muthu", 39,"Police station" )
#muthu.blab()


# A static variable (or a class variable) is a variable that belongs to the class itself rather than instances of the class. this mean that the variable is shared among all instances of the class. Statuc variables are defined inside a class but outside of any methods, typcally at the beginning of that class definition.


class Car:
  #static variable

  num_cars = 0
  car_names = []
  def __init__(self, brand , model):
    self.brand = brand
    self.model = model

    # Accessing Static variable

    Car.num_cars += 1
    Car.car_names.append(f"{brand},{model}")    

car1 = Car("toyota", "Fortuner 2024")

car2 = Car("Suzuki", "Brezza")


print("Number of cars created", Car.num_cars)
print("Cars created ", Car.car_names)