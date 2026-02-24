# Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".

student = {"name":"John", "age":"20", "grade" : "A"}
print(student["name"])
# print(student["age"])
# print(student["grade"])

# Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.

product = {"name":"Laptop","price":999.99, "stock": "50"}
print(product["name"])
print(product["price"])
print(product["stock"])
product["price"] = 899.99
product['glass'] = 400
print(product)


# Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". 
# Add a new key "salary" with the value 50000.
employee = {"name":"Alice","position":"Manager" }
employee["salary"] = 50000
print(employee)


# Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively.
#  Remove the key "banana".

inventory = {"apple":8, "banana": 5, "orange": 8}
del inventory["banana"]
print(inventory)

# Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". 
# Use the copy() method to make a copy of the dictionary and call it person_copy.

person = {"name": "Bob", "age": 25, "city":"New York"}
# person_copy = {"name": "Bob", "age": 25, "city":"New York"}.copy()
person_copy = person.copy()
print(person_copy)


# Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary 
# with keys "name" and "age" with appropriate values. Access and print the age of "child2".

family ={"child1":{"name":"John", "age": 24},
         "child2":{"name":"Ben", "age": 22},
         "child3":{"name":"Pat", "age": 20}
         }
print(family["child2"]["age"])
print(family["child3"]["age"])
print(family["child1"]["name"])

# Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values 
# "Toyota", "Corolla", and 2020. Access and print the value of "model".

car = {"brand":"Toyota", "model":"Corolla", "year":2020 }  
print(car["model"])
           
# Create a dictionary called `settings` with keys "volume", "brightness", and "language", 
# and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
settings = {"volume":50, "brightness":75,"language":"English"}
settings["language"] = "Spanish"
print(settings)



# Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88.
#  Remove the key "science".

scores = {"math":90, "science":85, "english":88}
scores.pop("science")
print(scores)

# Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding 
# values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.

menu = {"starter":"Soup", "main_course":"Steak", "dessert":"Ice Cream"}
print("appetizer" in menu )

# Create a dictionary called `config` with keys "theme", "language", and "timezone", and 
# corresponding values "dark", "English", and "UTC". Clear the dictionary.

config = {"theme":"dark", "language":"English","timezone":"UTC"}
config.clear()
print(config)

# ....................................................................................................................

# ===============================
# Nested Dictionary Modification Exercises
# ===============================

# Q1. Given this dictionary, change the "math" score to 95.
student = {
    "name": "Alice",
    "scores": {"math": 80, "english": 85}
}
# Expected Output:
# {'name': 'Alice', 'scores': {'math': 95, 'english': 85}}

student = {
    "name": "Alice",
    "scores": {"math": 80, "english": 85}
}
student["scores"]["math"] = 95
print(student)


# Q2. Add a new subject "science" with score 90 inside "scores".
student = {
    "name": "Alice",
    "scores": {"math": 80, "english": 85}
}
# Expected Output:
# {'name': 'Alice', 'scores': {'math': 80, 'english': 85, 'science': 90}}

student = {
    "name": "Alice",
    "scores": {"math": 80, "english": 85}
}

student["scores"]["science"] = 90
print(student)

# Q3. Change the author's name of "Python 101" to "Mike".
library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}

# Expected Output:
# {'Python 101': {'author': 'Mike', 'year': 2020}, 'Data Science': {'author': 'Jane', 'year': 2021}}

library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}
library["Python 101"]["author"]="Mike"
print(library)


# Q4. Add a new key "publisher" = "O'Reilly" to "Data Science".
library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}
# Expected Output:
# {'Python 101': {'author': 'Tom', 'year': 2020}, 'Data Science': {'author': 'Jane', 'year': 2021, 'publisher': "O'Reilly"}}

library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}

library["Data Science"]["Publisher"] = "O'Reilly"
print(library)

# Q5. In this dictionary, add a new phone number "work": "555-999" for Alice.
contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
}
# Expected Output:
# {'Alice': {'home': '555-123', 'mobile': '555-456', 'work': '555-999'}, 'Bob': {'home': '555-789'}}
contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
    }

contacts["Alice"]["work"] = "555-999"
print(contacts)


# Q6. Change Bob’s "home" number to "555-000".
contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
}
# Expected Output:
# {'Alice': {'home': '555-123', 'mobile': '555-456'}, 'Bob': {'home': '555-000'}}

contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
}
contacts["Bob"]["home"] = "555-000"
print(contacts)

# # Q7. Add a new student {"name": "Eve", "scores": {"math": 88, "english": 92}}
# # into the list of students.
# students = [
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 70}}
# ]
# # Expected Output:
# # [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}},
# #  {'name': 'Bob', 'scores': {'math': 75, 'english': 70}},
# #  {'name': 'Eve', 'scores': {'math': 88, 'english': 92}}]

# students = {
#     {"name": "Alice", "scores": {"math": 80, "english": 85}},
#     {"name": "Bob", "scores": {"math": 75, "english": 70}}
#     }
# students[student3] = {"name": "Eve", "scores": {"math": 88, "english": 92}}
# print(students)

# Q8. Change Bob's english score from 70 to 78.
students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 70}}
] 

# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}},
#  {'name': 'Bob', 'scores': {'math': 75, 'english': 78}}]

students[1]["scores"]["english"] = 78
print(students)

# Q9. Add a new dictionary {"year": 2022, "semester": "Spring"} 
# inside Alice’s record under a new key "enrollment".
students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 78}}
]
# Expected Output:
# [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}, 'enrollment': {'year': 2022, 'semester': 'Spring'}},
#  {'name': 'Bob', 'scores': {'math': 75, 'english': 78}}]

students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 78}}
]

students[0]["enrollment"] = {'year': 2022, 'semester': 'Spring'}
print(students)

# Q10. In this shop cart, add a new product "Notebook" with price 200.
cart = {
    "items": [
        {"name": "Pen", "price": 10},
        {"name": "Book", "price": 50}
    ],
    "owner": "Alice"
}
# Expected Output:
# {'items': [{'name': 'Pen', 'price': 10}, {'name': 'Book', 'price': 50}, {'name': 'Notebook', 'price': 200}],
#  'owner': 'Alice'}

cart = {
    "items": [
        {"name": "Pen", "price": 10},
        {"name": "Book", "price": 50}
    ],
    "owner": "Alice"
}
cart["items"].update("Notebook") = 200
print(cart)

