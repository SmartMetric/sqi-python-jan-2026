# Ask the user for their name
# print the name in all uppercase letters.
# Expected output:
# HELLO JOHN

user = input("What is your name ?"  ).upper()
print("HELLO", user )

# Ask the user for their first name and last name
# print them in reverse order using one print statement.
# Expected output:
# Ajana Olumide

first_name = input("What is your first name?  ")
last_name = input("What is your last name ?  ")
print(last_name, first_name)

# Ask the user for their age
# print whether the age entered is an even number.
# Expected output:
# True

age = input("What is your age?" )
age = int(age)
print(age %2 == 0)

# Ask the user for their age
# calculate how old they will be in 10 years.
# Expected output:
# In 10 years, you will be 45 years old.

user = input("What is your age?  ")
print(int(user) + 10)

# Ask the user for two different years
# print how many years apart the two years are.
# Expected output:
# The difference is 12 years.
admission_year = 2004
graduation_year = 2016
print(int(graduation_year - admission_year))


# Ask the user to enter a word
# print the word reversed.
# Expected output:
# nohtyP

user = input("enter any word"  )
print(user[::-1])

# Ask the user to enter a sentence
# print only the first and last characters.
# Expected output:
# Se
user = input("Type sentence")
print(user[0], user[-1])

# Ask the user for a word
# check if the word remains the same when reversed.
# Expected output:
# True

user = input("Enter any word")
user = user==user[::-1]
print(user)

# Ask the user for a password
# print whether the password length is an odd number.
# Expected output:
# False

user = input("enter paaword")
user = len(user) % 2 ==1
print(user)

# Ask the user for a password
# print True if the password length is at least 10 characters.
# Expected output:
# True

user = input("enter your pin")
user = len(user) >= 10
print(user)
