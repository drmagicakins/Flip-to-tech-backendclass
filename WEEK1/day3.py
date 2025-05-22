#dogs = ["mocky","snow","pauwy"]
"""
a = []
b = [1,2,3,4,5]
c = [10, "apple", True, 3.55]
d = [[1,2],[3,4], [5,6]]

e = ["apple", "banana", "mango"]
print(e[1])
for fruit in e:
    print(fruit)
"""    
#common operation you can perform in list
#Append
"""e.append("orange") #append() is a method
print(e)
e.insert(1, "tomato") #decide the position to insert while .append()/add will add towards the end
print(e)
e.remove("banana")
print(e)
e.pop() #remove from the end
print(e)
del e[1] #delete a value
print(e)
e[0] = "tomato" #change a value in a list
print(e)
print(len(e[1])) #count the characters
print(e)"""

#slicing to print a value while omitting some
"""
num = [0, 1, 2, 3, 4, 5]
print(num[1:4])
print(num[:3]) #print 1, 2 and 3 values
print(num[::2]) #print 0 2 and 4 skipped 1 and 2
print(num[::3]) #print 0 1nd 3 values 
print(num[::4]) #print 0 and 4 values
print(num[::-1]) #display value backwards
"""
## Create a UI for submitting assignment and admin page for viewing the assignment
## signup and login page
## student should be able to submit e.g. files, codes and URL

#Turple & Dictionary
#Turple is an unchangeable list - it can more than one data type
#Dictionary 

t1 = (1,2,3,4)
t2 = 1,2,3 #another turple
t3 = ("apple", 1, True) #mixed turple
t4 = (7,)
print(t1)

for i in t1:
    print(i)

#Dictionary is defined as key-values pair
student = {
    "name":"John",
    "age":23,
    "email":"drmagicakins@gmail.com",
    "sex":"male"
    }
student["name"] = "Bayo"
print(student)

d = dict(city="lagos")
print(d)
print(student["name"])

for a in student:
    print(a, student[a]) #print data in dictionary

del student["name"]
print(student)
    


