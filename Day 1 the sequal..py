# Section 1 Print.
# Print well "prints" stuff onto the IDE terminal like Integers Strings and Boolean.
print("The Gods had condemned Sisyphus to ceaselessly rolling a rock to the top of a mountain, whence the stone "
      "would fall back of its own weight. They had thought with some reason that there is no more dreadful punishment "
      "than futile and hopeless labor.")
print("Hello Python")
print(True)
# Section 2 Variables.
# Variables Store data like Strings Integers And Boolean.
First_Name = "Elliot"
Last_Name = " Alderson"
Full_Name = First_Name + Last_Name
print(Full_Name)
# print("Random String" + Random variable) this allows you to print A string alongside a variable
print("Hello, " + Full_Name)
# Print(type()) allows you to print the type of data inside the variable.
print(type(Full_Name))
age = 21
age = age + 1
# Or you could do age += 1.
print(age)
print(type(age))
# This converts a variable in which case is a number into a string same thing can be done vice-versa and with booleans
print("Your age is: " + str(age))
height = 160.75
print(height)
print(type(height))
print("your height is " + str(height) + " centimeters")
human = True
print(human)
print(type(human))
print("Are you no longer human? " + str(human))
# Section 3 multiple assignment
# This is very useful allows you to assign multiple variables in the same line of code!
Name, Age, Based = "Elliot", 24, True
print(Name)
print(Age)
print(Based)
# this allows you to assign multiple variables that have the same value in one line of code
Jassim = Mohammed = Ali = Eyad = 15
print(Jassim)
print(Mohammed)
print(Ali)
print(Eyad)
# Section 4 String Manipulation
# Counts how many letters in a variable.
print(len(Name))
# finds if there is a certain letter  in a variable or data and states its position.
print(Name.find("l"))
# Capitalizes the first letter of the string.
print(Name.capitalize())
# Makes the string uppercase.
print(Name.upper())
# Makes the string lowercase.
print(Name.lower())
# True or false whether the data type is in lowercase.
print(Name.islower())
# True or false whether the data type has digits in it.
print(Name.isdigit())
# True or False whether the data type has alphabets in it.
print(Name.isalpha())
# counts how much of a certain value are in a variable or data type.
print(Name.count("l"))
print(Name.replace("E", "A"))
print(Name.replace("l", "p"))
print(Name * 3)
# Section 5 Type casting
# This converts a variable in which case is a number into a string same thing can be done vice-versa and with booleans
x = 1  # Integer(Number)
y = 2.3  # Float (Decimal Number)
z = "9"  # String (Words)
y = str(y)
z = str(z)
x = str(x)
print("X is " + x)
print("X is " + y)
print(z * 3)
# Section 6 User Input
name = input("What is your name? ")
Age_Input = float(input("What is your age? "))
Height = float(input("How tall are you? "))
print("Hello, " + name + "!" " You are " + str(Age_Input) + "!" " And " + str(Height) + " centimeters tall!")
# Section 7
