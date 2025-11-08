class A:
    def feature1(self):
        print("Feature 1")
       
    def feature2(self):
         print("Feature 2")

class B:
    def feature3(self):
        print("feature 3")

    def feature4(self):
        print("Feature 4")  

class C(A,B):
    def feature5(self):
        print("Feature 5")        

# a1=A()
# a1.feature1()     
# 
# b1=B()  
# b1.feature1()   
# b1.feature2()
# b1.feature3()
# b1.feature4

c1=C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()


#Inheritance with constructor

class parent:
    def __init__(self):
        print("Parent constructor")

class child(parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

c=child()        


