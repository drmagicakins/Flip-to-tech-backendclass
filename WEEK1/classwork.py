import os

#Write a function to display even number from 1 - 50


"""def diseven():
    even = range(1, 51) #store range of numbers
    for i in even: #loop through the numbers
        if i % 2 == 0: # display even numbers that are divisible by 2 without remainder
            print(i)

diseven()"""

"""file = open("file.txt", "r")

print(file.read()) #read() method converts it to a string 

file = open("file.txt","a+")
file.write("I love to read good books.") #clears and replace with this in file.txt
print(file.read())"""

# Professional method of creating and writing in a file
"""with open('file2.txt', 'w') as file: # "with" works together with "as"
    file.write("Hello world \n ")
    file.write("I love Python \n")
    file.write("On my journey to creating a dynamic web app")

with open("file2.txt","r") as file:
    content = file.read()
    print(content)
    print(len(content))

with open("file2.txt","a+") as file:
    file.write("\n I dislike errors but love debugging... ('V')")
    

with open("file2.txt","r") as file:
    content = file.read()
    print(content)

if os.path.exists("file2.txt"):
    os.remove("file2.txt")
    print("file has been deleted")
else:
    print("file does not exist")"""

FILENAME = "data.txt"

userdata = input("Enter some data")

with open(FILENAME, "a") as file:
    file.write(userdata + "\n") 

print("Your data has been submitted")

print("Reading from the file")


with open(FILENAME,"r") as file:
    print(file.read())


#file1 hello
#file2 print hello from file 2

