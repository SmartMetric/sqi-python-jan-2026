# # Scenario: You need to check if a user's password is strong enough.

# # Task: Write a program in a file named `password_strength_checker.py` that takes a string called `password` and prints `True` if the password is strong and `False` otherwise. A strong password:

# # Is at least 8 characters long.
# # Contains both uppercase and lowercase characters.
# # Contains at least one digit.
# # Contains at least one special character (e.g., !@#$%^&*()).





# password = "p@ssw0rd123"

# is_at_least_8_chars_long = len(password) >= 8

# has_upper = any(char.isupper() for char in password)
# has_lower = any(char.islower() for char in password)

# print(all([is_at_least_8_chars_long, has_upper, has_lower]))
# print(is_at_least_8_chars_long and has_upper and has_lower)


# #Complete the one I started using list comprehensions, and do the same exercise using a single for loop


































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












