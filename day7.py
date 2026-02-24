# Attempt to modify the character at index 2 in the string "Python" from question 9. Print the resulting error message.
# value = "Python"
# (value[1]) = x
# print(x)
# NameError: name 'x' is not defined


# Assign values "Orange", "Banana", "Cherry" to multiple variables x, y and z in one line respectively.
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)


# 12.	Assign the values 10, "John", and True to the variables age, name, and is_student in a 
# single line.
age, name, is_student = "10", "John", True
print(age, name, is_student)

#  13. 	Swap the values of x and y, where x = 5 and y = 10, without using a temporary variable.
x, y = 5, 10
x, y = 10, 5
print(x,y)


#  14. 	Create a list of numbers with values 1, 2, and 3. Unpack the list into separate 
# variables a, b, and c.
numbers = 1, 2, 3
a, b, c = numbers
print(a, b, c) 



#  15. 	Convert a string variable called height from “1.35” to a float.
height = "1.35"
height = str(1.35)
print(height)

#  16.	Predict the output of the following statements:
# 	a) bool("") --- False
# b) bool(123) --- True 
# c) bool(["apple", "cherry", "banana"]) --- True
# d) bool(False) --- False
# e) bool(None) --- False
# f) bool(0) --- False
# g) bool("abc") --- True
# h) bool(()) --- False
# i) bool([]) --- False
# j) bool({}) --- False
# 17.	Convert a string “James John Kennedy” called “names” to a list using the string 
# .split() method. Store the result in a list called “names_list”
names = "James John Kennedy"
name_list = names.split()
print(name_list)


# 18.	You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# 'Chicago']. Convert this list into a single string where each city is separated by a 
# semicolon and a space. Store the result in a string called cities_string.
cities_list = ['New York', 'Los Angeles', 'Chicago']
cities_string = "; ".join (cities_list)
print(cities_string)



# --------------------------------------------------------------------------------------
# Scenario: You need to format the details of a book in order to make it more readable.
# Task: Write a program named `book_info_beautifier.py`. You are given a string called `book_info`. It is of the format:
# author ; book title ; year published ; isbn number ; number of pages ; cost
# Assume that semicolons (;) are only used to separate the components, and not used in any of the components 
# themselves. Also assume that all the components are always given.

# Example input:
# book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"

# Instructions:
# Extract and preprocess the components:
# Author: Capitalize the first letter of the author's names i.e. title case
# Book Title: Trim any leading and trailing whitespaces and convert the title to be in title case.
# ISBN Number: Correct the typo in the ISBN number by replacing ISN with ISBN.
# Cost: Format the cost to 2 decimal places and prepend the naira symbol ₦.
# Format the information into a new multi-line string called `formatted_book_info` using an f-string or the format method.
# The output should be of the format:
# The book `book_title` was written by `author` and published in `year_published`.
# It has `no_of_pages` pages and `isbn` and costs `cost`.
# Using the example above, the expected output is: 
# The book The Art Of Programming was written by John Doe and published in 2020.
# It has 350 pages and ISBN 978-3-16-148410-0 and costs ₦2500.00.

# Steps:
# Split the `book_info` string into its components using `.split(“ ; “)`.
# Preprocess each component as described.
# Create and print the `formatted_book_info` string.

#  "george orwell ; 1984 ; 1949 ; ISN 978-0-452-28423-4 ; 328 ; 1999"
# The book 1984 was written by George Orwell and published in 1949.
# It has 328 pages and ISBN 978-0-452-28423-4 and costs ₦1999.00.
author = "George Orwell".lower()
title = "1984"
publication_year = "1949"
pages = "328"
ISBN = "978-0-452-28423-4"
price = "1999"
book_info = f"{author}; {title} ; {publication_year} ; {ISBN} ; {price}"
print(book_info)


# ------------------------------------------------------------------------------------------------------
# Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.
name = input("what is your name ?  ")
print(f"Hello, {name}!")

dob= input("When is your year of birth? ")
dob = int(dob)
from datetime import datetime
current_year = datetime.now().year
age = current_year - dob
print(f"You are {age}years old")

# Ask the user for their favourite color. Print a statement that includes the color in the format 
# “Your favorite color is {favourite_color}.”.

favourite_colour = input("What is favourite colour ?  ")
print(f"favourite_colour is {favourite_colour}")

#**** Create a program that asks the user to input a password ****and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# Bonus point if you can hide the password input from displaying on the screen as clear text.
from getpass import getpass
password = getpass("Enter your password?  ")
print({password})

# Write a program that asks the user for their weight (in kilograms) and height (in meters) and 
# calculates their Body Mass Index (BMI). Calculate the BMI using the formula 
# BMI = weight / (height ** 2). Round the BMI to 2 decimal places. 
# Print a statement in the format “Your BMI is {BMI}”
weight = input("What is your weight (kg)?  ")
height = input("What is your height (m)?  ")
BMI = weight / (height **2)
print(f"Your BMI is {BMI}")

#***** Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.
# Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”
time_in_mins = int(input("enter time in minutes"))
hour = time_in_mins // 60
minutes = time_in_mins % 60
print(time_in_mins)
