# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data
# list is mutable

# List can store Numbers, Strings, Float, Boolean, List, Tuple, Dictionary, etc.


num = [10,12,22,32,42,52]

print(num)

print(num[0])

print(num[1:4])

print(num[-3])

names=["Rutuja", "Devyani", "Jyoti", "Yash"]

print(names)

print(names[3])

print(len(names))

mil=(num, names)
print(mil)

num.append(62)

print(num)

num.insert(2, 72)
print(num)

num.remove(62)
print(num)

num.pop(2)
print(num)

num.pop()
print(num)

del num[2:]
print(num)

del num[:2]
print(num)

num.append(22)
print(num)

num.append(36)
print(num)

num.append(56)
print(num)

num.append(78)
print(num)

num.insert(2, 98)
print(num)

num.extend([22,34,65,98])
print(num)

print(min(num))

print(max(num))

print(sum(num))

a=num.sort()
print(a)