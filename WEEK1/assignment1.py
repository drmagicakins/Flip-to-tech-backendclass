#Theoretical Questions
#What data type is the variable x = 10 in Python?
#Answer: int (integer)

#Explain the difference between a list and a tuple in Python.
#Answer: A list is mutable (can be changed), while a tuple is immutable (cannot be changed).

#What is the output of print(type("hello"))?
#Answer: <class 'str'>

#Why would you use a dictionary data structure instead of a list?
#Answer: A dictionary stores key-value pairs for fast lookups, while a list stores items by index.

#What is the difference between == and = operators in Python?
#Answer: == checks for equality; = is the assignment operator.

#How are single quotes (') and double quotes (") different when defining strings in Python?
#Answer: They are functionally the same; you can use either to define strings.

#What type of object is returned by the expression a < b in Python?
#Answer: bool (boolean)

#Explain the purpose of triple quotes ("""...""") in Python.
#Answer: Used for multi-line strings or docstrings.

#What happens when you add a string and an integer in Python?
#Answer: It raises a TypeError.

#What is the purpose of the return statement in a function?
#Answer: It ends the function and sends a result back to the caller.

#What data type would print(type(3.14)) return?
#Answer: <class 'float'>

#What is type casting in Python?
#Answer: Converting one data type to another (e.g., string to integer).

#What's the difference between mutable and immutable data types in Python?
#Answer: Mutable types (like lists) can be changed; immutable types (like strings, tuples) cannot.

#What does the % operator do with numbers in Python?
#Answer: It returns the remainder of a division (modulus).

#How are sets different from lists in Python?
#Answer: Sets are unordered and do not allow duplicates; lists are ordered and allow duplicates

#Practical Tasks
#1. Convert string "25" to integer and add to 10:
result = int("25") + 10
print(result)

#2. Create dictionary and print "age":
person = {"name": "John", "age": 30, "city": "Lagos"}
print(person["age"])

#3. Function to return product:
def multiply(a, b):
    return a * b

#4. List of first 5 even numbers and print length:
evens = [2, 4, 6, 8, 10]
print(len(evens))

#5. Concatenate "Hello" and "World":
greeting = "Hello" + " " + "World"
print(greeting)

#6. Function to check even or odd:
def check_number(n):
    return "Even" if n % 2 == 0 else "Odd"

#7. Tuple and trying to add a fourth country:
countries = ("Nigeria", "Ghana", "Kenya")
#countries.append("South Africa")  # This will raise an AttributeError
print("Tuples are immutable; you cannot add to them.")

#8. Check if "apple" exists in list:
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)

#9. Boolean check for is_student:
is_student = True
if is_student:
    print("Student")
else:
    print("Not a student")

#10. Function to return string length:
def string_length(s):
    return len(s)

#11. Set with duplicates:
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)  # Output: {1, 2, 3}

#12. 3 raised to power 4:
result = 3 ** 4
print(result)

#13. Multiline string:
message = """This is line one.
This is line two.
This is line three."""
print(message)

#14. Extract first and last characters from "Python":
word = "Python"
print(word[0], word[-1])

#15. List with mixed types and print type of each:
mixed_list = ["hello", 42, True]
for item in mixed_list:
    print(type(item))
