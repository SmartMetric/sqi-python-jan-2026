

# ```
# # -------------------------
# # EXERCISE 1
# # -------------------------
# # Create a function called greet()
# # It should print: Hello there!
# #
# # Expected output:
# # Hello there!
# #
# # Function call:
# # greet()

def greet():
    print("Hello there!")
greet()



# # -------------------------
# # EXERCISE 2
# # -------------------------
# # Create a function called say_name(name)
# # It should print the name in all caps
# #
# # Expected output:
# # JOHN
# #
# # Function call:
# # say_name("John")
def say_name(name):
  name_upper= name.upper()
  print(name_upper)
say_name("John")


# # -------------------------
# # EXERCISE 3
# # -------------------------
# # Create a function called show_age(age)
# # It should print: You are <age> years old
# #
# # Expected output:
# # You are 15 years old
# #
# # Function call:
# # show_age(15)
def show_age(age):
   print(f"You are {age} years old")
show_age(15)


# # -------------------------
# # EXERCISE 4
# # -------------------------
# # Create a function called multiply_by_two(num)
# # It should print the number multiplied by 2
# #
# # Expected output:
# # 20
# #
# # Function call:
# # multiply_by_two(10)
def multiply_by_two(num):
   num = num * 2
   print(num)
multiply_by_two(10)

# # -------------------------
# # EXERCISE 5
# # -------------------------
# # Create a function called subtract_numbers(a, b)
# # It should print the result of a - b
# #
# # Expected output:
# # 7
# #
# # Function call:
# # subtract_numbers(10, 3)

def subtract_numbers(a, b):
   result = a-b
   print(result)
subtract_numbers(10, 3)

# # -------------------------
# # EXERCISE 6
# # -------------------------
# # Create a function called ask_and_square()
# # The function should:
# # - Ask the user to enter a number
# # - Print the square of that number
# #
# # Expected input:
# # 4
# #
# # Expected output:
# # 16
# #
# # Function call:
# # ask_and_square()

def ask_and_square():
    number = int(input("Enter a number:    "))
    result = number **2
    print(result)
ask_and_square()


# # -------------------------
# # EXERCISE 7
# # -------------------------
# # Create a function called print_length(word)
# # It should print the length of the word
# #
# # Expected output:
# # 6
# #
# # Function call:
# # print_length("Python")

def print_length(word):
    length_of_word = len(word) 
    print(length_of_word)
print_length("Python")

# # -------------------------
# # EXERCISE 8
# # -------------------------
# # Create a function called add_three_numbers(a, b, c)
# # It should print the sum of the three numbers
# #
# # Expected output:
# # 12
# #
# # Function call:
# # add_three_numbers(3, 4, 5)
def add_three_numbers(a, b, c):
    sum = a + b + c
    print(sum)
add_three_numbers(3, 4, 5)


# # -------------------------
# # EXERCISE 9
# # -------------------------
# # Create a function called repeat_word(word)
# # It should print the word 3 times on the same line
# #
# # Expected output:
# # hi hi hi
# #
# # Function call:
# # repeat_word("hi")

def repeat_word(word):
   result = (word + " ") * 3
   print(result)
  
repeat_word("hi")



# # -------------------------
# # EXERCISE 10
# # -------------------------
# # Create a function called ask_name_and_greet()
# # The function should:
# # - Ask the user to enter their name
# # - Print: Hello <name>
# #
# # Expected input:
# # Winnie
# #
# # Expected output:
# # Hello Winnie
# #
# # Function call:
# # ask_name_and_greet()
# ```

def ask_name_and_greet():
    name = input("Enter your name:    ")
    print(f"Hello {name}")

ask_name_and_greet()


# 7. Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

words_only_uppercase = all(words.isupper() for words in greetings)
print(words_only_uppercase)




#8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
words = ["apple", "zebra", "mango", "lemon"]

start_z= any(word.startswith("z") for word in words)

print(start_z)

#11. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
words = ["hi", "dog", "go", "sun"]

longer_than_2= all(len(word) > 2 for word in words)
print(longer_than_2)


# 14. Do all words end with a vowel?
# Input: ["banana", "mango", "kiwi", "grape"]
# Expected Output: True
fruits = ["banana", "mango", "kiwi", "grape"]
vowels = "aeiouAEIOU"

endwith_vowel = all(word[-1] in vowels for word in fruits) 
print(endwith_vowel)



# 15. Create a list of words in lowercase
# Input: ["HELLO", "WORLD", "PYTHON"]
# Expected Output: ["hello", "world", "python"]
greetings = ["HELLO", "WORLD", "PYTHON"]

lowercase= [word.lower() for word in greetings]
print(lowercase)


# # Scenario: You need to check if a user's password is strong enough.

# # Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# # Is at least 8 characters long.
# # Contains both uppercase and lowercase characters.
# # Contains at least one digit.
# # Contains at least one special character (e.g., !@#$%^&*()).



password = input("Enter your password:    ").strip()
special_character= "!@#$%^&*()"

atleast_8_characters = len(password) >= 8

has_upper = any(char.isupper() for char in password)

has_lower = any(char.islower() for char in password)

has_digit = any(char.isdigit() for char in password)

has_special = any(char in special_character for char in password)

all_check= all((atleast_8_characters,has_upper,has_lower,has_digit,has_special))
if all_check:
    print("Correct Password")
else:
    print("Incorrect Password")




def add_two_nums(a, b):
    return (a + b)


print(add_two_nums(3, 4))


# def all_except_lagos (State





