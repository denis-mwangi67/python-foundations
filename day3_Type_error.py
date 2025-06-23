# Data Types In Python


# Everything in python is consider as an object
# Data types are classes ei int, float, string, boolean
# variable are instance or object of the class ie var_1
var_1 = 3

print(type(var_1))
# <class 'int'>
#String
name = "root"
print(type(name))
print(name[0:3])

name_1 = "Computer Science"

print(name + name_1)
#Boolean
var = True 
var_4 = False

print(type(var))
print(type(var_4))

# Type conversion or casting
#is to change the variable to other variable format
print(len("Computer Science"))
# len() is for find out the string length

length = len("Computer Sci")
print(type(length))
print(type(str(length)))
print("this are number of letter " + str(length))

print("10"+"10")
print(int("10")+int("10"))

#Take input from a user and add them

#Num_1 = int(input("Enter Num 1: "))
#Num_2 = int(input("Enter num 2: "))

#print(Num_1 + Num_2)


#program to add digit of a number

number = input("Enter Number: ")
first_num = number[0]
second_num = number[1]


print(int(first_num) + int(second_num))


