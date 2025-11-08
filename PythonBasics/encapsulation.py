class student:
    def __init__(self):
        self.__marks=90

    def show(self):
        print("Marks :", self.__marks)    

s=student()

s.show()

###################################
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_name(self):
     return self.__name
  
  def set_name(self, name):
    self.__name=name 

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Rutuja", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())

p1.set_name("Patil")
print(p1.get_name())