# Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# length, width, and height, and print each variable.

dimension = 10, 20, 30
length, width, breath = dimension
print(length) 
print(width)
print(breath)

# # Given the tuple coordinates:
# coordinates = (1.5, 2.5, 3.5)
# # Unpack the tuple into variables x, y, and z, and print the value of y.

coordinates = (1.5, 2.5, 3.5)
x, y, z = coordinates
print(y)

# Create a tuple called person with values ("John", 25, "Engineer"). 
# Unpack the values into variables name, age, and profession, and print the value of profession.
personal_profile = ("John", 25, "Engineer")
name, age, role = personal_profile
print(role)

# Given the nested tuple data:
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# Unpack the first element of data into variables student1 and student2, and print student2.

data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
((student1, student2), (course1, course2), (score1, score2)) = data
print(student2)

# Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two values into variables
#  color1 and color2, and print both variables.

colors =  ("red", "green", "blue", "yellow")
color1, color2, *_ = colors
print(color1, color2)


# Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. 
# Print the extracted age and the first department.

record = ("Jane", (32, "Manager"), ["HR", "Finance"])
_, (age, position ), [dept1, dept2] = record
print(age, dept1)

# Create a tuple called triplet with values ("one", "two", "three"). 
# Unpack the tuple into variables and print the value of the second variable.

triplet = ("one", "two", "three")
taye, kehinde, eta = triplet
print(kehinde)


# Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. 
# Print the category and the manufacture year.
info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
productID, (category, price), (day, month, year) = info
print(category, year)
 
# Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). 
# Unpack the nested tuples into individual variables and print the second value of the third tuple.

# values =  (("a", "b"), ("c", "d"), ("e", "f"))..........................................


# Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.

inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
(fruit1, Quantity1), (fruit2, Quantity2), (fruit3, Quantity3) = inventory
print(Quantity2)


