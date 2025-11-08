def greet():
    print("Hello")
    print("Good morning")

greet()    

def add(a,b):
    c=a+b
    print(c)

add(10,20)  

def add_sub(a, b):
    c = a + b
    d = a - b
    return c, d
result1,result2=add_sub(5,6)
print(result1)
print(result2)


def person(age, name):
    print(age)
    print(name)

person(26,"Rutuja")

def count(list):
    even=0
    odd=0

    for i in list:
        if i % 2==0:
            even+=1
        else:
            odd+=1
        return even, odd
list=[20,39,87,21,34,54,50]

even,odd = count(list)        
print("Even : {} and Odd : {}".format(even,odd))