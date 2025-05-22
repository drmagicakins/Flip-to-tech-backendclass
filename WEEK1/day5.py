import random, datetime #built-in function
import math_tool #external function
import pyjokes
#Exception handling files and import

print(math_tool.Square(6))


#Inbuilt module requires installation
#External module doesn't require installation

#Types of external modules
#Math, Random, Datetime, OS, JSON, request, pandals, flask, beautiful soap - scrapping website,  

#Example of Built-in module
number = random.randint(1, 10) #get random number
print("print random number", number)


now = datetime.datetime.now()
print('Today is:', now.time())

#Open source - pypi.org

jokes = pyjokes.get_joke()
print('This is your joke:', jokes)

try:
    val = int(input("Enter a number"))
except ValueError:
    print("Oops! You have an error")
else:
    print('your number is:', val)


try:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    ans = num1 / num2
    print(ans)
except ValueError:
    print("enter only numbers")
except ZeroDivisionError:
    print("you can't divide by zero")
else:
    print(f"the result is {ans}")
finally:
    print("this is the end of your code")






