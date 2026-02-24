# # # # # # # # # # # # # # # # # Question 1

# # # # # # # # # # # # # # # # # Input:

# # # # # # # # # # # # # # # # # ["pen", "pencil", "eraser"]


# # # # # # # # # # # # # # # # # Print each item with its position starting from 1.

# # # # # # # # # # # # # # # # tools=["pen", "pencil", "eraser"]
# # # # # # # # # # # # # # # # for position, tool in enumerate(tools, 1):
# # # # # # # # # # # # # # # #     print(tool, position)

# # # # # # # # # # # # # # # # Question 2

# # # # # # # # # # # # # # # # Input:

# # # # # # # # # # # # # # # # ["dog", "cat", "lion", "tiger"]


# # # # # # # # # # # # # # # # Print the index of "tiger".

# # # # # # # # # # # # # # # animals = ["dog", "cat", "lion", "tiger"]
# # # # # # # # # # # # # # # for index, animal in enumerate(animals):
# # # # # # # # # # # # # # #     if animal == "tiger":
# # # # # # # # # # # # # # #         print(index)


# # # # # # # # # # # # # # # Question 3

# # # # # # # # # # # # # # # Input:

# # # # # # # # # # # # # # # [10, 25, 7, 40, 18]


# # # # # # # # # # # # # # # Print only the numbers greater than 20, together with their index.

# # # # # # # # # # # # # # numbers = [10, 25, 7, 40, 18]
# # # # # # # # # # # # # # for index, number in enumerate(numbers, 1):
# # # # # # # # # # # # # #     if number > 20:
# # # # # # # # # # # # # #         print(number, index)

# # # # # # # # # # # # # # Question 4

# # # # # # # # # # # # # # Input:

# # # # # # # # # # # # # # ["HELLO", "WORLD", "PYTHON"]


# # # # # # # # # # # # # # Print each word in lowercase, prefixed with its position starting from 1.

# # # # # # # # # # # # # words = ["HELLO", "WORLD", "PYTHON"]
# # # # # # # # # # # # # for position, word in enumerate(words, 1):
# # # # # # # # # # # # #     lowercase_word = word.lower()
# # # # # # # # # # # # #     print(position, lowercase_word)




# # # # # # # # # # # # # Question 5

# # # # # # # # # # # # # Input:

# # # # # # # # # # # # # ["red", "blue", "green", "blue", "yellow"]


# # # # # # # # # # # # # Print all indexes where "blue" appears.

# # # # # # # # # # # # colors = ["red", "blue", "green", "blue", "yellow"]
# # # # # # # # # # # # for indexes, color in enumerate(colors):
# # # # # # # # # # # #    if color == "blue":
# # # # # # # # # # # #     print(indexes, color)


# # # # # # # # # # # # Question 6

# # # # # # # # # # # # Input:

# # # # # # # # # # # # [3, 6, 9, 12, 15]


# # # # # # # # # # # # Print:

# # # # # # # # # # # # "EVEN position" if the position is even

# # # # # # # # # # # # "ODD position" if the position is odd
# # # # # # # # # # # # along with the number
# # # # # # # # # # # # (positions start from 1).

# # # # # # # # # # # # nunbers = [3, 6, 9, 12, 15]
# # # # # # # # # # # # for position, number in enumerate(nunbers, 1):
# # # # # # # # # # # #     if number % 2 == 0:
# # # # # # # # # # # #         print(f"EVEN position")
# # # # # # # # # # # #     elif number % 2 != 0:
# # # # # # # # # # # #         print(f"ODD position")

# # # # # # # # # # # # Question 7

# # # # # # # # # # # # Input:

# # # # # # # # # # # # ["apple", "banana", "kiwi", "mango"]


# # # # # # # # # # # # Print only the items that have more than 5 characters, along with their index.
# # # # # # # # # # # fruits = ["apple", "banana", "kiwi", "mango"]
# # # # # # # # # # # for index, fruit in enumerate(fruits, 1):
# # # # # # # # # # #     if len(fruit) > 5:
# # # # # # # # # # #         print(fruit, index)


# # # # # # # # # # # Question 8

# # # # # # # # # # # Input:

# # # # # # # # # # # ["Ada", "Bola", "Chidi", "Dami"]


# # # # # # # # # # # Print:

# # # # # # # # # # # Student <position>: <name>


# # # # # # # # # # # Positions should start from 1.


# # # # # # # # # # students = ["Ada", "Bola", "Chidi", "Dami"]
# # # # # # # # # # for Positions, student in enumerate(students, 1):
# # # # # # # # # #     print(f"Student {Positions}: {student}")


# # # # # # # # # # Question 9

# # # # # # # # # # Input:

# # # # # # # # # # [5, 12, 3, 18, 7]


# # # # # # # # # # Print the index and value only for numbers that are odd.

# # # # # # # # # numbers = [5, 12, 3, 18, 7]
# # # # # # # # # for index, number in enumerate(numbers, 1):
# # # # # # # # #     if number % 2 != 0:
# # # # # # # # #         print(index, number)

# # # # # # # # # Question 10

# # # # # # # # # Input:

# # # # # # # # # ["cat", "dog", "elephant", "ant"]


# # # # # # # # # Print the index and word only if the word starts with the letter "a" or "e".

# # # # # # # # animals = ["cat", "dog", "elephant", "ant"]
# # # # # # # # for index, animal in enumerate(animals):
# # # # # # # #     if animal.startswith(("a" , "e")):
# # # # # # # #         print(index, animal)




# # # # # # # # Question 1

# # # # # # # # Input:

# # # # # # # # ["chair", "table", "desk", "shelf"]


# # # # # # # # Print only the position and item for items whose position is even.
# # # # # # # # Positions must start from 1.

# # # # # # # # Expected style (example):

# # # # # # # # 2 table
# # # # # # # # 4 shelf

# # # # # # # # Question 2

# # # # # # # # Input:

# # # # # # # # [11, 4, 9, 20, 7]


# # # # # # # # Print the index and value for numbers that are odd.
# # # # # # # # Index must start from 0.

# # # # # # # # Question 3

# # # # # # # # Input:

# # # # # # # # ["blue", "green", "red", "yellow", "blue"]


# # # # # # # # Print all positions (starting from 1) where "blue" appears.
# # # # # # # # Print only the position, nothing else.

# # # # # # # # Question 4

# # # # # # # # Input:

# # # # # # # # [100, 200, 300, 400]


# # # # # # # # Print:

# # # # # # # # "EVEN position" and the value if the position is even

# # # # # # # # "ODD position" and the value if the position is odd

# # # # # # # # Positions must start from 1.

# # # # # # # # Question 5

# # # # # # # # Input:

# # # # # # # # ["ant", "dog", "elephant", "cat", "eagle"]


# # # # # # # # Print index and word only if:

# # # # # # # # the word starts with "a" or "e"

# # # # # # # # Index must start from 0.




# # # # # # # names = ["Ada", "Bola", "Chidi", "Dami"]
# # # # # # # scores = [85, 70]

# # # # # # # for name, score in zip(names, scores):
# # # # # # #     print(name, score)

# # # # # # # # Question 1

# # # # # # # # Input:

# # # # # # # person = {"name": "Ada", "age": 20, "city": "Lagos"}


# # # # # # # # Print each key with its position starting from 1.

# # # # # # # for position, key in enumerate(person, 1):
# # # # # # #     print(position, key)

# # # # # # # Question 2

# # # # # # # Input:

# # # # # # # prices = {"bread": 1200, "milk": 800, "eggs": 1500}


# # # # # # # Print each position, key, and value on one line.

# # # # # # prices = {"bread": 1200, "milk": 800, "eggs": 1500}
# # # # # # for position, (key, value) in enumerate(prices.items(), 1):
# # # # # #     print(position, key, value)





# # # # # # # Question 3

# # # # # # # Input:

# # # # # # # scores = {"Ada": 85, "Bola": 70, "Chidi": 90, "Dami": 60}


# # # # # # # Print only the names whose position is even.

# # # # # # scores = {"Ada": 85, "Bola": 70, "Chidi": 90, "Dami": 60}
# # # # # # for position , name in enumerate(scores, 0) :
# # # # # #     if position % 2 == 0:
# # # # # #         print(position, name )
 





# # # # # # # Question 4

# # # # # # # Input:

# # # # # # # inventory = {"Pen": 100, "Book": 500, "Eraser": 50}


# # # # # # # Print only the items whose value is greater than 100, together with their position.

# # # # # # inventory = {"Pen": 100, "Book": 500, "Eraser": 50}
# # # # # # for position, (key, value) in enumerate(inventory.items(), 1):
# # # # # #     if  value> 100:
# # # # # #         print(position, key, value)

# # # # # # Question 5
# # # # # # Print:

# # # # # # <position> <key> -> <value>
# # # # # # Input:

# # # # # # user = {"username": "olu", "role": "admin", "status": "active"}
# # # # # # for position, (key, value) in enumerate(user.items(), 1):
# # # # # #     print(position, key, "->", value)

# # # # # # Question 6

# # # # # # Input:
# # # # # # Print the position and name only for students whose gender is "F".

# # # # # # students = {"Ada": "F", "Bola": "F", "Chidi": "M", "Dami": "M"}
# # # # # # for position, (name, gender) in enumerate (students.items(), 1):
# # # # # #     if gender == "F":
# # # # # #         print(position,name )


# # # # # # Print the position and name only for students whose gender is "F".



# # # # # # Question 7

# # # # # # Input:

# # # # # # countries = {"NG": "Nigeria", "GH": "Ghana", "KE": "Kenya", "ZA": "South Africa"}


# # # # # # Print only the position and country name (ignore the country code).

# # # # # # countries = {"NG": "Nigeria", "GH": "Ghana", "KE": "Kenya", "ZA": "South Africa"}
# # # # # # for position, (country_code, country_name) in enumerate(countries.items(), 1):
# # # # # #     print(position, country_name) 

# # # # # # Question 8

# # # # # # Input:

# # # # # # results = {"Ada": 85, "Bola": 70, "Chidi": 90, "Dami": 60}


# # # # # # Print:

# # # # # # "PASS" if score ≥ 75

# # # # # # "FAIL" otherwise

# # # # # # Include the position, name, and result.

# # # # # results = {"Ada": 85, "Bola": 70, "Chidi": 90, "Dami": 60}
# # # # # for position, (name, score) in enumerate(results.items(),1):
# # # # #     if score >= 75:
# # # # #         print(position, name, "PASS")
# # # # #     else:
# # # # #         print(position, name, "FAIL")

# # # # # # Question 9

# # # # # # Input:

# # # # # # settings = {"theme": "dark", "language": "en", "timezone": "UTC"}


# # # # # # Print the position of the key "language".
# # # # # settings = {"theme": "dark", "language": "en", "timezone": "UTC"}
# # # # # for position, key in enumerate(settings, 1):
# # # # #     if key =="language".lower():
# # # # #         print(position, key)






# # # # # # Question 10
# # # # # # Using enumerate, print the position and order ID only for orders whose status is "paid".


# # # # # # Input:

# # # # # # orders = {
# # # # # #     "O1": {"amount": 5000, "status": "paid"},
# # # # # #     "O2": {"amount": 3000, "status": "pending"},
# # # # # #     "O3": {"amount": 7000, "status": "paid"}
# # # # # # }

# # # # # # for position, (order_ID, details) in enumerate(orders.items()):
# # # # # #     if details["status"] == "paid":
# # # # # #         print(position, order_ID) 







# # # # # # Question 1

# # # # # # Using enumerate, print the position and order ID for orders whose amount is greater than 4000.

# # # # # # Input

# # # # # # orders = {
# # # # # #     "O1": {"amount": 5000, "status": "paid"},
# # # # # #     "O2": {"amount": 3000, "status": "pending"},
# # # # # #     "O3": {"amount": 7000, "status": "paid"},
# # # # # #     "O4": {"amount": 2000, "status": "paid"}
# # # # # # }
# # # # # # for position, (orderID, details) in enumerate(orders.items(), 1):
# # # # # #     if details["amount"] > 4000:
# # # # # #         print(position, orderID)





# # # # # # Question 2

# # # # # # Using enumerate, print:

# # # # # # <position> <order_id> PAID


# # # # # # Only for orders where:

# # # # # # status is "paid"

# # # # # # amount is at least 6000

# # # # # # # Input
# # # # # # orders = {
# # # # # #     "A101": {"amount": 4500, "status": "paid"},
# # # # # #     "A102": {"amount": 6200, "status": "paid"},
# # # # # #     "A103": {"amount": 7000, "status": "pending"},
# # # # # #     "A104": {"amount": 8000, "status": "paid"}
# # # # # # }

# # # # # # for position, (order_id, details) in enumerate(orders.items(), 1):
# # # # # #     if details["status"] == "paid" and details["amount"]>=6000:
# # # # # #         print(position, order_id, "PAID" )


# # # # # # Question 1
# # # # # # numbers = [6, 14, 3, 20, 9]


# # # # # # Create a list that contains numbers greater than 10.

# # # # # numbers = [6, 14, 3, 20, 9]

# # # # # greater_than_10= [number for number in numbers if number  > 10]
# # # # # print(greater_than_10) 


# # # # # Question 2
# # # # # names = ["Ada", "Bola", "Sam", "Ife"]


# # # # # Create a list that shows, for each name, whether it starts with a vowel.

# # # # vowels = "a,e,i,o,u, A, E, I, O, U"

# # # # names = ["Ada", "Bola", "Sam", "Ife"]
# # # # vowels_check = [vowels in name for name in names]
# # # # print(vowels_check) 


# # # # Question 3
# # # # words = ["pen", "pencil", "eraser", "bag"]


# # # # Create a list containing only words longer than 3 characters.

# # # words = ["pen", "pencil", "eraser", "bag"]
# # # longer_than_3 = [word for word in words if len(word) > 3]
# # # print(longer_than_3)


# # Question 4
# # scores = [45, 60, 30, 90]


# # Create a list that shows, for each score, whether it is a passing score (50 and above

# scores = [45, 60, 30, 90]

# passing_score = [score >= 50 for score in scores]
# print(passing_score)



# Question 5
# items = ["Apple", "banana", "Avocado", "pear"]


# Create a list containing only items that start with the letter “a” (case-insensitive).

items = ["Apple", "banana", "Avocado", "pear"]

letter_with_a = [fruit for fruit in items if fruit.lower().startswith("a") ]
print(letter_with_a)









