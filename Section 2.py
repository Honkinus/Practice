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