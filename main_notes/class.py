#List
person = ["Jeff", "Smith", 55]

#Dictionary
person_new = {"first_name": "Jeff", "last_name": "Smith", "age": 55}
person_new["first_name"]

#Class Store 

class Person:
    pass

p = Person()
p.name = "Jeff"
p.age = 55

print(p.name)


#__init__ method

class Person:

    def __init__(self, name, age): #self is an instance
        print("Work!!!!")
        self.name = name
        self.age = age

p1 = Person("Jeff", 55)
p2 = Person("Sally", 34)
p3 = Person("Jim", 84)
p4 = Person("Frank", 100)


print(p1.name)
print(p2.name)
print(p3.name)
print(p4.name)


#Looping through

class Person:

    def __init__(self, name, age): #self is an instance
        print("Create Person!!")
        self.name = name
        self.age = age

p1 = Person("Jeff", 55)
p2 = Person("Sally", 34)
p3 = Person("Jim", 84)
p4 = Person("Frank", 100)

people = [p1, p2, p3, p4]

for p in people:
    print(p.name)

#Obj Pointers
class Person:

    def __init__(self, name):
        print("Hello")
        self.name = name

a = Person("Mars")
b = a
#Same obj, just known as a different variable 
print(a.name)
print(b.name)

del a 

#print(a) # name error
print(b)

del b

#print (b) #b does not exist 

