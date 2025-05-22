#import statistics Library
import statistics 
#1. Student Grades with a List
print("Create a list of student scores and calculate the average.")
scores = [56,60,67,81,30,95]
print(scores)
average = statistics.mean(scores)
print(average)

#2. Favorite Fruits (List)
print("Create a list of your 5 favorite fruits. Add one, remove one, and print the list.")
fruits = ["mango","pawpaw","grape","orange","apple"]
print(fruits)
fruits.append("watermelon") #add a fruit to the list
print(fruits)
del fruits[0]
print(fruits)


#3. Tuple Unpacking
print("Store a coordinate `(x, y)` in a tuple and print both.")
coordinate = (3, 7) #define a tuple using bracket, reference a tuple with 0,1,2,... index
print("x coordinate:", coordinate[0])
print("x coordinate:", coordinate[1])

#4. Days of the Week (Tuple)
print("Create a tuple of all weekdays. Print the 1st and last day.")
weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
print(weekdays[0]) #print first tuple
print(weekdays[-1]) #print last tuple

#5. Dictionary of a Person
print("Create a dictionary for a person with name, age, and gender.")
dictionary = {"name":"Akinyemi Mathew","age":43,"gender":"male"}
print(dictionary)


#6. Add & Update Dictionary Data
print("Add a new key `job` and update the `age`.")
dictionary["job"] = "Data Scientist"
dictionary["age"] = 35
print(dictionary)

#7. Phonebook (Dictionary)
print("Create a dictionary with names and phone numbers. Let the user search by name.")
phonebook = {
    "John":"08022334455",
    "Blessing":"08033221189",
    "Peter":"09011229900",
    "Akeem":"09123324421",
    "Abraham":"08012212233"
    }
name = input("Enter a name to search")
if name in phonebook:
    print(f"{name}'s phone book is {phonebook[name]}")
else:
    print("Name not found in phonebook.")