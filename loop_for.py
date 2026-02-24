# my_list = ["James", "Janet", "Jack", "Jill"]

# for name in my_list:
#     print(name)


# wild_animals = ["snake", "lion", "dog", "goat", "hen"]

# for animal in wild_animals:
#     print(animal)

# wild_animals = ["snake", "lion", "dog", "goat", "hen"]

# for wild_animal in wild_animals:
#     print(wild_animals)

# ['snake', 'lion', 'dog', 'goat', 'hen']
# ['snake', 'lion', 'dog', 'goat', 'hen']
# ['snake', 'lion', 'dog', 'goat', 'hen']
# ['snake', 'lion', 'dog', 'goat', 'hen']
# ['snake', 'lion', 'dog', 'goat', 'hen']


# wild_animals = ["snake", "lion", "dog", "goat", "hen"]

# for evydnjefnnf in wild_animals:
#     print(evydnjefnnf)

# import string

# name = "Winnie!"

# vowels = "AEIOUaeiou"

# alphabets = string.ascii_letters

# for char in name:
#     if char not in vowels and char in alphabets:
#         print(char)


# print(list(range(2, 9)))


# for number in range(2, 9):
#     print(number)


# for wild_animal in ["snake", "lion", "dog", "goat", "hen"]:
#     print(wild_animal)


# for num in [1, 2, 3]:
#     print(num)

# capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Australia': 'Canberra', 'Egypt': 'Cairo'}

# capitals = list(capitals.items())

# print(capitals)

# i = 0

# while i < len(capitals):
#     country, capital = capitals[i]
#     print(f"The capital of {country} is {capital}")
#     i += 1


# capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Australia': 'Canberra', 'Egypt': 'Cairo'}


# for country, capital in capitals.items():
#     print(f"The capital of {country} is {capital}")


# for animal in {'snake', 'lion', 'dog', 'goat', 'hen'}:
#     print(animal)

# actions = ["wake up", "walk", "skip", "run", "talk", "stop", "land"]

# 1. Loop through the actions, but skip "skip"

# Output:

# "wake up"
# "walk"
# "run"
# "talk"
# "stop"
# "land"


# for action in actions:
#     if action == "skip":
#         continue
#     print(action)

# 2. Stop right before stop

# Output:

# "wake up"
# "walk"
# "skip"
# "run"
# "talk"

# for action in actions:
#     if action == "stop":
#         break
#     print(action)



# print(list(range(3, 100, 5)))

# print(list(range(10, -1, -1)))
# for i in range(10, -1, -2):
#     print(i)


# print(list(range(8)))

# means_of_transportation = ["airplane", "jet", "train", "car", "camel", "broom"]

# for i in range(len(means_of_transportation)):
#     means_of_transport = means_of_transportation[i]
#     print(f"The element at index {i} is {means_of_transport}")

# The element at index 0 is airplane
# The element at index 1 is jet
# The element at index 2 is train


# means_of_transportation = ["airplane", "jet", "train", "car", "camel", "broom"]

# for i in range(len(means_of_transportation)):
#     means_of_transport = means_of_transportation[i]
#     print(f"{i+1}. {means_of_transport}")


# means_of_transportation = ["airplane", "jet", "train", "car", "camel", "broom"]

# print(list(enumerate(means_of_transportation)))


# for (index, means_of_transport )in enumerate(means_of_transportation, start=1):
#     print(index)
#     print(means_of_transport)


# means_of_transportation = ["airplane", "jet", "train", "car", "camel", "broom"]

# for i in range(len(means_of_transportation)):
#     means_of_transport = means_of_transportation[i]
#     print(f"{i+1}. {means_of_transport}")


# 1. airplane
# 2. jet
# 3. train
# 4. car
# 5. camel
# 6. broom


# ingredients = {"maggi", "pepper", "ginger", "salt", "tumeric", "curry", "cinnamon"}
# ingredients = {}

# for ingredient in ingredients:
#     print(ingredient)
# else:
#     print("Loop has ended")



# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# for adj in adjectives:
#     for animal in animals:
#         print(adj, animal)


# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]


# print(list(zip(adjectives, animals)))
# for adj, animal in zip(adjectives, animals):
#     print(f"{adj} {animal}")

# adjectives = ["fierce", "majestic", "playful", "happy", "sad"]
# animals = ["lion", "eagle", "dolphin"]

# for adj, animal in zip(adjectives, animals):
#     print(f"{adj} {animal}")


# adjectives = ["fierce", "majestic", "playful", "happy", "sad"]
# animals = ["lion", "eagle", "dolphin"]


# shortest = min(adjectives, animals, key=len)

# for i in range(len(shortest)):
#     adj = adjectives[i]
#     animal = animals[i]
#     print(f"{adj} {animal}")



# name = "Felix"

# if name == "James":
#     pass


# print("End of file")



# name = "Felix"

# for char in name:
#     pass



# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60


# 11. Collect a phrase from the user and use a loop to generate an acronym by taking the first
# letter of each word. Print the acronym. Example:
# Input: "Portable Network Graphics"
# Output: "PNG"

