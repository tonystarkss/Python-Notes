
character_name = "John"
character_age = 50
is_male = True
print("There once was a man named " + character_name + ", ")
print("he was" + character_age + "years old. ")
# Variable labeled name and age with a print statement and a boolean statement

character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")
# Variable labeled with a new name and new print statement

phrase = "Batman Rises"
print(phrase)
# Print the phrase

print(10 % 3)
# 10 divided by 3 and output the remainder

my_num = 7
print(str(my_num) + " is my number")
# Print a number with a string

my_num2 = -5
print(abs(my_num2))
# Prints the absolute value of my num2

my_num3 = -8
print(pow(3, 2))
# Power math operator

my_num4 = -6
print(max(4, 6))
# Prints the highest value

my_num5 = -10
print(min(3, 2))
# Prints the lowest value

my_num6 = -8
print(round(3.2))
# Rounds numbers

from math import *
# Import math function

my_num7 = -4
print(floor(3.7))
# Grabs the lowest number

my_num8 = -8
print(ceil(3.8))
# Grabs the highest number

my_num9 = 6
print(sqrt(36))
# Square root operator

name = input("Enter you name: ")
age = input("Enter you age: ")
print("Hey " + name + "! you are " + age)
# Input functions example

friends = ["Josh", "Shane", "Ben"]
print(friends)
# List example can be strings or booleans

friends = ["Josh", "Shane", "Ben"]
print(friends[0])
# Accessing elements of the list using the index

friends = ["Josh", "Shane", "Ben"]
print(friends[-2])
# Accessing elements but starting backwards index

friends = ["Josh", "Shane", "Ben"]
print(friends[1:])
# Grabs the index of one and anything after that

friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
print(friends[1:3])
# Grabs elements up to 3 but not including 3 and is a range index

friends = ["Josh", "Shane", "Ben"]
friends[1] = "Mike"
print(friends[1])
# Updating a value in the list

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
friends.extend(lucky_numbers)
print(friends)
# Taking a list an appending it on another (adding it to it)

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
friends.append("Mike")
print(friends)
# Apppend function always adds to the back of the list

lucky_numbers2 = [4, 8, 15, 16, 23, 42]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
friends.insert(1, "Jack")
print(friends)
# Position one now is jack, pushes list down

lucky_numbers3 = [4, 8, 15, 16, 23, 42]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
friends.remove("Noah")
print(friends)
# Removes elements from the list

lucky_numbers4 = [4, 8, 15, 16, 23, 42]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
friends.clear()
print(friends)
# Empties the list

lucky_numbers5 = [4, 8, 15, 16, 23, 42]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
friends.pop()
print(friends)
# Takes an item off of the list

lucky_numbers6 = [4, 8, 15, 16, 23, 42]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
print(friends.index("Chris"))
# Finds and prints the index of where the element is in the list

lucky_numbers7 = [4, 8, 15, 16, 23, 42]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah", "Josh", "Josh"]
print(friends.count("Josh"))
# Counts how many times an element appears in the list

lucky_numbers8 = [4, 8, 15, 16, 23, 42]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
friends.sort()
print(friends)
# Sorts the list in alphabetic order

lucky_numbers9 = [4, 8, 15, 43, 23, 20, 16]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
lucky_numbers9.sort()
print(lucky_numbers9)
# Sorts the integers in order lowest to highest

lucky_numbers9 = [4, 8, 15, 43, 23, 20, 16]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
lucky_numbers9.reverse()
print(lucky_numbers9)
# Reverses the order of the numbers

lucky_numbers9 = [4, 8, 15, 43, 23, 20, 16]
friends = ["Josh", "Shane", "Ben", "Chris", "Noah"]
friends2 = friends.copy()
print(friends2)
# Copy lists

coordinates = (4, 8)
# Tuple with a value the tuple can't be changed or modified

coordinates = (4, 8)
print(coordinates[0])
# Index the tuple

coordinates = [(4, 8), (6, 7), (15, 3)]
print(coordinates)
# Multiple tuples

def say_hi():
    print("Hi user!")

say_hi()
# Function and calling the function, always have to call a function

def say_hello(name):
    print("Hello " + name)

say_hello("Josh")
# Function and calling it with a parameter

def say_hello(name, age):
    print("Hello " + name + ", you are " + age)

say_hello("Josh", "20")
# Function with multiple parameters

def say_hello(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hello("Josh", 20)
# Function with multiple parameters including a string

def cube(num):
    return num*num*num

result = cube(3)
print(result)
# Return function example returns a value back to the call

is_male = True

if is_male:
    print("You're a male")
else:
    print("You're not a male")
# If statement example

is_male = True
is_tall = True

if is_male or is_tall:
    print("You're a male or tall or both")
else:
    print("You're not a male or tall")
# If statement with a or operator

is_male = True
is_tall = True

if is_male and is_tall:
    print("You're a male and tall")
else:
    print("You're not a male or tall or both")
# If statement with a and operator

is_male = True
is_tall = True

if is_male or is_tall:
    print("You're a male and tall")
elif is_male and not(is_tall):
    print("You're a short male")
elif not(is_male) and is_tall:
    print("You're' not a male but you're tall")
else:
    print("You're not a male or tall")
# If statement with a else if operator

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(30, 44, 500))
# Comparison operator == - checks if equal, != - Not equal, > - greater than, < - less than, >= - greater than & =, <=

i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")
# While loop example, code will loop through as long as the condition is true

for letter in "Batman Rises":
    print(letter)
# For loop example, prints each letter individually

friends = ["Shane", "Ben", "Noah"]
for friend in friends:
    print(friend)
# For loop that prints all the objects in the array

for index in range(3, 10):
    print(index)
# For loop range

friends = ["Shane", "Ben", "Noah"]
for index in range(len(friends)):
    print(friends[index])
# For loop indexing the array

for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")
# If else inside a for loop

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(3, 4))
# Taking a base number and making it a power number

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][1])
# 2D list/array example

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)
# Nested loop example

print("Comments are fun")
# Comment example

try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid Input")
# Try and except example

open("employees.txt", "r")
# Read mode for the txt

open("employees.txt", "w")
# Write mode for the txt

open("employees.txt", "a")
# Append mode for the txt append info on the end of the file

open("employees.txt", "r+")
# Read and write

print(employee_file.readable())
# Boolean to check if the file is readable

print(employees_file.read())
# Reads and prints the info from the file

print(employees_file.readline())
# Reads the first line, if put multiple times can print every line

print(employees_file.readlines())
# Puts the lines in a list

employees_file.write("\nLeah - Customer Service")
# New line when appending

employees_file = open("employees1.txt", "w")
# Creates another file and writes

employees_file = open("index.html", "w")
# Creates a html file

employees_file.write("<p>This is HTML code inside python</p>")
# HTML code inside the file

import main

print(main.roll_dice(10))
# Module example using an external source to import into another python project

class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
# Class example data type for a "student"

from student import Student
# Referring to file and class

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Alex", "Art", 2.8, True)

print(student2.gpa)
# Object example

from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_chicken()

myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()
# Inherite example taking classes from multiple files in one

from Chef import Chef


class ChineseChef(Chef):

    def make_special_dish(self):
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")
# Importing classes to another class in a separate file with the same attributes applied and parameters modified


