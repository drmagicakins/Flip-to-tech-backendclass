##Learning Python - Variables, Data types, and Functions
#conditional statement is used to check the condition and run the code based on the condition
#if condition
# code to run if condition is true

"""x = int(input("enter your age: "))
if x == 18:
    print("you are 18")
else:
    print("you are not 18")"""

"""
score = int(input("enter your score: "))
if score >= 70:
    print("you have an A")
elif score >= 60:
    print("you have B")
elif score >= 50:
    print("you have c")
elif score >= 40:
    print("you have d")
else:
    print("you have failed woefully")
    """

# Loop -> Used to perform a task repeatedly, iterate things e.g: foreach
"""x = range(5)
print(x)

for i in x:
    print(i)

fruits = ["banana","mango","pawpaw","orange","grape"]
for fruit in fruits:
    print(fruit)

for i in range(0, 7):
    print(i)

#while loop -> infinte loop 
# incremental -> adds value to a value
x = 1
while x <= 5:
    print(x)
    x += 1
"""
"""y = 1
while y <= 100:
    print(y)
    y += 1
"""
#Password system using while loop

password = ""

while password != "secrete":
    password = input("Enter your password")
    
print("Login successful!")