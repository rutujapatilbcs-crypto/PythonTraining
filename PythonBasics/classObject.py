class Dog:
    sound = "bark"

dog1 = Dog() # Creating object from class
print(dog1.sound) # Accessing the class


#Using __init__()

class Dog:
    species="Canine" #class variable
    def __init__(self, name, age):
        self.name=name
        self.age=age

dog2=Dog('Buddy', 3)
print(dog2.name)
print(dog2.age)
print(dog2.species)



class computer:
    def __init__(self):
        self.name='Rutuja'
        self.age=25

    def update(self):
        self.age=26  
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            False   

c1=computer()
c2=computer()

if c1.compare(c2):
    print("They are same")
c1.update()

