
# --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------

# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
digits = [1, 2, 3, 4, 5]

square = [digit ** 2 for digit in digits ]
print(square)


# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
names = ["John", "Sara", "Mike", "Amanda"]
names_with_a = [name for name in names if "a" in name.lower()]
print(names_with_a)


# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
values = [5, 12, 3, 18, 7]
list_booleans = [value >10 for value in values ]
print(list_booleans)

# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
animals = ["dog", "cat", "lion", "tiger"]
last_character = [animal[-1]for animal in animals]
print(last_character)


# 12. Create a list of triple the value of each number
# Input: [2, 4, 6, 8]
# Expected Output: [6, 12, 18, 24]
nums = [2, 4, 6, 8]
triple = [number*3 for number in nums]
print(triple)

# 15. Create a list of words in lowercase
# Input: ["HELLO", "WORLD", "PYTHON"]
# Expected Output: ["hello", "world", "python"]
greetings = ["HELLO", "WORLD", "PYTHON"]
lowercase = [word.lower() for word in greetings]
print(lowercase)


# 17. Create a list of words that contain the letter 'e'
# Input: ["sky", "tree", "rock", "stone"]
# Expected Output: ["tree", "stone"]
items = ["sky", "tree", "rock", "stone"] 
list_with_e = [item for item in items if "e" in item.lower()]
print(list_with_e)




fruits = ["apple", "banana", "orange", "mango"]

position = 1

for fruit in fruits:
    print(position, fruit)
    position = position + 1

fruits = ["apple", "banana", "orange", "mango"]

for position, fruit in enumerate(fruits, start=1):
    print(position, fruit)

fruits = ["apple", "banana", "orange"]

for count, fruit in enumerate(fruits, start=1):
    print(count, fruit)

values = [5, 12, 3, 18, 7]

for index, value in enumerate(values):
    if value > 10:
        print(index, value)


animals = ["dog", "cat", "lion", "tiger"]

for index, animal in enumerate(animals):
    if animal == "lion":
        print(f"The result is {animal} @ index {index}")



