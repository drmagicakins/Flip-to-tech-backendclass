name = "Ceejay"
age = 25
state = "california"
gender = "boy"
_sex = True
NameofFood = ["Pizza", "Burger", "Sushi", "Rice and beans"]
x = 10
y = -5
z = 0
print(x, type(x))
print(y, type(y))
print(z, type(z))
#print(NameofFood, type(NameofFood))
# text type
"""hijack hfjfdhjfd jhsjhds jshjsd""" 
pi = 3.14
e = 2.78475
multiline = """ my name is ceejay """
char = 'A'
print(pi, type(pi))
print(e, type(e))
print(name, type(name))
print(multiline)
print(char)
is_true = True
is_false = False
print(is_true, type(is_true))
print(is_false, type(is_false))

#sequence types
#List

fruits = ["apple","banana","cherry", 1, 2, 3, True, False]
print(fruits, type(fruits))
#print out single list
print(fruits[1]) #Result -> banana
print(fruits[6], type(fruits[6]))
#fruit = ("apple","banana","cherry")

#Mappping types
#dictionary

person = {
    "name": "Ceejay",
    "age": 23,
    "state": "Lagos",
    "is_student": True
}

print(person["age"])
print(person["is_student"])

#assets
fruits = {"apple", "banana", "cherry", 1, 2, 3, True, False}
print(fruits)

#Operation in python
#In pyhton you'll be performing actual operation
a = 10
b = 20
#addition

print(a+b) #addition
print(a-b) #subtraction
print(a/b) #division
print(a*b) #multiplication
print(a % b) #modulus
print(a ** b) #exponential 10 raise to power 20

myname = "Paul"
greet = "Hello"
print(greet+" "+myname) #concatenate

#Comparison operator
a,b = 10,20 #the output is always boolean value
print(a == b) #equal to
print(a!=b) #not equal to
print(a>b) #greater than
print(a<b) #less than
print(a>=b) #greater or equal to
print(a<=b) #less than or equal to

#Overview of Function
#functions
#def functionName(parameter):
#   "function task"
#   return parameter

def add(a,b):
    return a+b
print(add(10,20))

#Assignment


