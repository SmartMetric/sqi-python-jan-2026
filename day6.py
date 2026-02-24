# #17.	Convert a string “James John Kennedy” called “names” to a list using the string
name = "James John Kennedy"
print(name.split())

# .#split() method. Store the result in a list called “names_list”

# 18.	You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# 'Chicago']. Convert this list into a single string where each city is separated by a 
# semicolon and a space. Store the result in a string called cities_string.
cities_list = ['New York', 'Los Angeles', 'Chicago']
print(': '.join(cities_list))

# 19.	Create a string variable sentence with the value "the quick brown fox jumps over the 
# lazy dog". Capitalize the first letter of the string and 
# print the result.
statement = "the quick brown fox jumps over the lazy dog"
print(statement.capitalize())

# 20. 	Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# the first letter of each word and print the result.
statement = "to kill a mockingbird"
print(statement.title())

# 21. 	Create a string variable text with the value "hello world". Count the number of 
# occurrences of the letter 'o' and print the result.
value = "hello world"
print(value.count("o"))

# 22. 	Create a string variable filename with the value "document.txt". Check if the string 
# starts with "doc" and print the result.
value = "document.txt"
print(value.startswith("doc"))


# 23.	Create a string variable url with the value "https://www.example.com". Check if the 
# string ends with ".com" and print the result.
value = "https://www.example.com"
print(value.endswith('com'))

# 24.	Create a string variable phrase with the value "find the needle in the haystack". Find 
# the position of the word "needle" and print the result.
value ="find the needle in the haystack"
print(value.find("needle"))


# 25.	Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# Result. Bonus point if you can do it with the f-string and concatenation methods also.
value = "Hello, {}. Welcome to {}."
female = "Alice"
male = "Wonderland"
print(value.format(female,male))


# 26.	Create a string variable `quote` with the value "To be or not to be". Find the position 
# of the word "not" and print the result.
value = "To be or not to be"
print(value.find("not"))

# 27.	Create a string variable word with the value "hello". Check if all characters in the 
# string are lowercase and print the result.
value = "hello"
print(value.islower())

# 28.	Create a string variable shout with the value "HELLO". Check if all characters in the 
# string are uppercase and print the result.
value = "HELLO"
print(value.isupper())

# 29.	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# lowercase and print the result.
value = "PyThOn"
print(value.lower())


# 30. 	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# uppercase and print the result.
alue = "PyThOn"
print(value.upper())


# 31. 	Create a string variable padded_text with the value " hello ". Remove leading whitespace and 
# print the result.
value = " hello "
print(value.lstrip())

# 32. 	Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# print the result.
value = " hello "
print(value.rstrip())

# 33.	Create a string variable padded_text with the value " hello ". Remove both leading and trailing 
# whitespace and print the result.
value = " hello "
print(value.strip())
# 34.	Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# and print the result.
old_value = "Hello, World!"
new_value = old_value.replace("World","Alice")
print(new_value)