# --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------
# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
digits = [1, 2, 3, 4, 5]
 



# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
names = ["John", "Sara", "Mike", "Amanda"]


# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
values = [5, 12, 3, 18, 7]


# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
animals = ["dog", "cat", "lion", "tiger"]

# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
values = [5, 12, 3, 18, 7]


# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
names = ["John", "Sara", "Mike", "Amanda"]

# 7. Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

# 8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
words = ["apple", "zebra", "mango", "lemon"]

# 9. Is there any email address that contains ".org"?
# Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# Expected Output: True
emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]

# 10. Are all numbers odd?
# Input: [1, 3, 5, 7, 9]
# Expected Output: True
values = [1, 3, 5, 7, 9]


# 11. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
words = ["hi", "dog", "go", "sun"]


# 12. Create a list of triple the value of each number
# Input: [2, 4, 6, 8]
# Expected Output: [6, 12, 18, 24]
nums = [2, 4, 6, 8]


# 13. Are all temperatures above 0°C?
# Input: [12, 7, 3, -1, 5]
# Expected Output: False
temperatures = [12, 7, 3, -1, 5]

# 14. Do all words end with a vowel?
# Input: ["banana", "mango", "kiwi", "grape"]
# Expected Output: True
fruits = ["banana", "mango", "kiwi", "grape"]


# 15. Create a list of words in lowercase
# Input: ["HELLO", "WORLD", "PYTHON"]
# Expected Output: ["hello", "world", "python"]
greetings = ["HELLO", "WORLD", "PYTHON"]

# 16. Is there any number less than 0?
# Input: [5, -2, 3, 0, 8]
# Expected Output: True
numbers = [5, 4, 3, 3, 8]


# 17. Create a list of words that contain the letter 'e'
# Input: ["sky", "tree", "rock", "stone"]
# Expected Output: ["tree", "stone"]
items = ["sky", "tree", "rock", "stone"]


# 18. Are all names starting with uppercase letters?
# Input: ["Alice", "Bob", "charlie", "David"]
# Expected Output: False
names = ["Alice", "Bob", "charlie", "David"]


# 19. Is there any sentence longer than 20 characters?
# Input: ["Short one", "This is a much longer sentence", "Okay"]
# Expected Output: True
sentences = ["Short one", "This is a much longer sentence", "Okay"]


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