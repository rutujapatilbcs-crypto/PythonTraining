#While loop 

a=1

while a<=5:
    print("Rutuja", a)
    a=a+1

x=5

while x>=1:
    print("Patil", x)
    x=x-1

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1  

  i=1
  while i < 6:
     i += 1
     print(i)
     if(i == 4):
        continue
     print(i)


# For loop 

a=[22,"abc", 20.2]

for i in a:
   print(i)

b="Rutuja"
for x in b:
   print(x)

for i in range(10):
   print(i)

for i in range(11, 20, 3): 
   print(i)


#Iterate tuple using for loop

my_tuple=(10,20,30,40,50)
for i in my_tuple:
   print(i)

fruits=("Apple","Banana","Mango","Strawberry","Cherry")
for i in range(len(fruits)):
   print(i,fruits[i])

colours=("Red","White","Black","Yellow","Blue")
for i in range(len(colours)):
   print("index :", i, "Value :", colours[i])   

# Iterate tuple using while loop

name=("Rutuja","Devyani","Jyoti","yash")
i=0
while i<len(name):
   print(name[i])
   i+=1  

  