# Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

data={1:"Rutuja", 2:"Devyani", 3:"Jyoti"}
print(data)

print(data[1])
print(data[2])
print(data[3])

keys=['Yash','Devyani','Jyoti','Rutuja']
values=['Javascript','Python','React','Java']

data=dict(zip(keys,values))
print(data)

# print(data('Monika'))

data['Monika']='C sharp'
print(data)

prog={'Javascript':'Atom', 'Python':['Pycharm','Sublime'], 'Java':{'JSE','Eclipse','Netbeans','JEE'}}
print(prog)

print(prog['Javascript'])
print(prog['Java'])