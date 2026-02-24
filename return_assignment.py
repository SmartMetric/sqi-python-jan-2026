# # Exercise

# # Write a function sum_numbers(a, b) that returns the sum of two numbers.
# # Write a function is_even(n) that returns True if n is even and False if n is odd.
# # Write a function is_prime(n) that returns True if n is a prime number and False
# #  otherwise.
# # Using the is_prime(n) function from number 3, write a function that asks a user 
# # for an input n and returns all the prime numbers up to n.

# # Write a function lesser_of_two_evens(a, b) that returns the lesser of two given 
# # numbers if both numbers are even, but returns the greater if one or both numbers 
# # are odd.
# def lesser_of_two_evens(a, b):
#     return 
#         if a and b % 2 == 0 



# # Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# # is_alliteration(‘Levelheaded llama’) —> True
# # is_alliteration(‘Crazy Kangaroo’) –> False



# Write a function old_macdonald(name) that capitalizes the first and fourth letters 
# of a name old_macdonald(‘macdonald’) —> MacDonald
# Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.
# def old_macdonald(name):
#     return name[:0].upper + name[:3].upper
# print(old_macdonald("macdonald"))


# Write a function spy_game(list_of_ints) that takes in a list of integers and 
# returns True if it contains 007 in order.
# spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# spy_game([1, 7, 2, 0, 4, 5, 0]) —> False


# Write a function vol(radius) that computes the volume of a sphere given its
#  radius.


# Write a function range_check(num, low, high) that checks whether a number is 
# in a given range (inclusive of high and low).

def range_check(num, low, high):
    return num >= low and num <= high
print(range_check(2,1,3))


  # Write a function upper_lower(text) that accepts a string and calculates the 
  # number of uppercase letters and lowercase letters.
def upper_lower(text):
    uppercase = len([char for char in text if char.isupper()])
    lowercase = len([char for char in text if char.islower()])
    return uppercase, lowercase
print(upper_lower("MacDonAld"))

    
# Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.
#  13.	Write a function multiply(list_items) to multiply all the numbers in a list.
# 	Sample List: [1, 2, 3, -4]
# 	Expected output: -24


#  14.Write a function is_pangram(text) to check whether a string is a pangram or not. 
# 	Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# 	least once. For example: “The quick brown fox jumps over the lazy dog”.
# 	Hint: Import and use the string module.


#  15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# 	other. a word, phrase, or name formed by rearranging the letters of another, such as
# 	spar, formed from rasp.


#  16. 	Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# 	(BMI) given weight in kilograms and height in meters.
def calculate_bmi(weight, height):
    #BMI = weight (kg) / (height (m))²
    return weight / height**2
print(calculate_bmi(10, 4))


#  17. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# 	simple interest given principal amount, interest rate, and time (in years).

def calculate_simple_interest(principal, rate, time):
#SI = P × R × T / 100
    return (principal * rate * time)/100
print(calculate_simple_interest(10000, 10, 2))


#..........................................................................................................

# 3. Create a function called multiply_first_two that returns the product of the first two numbers 
# passed in.

def multiply_first_two(*numbers):
    return numbers[0] * numbers[1]
print(multiply_first_two(3, 5, 9, 2))
print(multiply_first_two(10, 2, 7))

# Test Data:
# print(multiply_first_two(multiply_first_two(*numbers)3, 5, 9, 2))
# print(multiply_first_two(10, 2, 7))

# Expected Output:
# 15
# 20


# # 4. Create a function called describe_books that prints out each book title and its author.
# def describe_books(**books):
#     return books
# print(describe_books(Hamlet="Shakespeare", ThingsFallApart="Chinua Achebe", Dune="Frank Herbert"))
# print(describe_books(Matilda="Roald Dahl", 1984="George Orwell"))

# Test Data:
# describe_books(Hamlet="Shakespeare", ThingsFallApart="Chinua Achebe", Dune="Frank Herbert")
# describe_books(Matilda="Roald Dahl", 1984="George Orwell")

# Expected Output:
# Hamlet is written by Shakespeare
# ThingsFallApart is written by Chinua Achebe
# Dune is written by Frank Herbert
# Matilda is written by Roald Dahl
# 1984 is written by George Orwell

# 5. Create a function called total_age that returns the sum of all the ages given.
def total_age(*ages):
    return sum(ages)
print(total_age(12, 30, 18))
print(total_age(40, 25))

# Test Data:
# print(total_age(12, 30, 18))
# print(total_age(40, 25))

# Expected Output:
# 60
# 65

# # 6. Create a function called list_countries that prints out each country passed in.
# def list_countries(*countries):
#     return for country in countries:
#         print(list_countries("Nigeria", "Ghana", "Kenya"))
        


# Test Data:
# list_countries("Nigeria", "Ghana", "Kenya")
# list_countries("Canada", "Mexico")

# Expected Output:
# Nigeria
# Ghana
# Kenya
# Canada
# Mexico

# 7. Create a function called student_details that prints each student’s name and score.

# Test Data:
# student_details(Fola=78, Muna=88, Kola=65)
# student_details(Sandra=91, Alex=85)

# Expected Output:
# Fola scored 78
# Muna scored 88
# Kola scored 65
# Sandra scored 91
# Alex scored 85


# 8. Create a function called average_score that returns the average of all scores passed in.

# Test Data:
# print(average_score(50, 60, 70))
# print(average_score(80, 90))

# Expected Output:
# 60.0
# 85.0

# # 7. Create a function called student_details that prints each student’s name and score.
def student_details(**students):

    for name, score in students.items():
        print(student_details(Fola=78, Muna=88, Kola=65))


# Test Data:
# student_details(Fola=78, Muna=88, Kola=65)
# student_details(Sandra=91, Alex=85)

# Expected Output:
# Fola scored 78
# Muna scored 88
# Kola scored 65
# Sandra scored 91
# Alex scored 85


# 8. Create a function called average_score that returns the average of all scores passed in.
def average_score(**scores):
    return sum(scores)/len(scores)

# Test Data:
# print(average_score(50, 60, 70))
# print(average_score(80, 90))

# Expected Output:
# 60.0
# 85.0

# 7. Create a function called student_details that prints each student’s name and score.


# Test Data:
# student_details(Fola=78, Muna=88, Kola=65)
# student_details(Sandra=91, Alex=85)

# Expected Output:
# Fola scored 78
# Muna scored 88
# Kola scored 65
# Sandra scored 91
# Alex scored 85


# 8. Create a function called average_score that returns the average of all scores passed in.

# Test Data:
# print(average_score(50, 60, 70))
# print(average_score(80, 90))

# Expected Output:
# 60.0
# 85.0

# 9. Create a function called total_price that adds up the prices of all items passed as keyword arguments.

# Test Data:
# print(total_price(bread=500, milk=1200, eggs=700))
# print(total_price(book=1500, pen=200))

# Expected Output:
# 2400
# 1700


# 10. Create a function called first_and_last that prints the first and last values passed in.

# Test Data:
# first_and_last(4, 10, 6, 9, 12)
# first_and_last("a", "b", "c", "d")

# Expected Output:
# First: 4, Last: 12
# First: a, Last: d


# 11. Create a function called describe_animals that prints out animal and their sound.

# Test Data:
# describe_animals(cat="meow", dog="bark", cow="moo")
# describe_animals(lion="roar", snake="hiss")

# Expected Output:
# cat makes the sound meow
# dog makes the sound bark
# cow makes the sound moo
# lion makes the sound roar
# snake makes the sound hiss


# 12. Create a function called total_characters that returns how many characters in total exist in all keyword values.

# Test Data:
# print(total_characters(a="banana", b="mango", c="kiwi"))
# print(total_characters(x="hi", y="there"))

# Expected Output:
# 15
# 7


# 13. Create a function called find_minimum that returns the smallest number from all the values passed in.

# Test Data:
# print(find_minimum(99, 45, 12, 88))
# print(find_minimum(8, 3, 7))

# Expected Output:
# 12
# 3


# 14. Create a function called sum_scores_and_bonuses that returns the total of all numbers passed, including keyword values.

# Test Data:
# print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
# print(sum_scores_and_bonuses(100, bonus=50))

# Expected Output:
# 50
# 150


# 15. Create a function called longest_word that returns the longest string from all the values passed in (args + kwargs).

# Test Data:
# print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
# print(longest_word("short", name="exaggeration", tool="pen"))

# Expected Output:
# hippopotamus
# exaggeration
# ====================================ASSIGNMENT===========================================

