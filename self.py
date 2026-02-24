# Given the string username = "administrator",
# use indexing to print the first character.
# Expected output:
# a
username = "administrator"
print(username[0])

# Given the string error_code = "PermissionDenied",
# use negative indexing to print the last character.
# Expected output:
# d
error_code = "PermissionDenied"
print(error_code[-1])

# Given the strings first = "Data" and second = "Science",
# use string concatenation to print them with a space in between.
# Expected output:
# Data Science
first = "Data" 
second = "Science"
print(first + " " + second)

# Given the variables name = "Ayo" and score = 85,
# use string interpolation to print the message below.
# Expected output:
# Ayo scored 85 in the test
name = "Ayo"

score = "85"
print (f"{name} scored {score} in the test")

# Given the string palindrome = "racecar",
# use slicing to reverse the string and print the result.
# Expected output:
# racecar
palindrome = "racecar"
print(palindrome[ ::-1])

# Given the string framework = "DjangoRestFramework",
# use slicing to extract and print the word "Rest".
# Expected output:
# Rest
framework = "DjangoRestFramework"
print(framework[6:10])

# Given the string warning = "Unauthorized access detected!",
# use slicing to print every second character.
# Expected output:
# Uatoie cesdtce!

warning = "Unauthorized access detected!"
print(warning[::2])

# Given the string text = "automation",
# use a string method to convert it to uppercase and print the result.
# Expected output:
# AUTOMATION
text = "automation"
print(text.upper())

# Given the string email = " ADMIN@COMPANY.COM ",
# use string methods to remove extra spaces and convert it to lowercase.
# Expected output:
# admin@company.com

email = " ADMIN@COMPANY.COM "
email = email.strip()
email = email.lower()
print(email)

# Given the string message = "Error: Disk Full Error",
# use a string method to count how many times "Error" appears.
# Expected output:
# 2
message = "Error: Disk Full Error"
print(message.count("Error"))

# Given the string ref = "INV-2025-00987",
# use slicing to print only the numeric part at the end.
# Expected output:
# 00987
ref = "INV-2025-00987"
print(ref[-5::])

# Given the string word = "Python",
# use indexing to print the third character.
# Expected output:
# t
word = "Python"
print(word[2])

# Given the string sentence = "System overload detected",
# use slicing to print the last 8 characters.
# Expected output:
# detected

sentence = "System overload detected"
print(sentence[-8::])

# Given the string data = "12345",
# use a string method to check if it contains only digits and print the result.
# Expected output:
# True
data = "12345"
print(data.isdigit())

# Given the string log = "Disk Full Error",
# use a string method to replace "Error" with "Warning" and print the result.
# Expected output:
# Disk Full Warning

log = "Disk Full Error"
log = "Disk Full Error".replace("Error", "Warning")
print(log)

# Complex Realistic Question 1

# You are given the following string:
# log_entry = "  ID=MK987, STATUS=FAILED, REASON=Timeout Error, ATTEMPTS=3  "
# Task: Transform the string so that the final output is:


# 3:spmtta o,rorT= nosaer ,DEALF=SUTATS,mk987=di
# i=,d,sr3pmtt

# id=mk987,status=FAILED,reason=Timeout Attempt,attempts=3
log_entry = "  ID=MK987, STATUS=FAILED, REASON=Timeout Error, ATTEMPTS=3  "
log_entry = "  ID=MK987, STATUS=FAILED, REASON=Timeout Error, ATTEMPTS=3  ".replace("ID=MK987", "id=mk987").replace("STATUS", "status").replace("Error", "Attempt").replace("ATTEMPTS", "attempts").replace("REASON", "reason")
print(log_entry.strip())

# MK987 made 3 attempts
log_entry = "  ID=MK987, STATUS=FAILED, REASON=Timeout Error, ATTEMPTS=3  "
newlog_entry = log_entry[5:10] + " "+ "made 3 attempts"
print(newlog_entry)

# 3:spmtta o,rorT= nosaer ,DEALF=SUTATS,mk987=di
log_entry = "  ID=MK987, STATUS=FAILED, REASON=Timeout Error, ATTEMPTS=3  "
reversed_log_entry = log_entry[::-1].replace("=" , ":").replace("STPMETTA" , "spmtta")
print(reversed_log_entry)

# Create a variable to store the value 50 using a valid variable name
# and print the value.
# Expected output:
# 50

value = 50
print(value)

# Identify which of the following variable names is invalid and explain why:
# # user-name = "Admin"
# answer = user-name. 
# reason: it does not comply with python standard

# Given the variable total_score = 92,
# use the type() function to print its data type.
# Expected output:
# <class 'int'>

total_score = 92
print(type(total_score))

# Create a multi-line string that prints the text below exactly as shown:
# Welcome to Python
# Learning is fun
text = "Welcome to Python Learning is fun"
print("""Welcome to Python Learning is fun""")

# Given the string text = "It's a beautiful day",
# print the string without causing a syntax error.
# Expected output:
# It's a beautiful day

text = "It's a beautiful day"
print(text)

# Given the string word = "Python",
# attempt to change the first character to "J"
# and observe the result.
# Expected output:
# An error message

word = "Python"
print("J"+word[1::])

# Given the variable age = "25",
# convert it to an integer and print the result.
# Expected output:
# 25

age = "25"
print(int(age))

# Given the variables a = 10 and b = 2.5,
# add them together and print the result.
# Expected output:
# 12.5

a = 10 
b = 2.5
print(a+b)

# Given x = 10 and y = 5,
# check if x is greater than y and print the result.
# Expected output:
# True

x = 10  
y = 5
print(x>=y)

# Given is_admin = True and is_logged_in = False,
# use AND logic to evaluate access and print the result.
# Expected output:
# False
is_admin = True 
is_logged_in = False
print(is_logged_in)


# Given the value data = "",
# use the bool() function to evaluate it and print the result.
# Expected output:
# False

data = "" 
print(bool(data))

# Given the variable items = 3,
# use bool() to evaluate it and print the result.
# Expected output:
# True

items = 3
print(bool(items))


# Write a single-line comment explaining what the print() function does.
# print function display result/ output

# Write a multi-line comment describing a program
# that collects a user's name and age.
statement = """ The story is about the customer relationship management that was newly inroduced into God s good logistics international express limted"""
print(statement)


# Given the input age = input("Enter your age: ")
# convert the input to an integer and print its data type.
# Expected output:
# <class 'int'>


# Given the input age = input("Enter your age: ")
# convert the input to an integer and print its data type.
# Expected output:
# <class 'int'>

age = input("Enter your age: ")
age = int(age)
print(type(age))


# Given the input price = input("Enter the price: ")
# convert the value to a float and print the result.
# Expected output:
# 1500.5

price = input("Enter the price: ")
price = float(price)
print((price))

# Given the input name = input("Enter your name: ")
# check the data type of name and print it.
# Expected output:
# <class 'str'>

name = input("Enter your name: ")
name = type(name)
print(name)

# Given x = 7 and y = 2.5
# add both values and print the result.
# Expected output:
# 9.5

x = 7 
y = 2.5
print(x + y)

# Given a = 4 and b = 3.0
# multiply both values and print the data type of the result.
# Expected output:
# <class 'float'>

x = 7 
y = 2.5
print(type(x + y))

# Given is_active = True
# print the value and its data type.
# Expected output:
# True
# <class 'bool'>

is_active = True
print(bool(is_active))


# Given num1 = 10 and num2 = 20
# check if num1 is greater than num2 and print the result.
# Expected output:
# False

num1 = 10 
num2 = 20 
print(num1>num2)


# Given a = True and b = False
# use AND logic to print the result.
# Expected output:
# False

a = True
b = False
print(a and b)


# Given a = True and b = False
# use OR logic to print the result.
# Expected output:
# True

a = True 
b = False
print(a or b )

# Given value = 0
# use bool() to evaluate the value and print the result.
# Expected output:
# False

value = 0
print(bool(value))

# Given value = "Python"
# use bool() to evaluate the value and print the result.
# Expected output:
# True

value = "Python"
print(bool(value))

# Given value = ""
# use bool() to check the value and print the result.
# Expected output:
# False

value = ""
print(bool(value))

# Given value = " "
# use bool() to check the value and print the result.
# Expected output:
# True

value = " "
print(bool(value))

# Given input_text = input("Enter something: ")
# use bool() to check if the user entered any value and print the result.
# Expected output:
# True

input_text = input("Enter something: ")
print(bool(input_text))

# Given number = input("Enter a number: ")
# convert the input to an integer and check if it is greater than 0.
# Expected output:
# True

number = input("Enter a number: ")
print(int(number)> 0)
































