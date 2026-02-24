# print(list("hello"))


# shopping_list = ["rice", "tomatoes", "on/ions", "groundnut oil", "curry", "maggi", "pepper", "salt", "thyme"]
# print(shopping_list)
# print(shopping_list[2])
# print(shopping_list[-1])

# shopping_list[3] = "butter"


# shopping_list.append("fish")


# shopping_list.insert(4, "chicken")
# shopping_list.insert(6, "chicken")
# shopping_list.insert(-1, "chicken")
# shopping_list.insert(8, "chicken")
# shopping_list.remove("onions")

# print("tomatoes" in shopping_list)
# print("garlic" in shopping_list)

# print(shopping_list)
# print(shopping_list[2:5])

# print(shopping_list.index("tomatoes"))

# shopping_list = ["rice", "tomatoes", "onions", "salt", "groundnut oil", "curry", "maggi", "pepper", "salt", "thyme"]
# print(shopping_list)


# shopping_list = ["rice", "tomatoes", "onions", "salt", "groundnut oil"]

# print(shopping_list)
# shopping_list.append("pepper")
# print(shopping_list)
# # list methods work in-place

# name = "David"

# number_of_ds = name.count("d")
# print(number_of_ds)
# print(name)


# songs = ["Iwo loba", "Osuba", "Beautiful things", "Not like us", "Holy words"]

# 1. print the 3rd song
# 2. Change the 4th song to uppercase
# 3. Check if "Osuba" is in `songs`
# 4. Add "Rainbow" to the end of the list
# 5. Add "Saved My Life" in between "Iwo loba" and "Osuba"
# 6. Remove "Iwo loba" from the list
# 7. Print a list of the first 3 songs in the list


# mobile_networks = ["Glo", "MTN", "Airtel", "9Mobile", "Smile"]

# print(mobile_networks)
# # mobile_networks[3] = "Etisalat"

# # mobile_networks[1:4] = ["Etisalat"]
# mobile_networks[3] = ["Etisalat"]

# print(mobile_networks)

# mobile_networks = ["Glo", "MTN", "Airtel", "9Mobile", "Smile"]

# print(len(mobile_networks))

# mixed = [5, True, "hello", None, 4.5, [1, 2, 3], ("red", "green", 1)]

# print(mixed)

# print(list("Hello"))

# colors = "red", "green", "blue"
# print(colors)

# print(list(colors))
# print(colors)


# colors = ["red", "green", "blue"]
# print(type(colors))

# "John".append("J")  # AttributeError

# colors = ["red", "green", "blue"]
# colors.append("purple", "brown")

# colors.insert(1, "red", "purple")



# colors = ["red", "green", "blue"]

# # colors.extend("hello")
# # colors.extend(("hello", "hey", "hi"))
# others = ["purple", "silver", "burgundy"]
# colors.extend(others)

# print(colors)

# colors = ["red", "green", "blue"]
# others = ["purple", "silver", "burgundy"]
# all_colors = colors + others
# print(all_colors)

# --------------------------REMOVING FROM A LIST------------------------------


# 1. .remove()
# fast_cars = ["Buggati", "Lamborghini", "BMW", "Ferrari", "Brabus", "Doge"]

# print(fast_cars)
# fast_cars.remove("Lamborghini")

# print(fast_cars)


# 2. del keyword
# fast_cars = ["Buggati", "Lamborghini", "BMW", "Ferrari", "Brabus", "Doge"]
# print(fast_cars)

# # del fast_cars[100]  # IndexError
# del fast_cars[1]
# print(fast_cars)

# del fast_cars

# print(fast_cars)


# 3. .pop()

# fast_cars = ["Buggati", "Lamborghini", "BMW", "Ferrari", "Brabus", "Doge"]

# print(fast_cars)
# # fast_cars.pop(1)
# # fast_cars.pop()
# lambo = fast_cars.pop(1)
# print(lambo)
# print(fast_cars)


# fast_cars = ["Buggati", "Lamborghini", "BMW", "Ferrari", "Brabus", "Doge"]
# # fast_cars.clear()

# # del fast_cars[::]

# fast_cars = []

# print(fast_cars)

# ------------------------------------SORTING A LIST---------------------------------
# lexicographical order 
# fast_cars = ["Buggati", "Lamborghini", "bMW", "Ferrari", "Brabus", "doge"]

# fast_cars.sort()
# fast_cars.sort(key=str.lower)
# fast_cars.sort(key=str.lower, reverse=True)
# fast_cars.sort(reverse=True)

# print(fast_cars)



# ------------------------------------SORTING A LIST---------------------------------


# ------------------------------------REVERSING A LIST---------------------------------
# fast_cars = ["Buggati", "Lamborghini", "bMW", "Ferrari", "Brabus", "doge"]
# # fast_cars.reverse()

# fast_cars = fast_cars[::-1]

# print(fast_cars)


# ------------------------------------REVERSING A LIST---------------------------------



# ------------------------------------COPYING A LIST---------------------------------
# fast_cars = ["Buggati", "Lamborghini", "bMW", "Ferrari", "Brabus", "doge"]

# fast_cars_copy = fast_cars  # reference, not a copy
# print(fast_cars)
# print(fast_cars_copy)

# fast_cars_copy.append("Mercedes")

# print("fast_cars:     ", fast_cars)
# print("fast_cars_copy:", fast_cars_copy)


# fast_cars = ["Buggati", "Lamborghini", "bMW", "Ferrari", "Brabus", "doge"]

# fast_cars_copy = fast_cars.copy()  # true shallow copy
# print(fast_cars)
# print(fast_cars_copy)

# fast_cars_copy.append("Mercedes")

# print("fast_cars:     ", fast_cars)
# print("fast_cars_copy:", fast_cars_copy)

# import copy

# fast_cars = [["Buggati", "Lamborghini"], ["bMW", "Ferrari"], ["Brabus", "doge"]]

# fast_cars_copy = copy.deepcopy(fast_cars)  # true shallow copy
# print(fast_cars)
# print(fast_cars_copy)

# fast_cars_copy[1].append("Mercedes")

# print("fast_cars:     ", fast_cars)
# print("fast_cars_copy:", fast_cars_copy)


# ------------------------------------COPYING A LIST---------------------------------


# ------------------------------------NESTED LISTS---------------------------------


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(matrix[1][1])
# print(matrix[2][2])

# print(matrix[-3][-3])

# matrix[2][1] = 100

# print(matrix)

# matrix[1][1] = matrix[1][0] + matrix[1][2]
# print(matrix)


# nested_list = [
#     ["Alice", "Bob"],
#     [10, 20, 30],
#     [True, False]
# ]

# print(nested_list[0][0][1:])
# print(nested_list[0][1][1])

# nested_list[2][0] = not nested_list[2][0]

# print(nested_list)
# nested_list[2][1] = not nested_list[2][1]

# print(nested_list)

# nested_list[1].reverse()

# print(nested_list)

# ------------------------------------NESTED LISTS---------------------------------







song = ["Iwo loba", "Osuba", "Beautiful things", "Not like us", "Holy words"]
# print the 3rd song
print(song[2])

# change the 4th song to uppercase
# print((song[3].upper)

# Check if "Osuba" is in song
print("Osuba" in song)

# Add "Rainbow"  to the end of the list
song.append("Rainbow")
print(song)

# Add "Saved my Life" in between
song.insert(1, "Saved my Life")
print(song)

song.remove("Iwo loba")
print(song)

print(song[:3])


      

