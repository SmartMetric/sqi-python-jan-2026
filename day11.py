states = {"Ondo":"Akure", "Kwara":"Ilorin", "Imo":"Owerri", "Osun":"Osogbo",  "Anambra":"Awka"}
states["Lagos"] = "Ikeja"
print(states)

#                           Ordered             Indexed             Mutable         Allow Duplicates
# Lists                       Yes                 Yes                 Yes               Yes
# Tuples                      Yes                 Yes                 No                Yes
# Dictionaries           Yes, from Py 3.7+     Yes, but with keys     Yes         Duplicate keys not allowed, duplicate values allowed


# numbers = (10, 20, 30)
# numbers[1] = 200


# numbers = ([10, 20], [30, 40], [50, 60])
# numbers[1][0] = 300

# print(numbers)

# numbers[1] = [300, 400]

# empty_dict = {}

# phone_book = {"Winnie": "09030556547", "Francis": "07080434796", "Pelumi": "07077172351", "Adil": "09134668655", "Olumide": "07063387933", 0: "zero", "winnie": "08032239275", "David": "09134668655"}

# print("Winnie" in phone_book)
# print("09030556547" in phone_book)

# print(phone_book)

# print(phone_book["Winnie"])
# print(phone_book[0])

# # FAANG - Facebook, Amazon, Apple, Netflix, Google

# phone_book["Pelumi"] = "08159170485"

# print(phone_book)

# phone_book["John"] = "08066066454"

# print(phone_book)

# del phone_book["Adil"]

# print(phone_book)



# Ondo - Akure
# Kwara - Ilorin
# Imo - Owerri
# Osun - Osogbo
# Anambra - Awka

# 1. Create a dictionary `states_and_capitals` mapping the states to their capitals
# 2. Add a new state `Lagos` and map to its capital `Ikeja`
# 3. Change the capital of "Osun" to upper case without directly using `OSOGBO`
# 4. Remove "Ondo" from the dictionary

# states_and_capitals = {"Ondo": "Akure", "Kwara": "ilorin", "Imo": "Owerri", "Osun": "Osogbo", "Anambra": "Awka"}

# states_and_capitals["Lagos"] = "Ikeja"

# print(states_and_capitals)

# states_and_capitals["Osun"] = states_and_capitals["Osun"].upper()
# print(states_and_capitals)

# del states_and_capitals["Ondo"]
# print(states_and_capitals)


# states_and_capitals = {"Ondo": "Akure", "Kwara": "ilorin", "Imo": "Owerri", "Osun": "Osogbo", "Anambra": "Awka"}

# print(states_and_capitals.keys())  # dict_keys data type
# print(list(states_and_capitals.keys()))  # dict_keys data type

# print(states_and_capitals.values())

# print("Owerri" in states_and_capitals.values())

# print(states_and_capitals.items())


# ------------------------------------------ACCESSING DICT VALUES------------------------------------------

my_dream_car = {
    "brand": "Lamborghini",
    "model": "SVJ",
    "manufacture_year": 2024,
    # "is_electric": False
}

# print(my_dream_car["model"])  # bracket notation

# print(my_dream_car.get("model"))

# # print(my_dream_car["color"])  # KeyError

# print(my_dream_car.get("color"))

# print(my_dream_car.get("color", "N/A"))

# print(my_dream_car.get("is_electric", True))


# print(my_dream_car.setdefault("color"))

# print(my_dream_car)

# print(my_dream_car.setdefault("color", "blue"))

# print(my_dream_car)

# print(my_dream_car.setdefault("model", "Urus"))

# print(my_dream_car)

# ------------------------------------------ACCESSING DICT VALUES------------------------------------------



# ------------------------------------------UPDATING A DICT------------------------------------------

# my_dream_house = {
#     "type of house": "mansion",
#     "no_of_rooms": 20,
#     "has_garage": True,
#     "has_minibar": True,
#     "football_pitch_size_in_sq_metres": 55.5
# }


# my_dream_house["type"] = "castle"  # bracket notation

# print(my_dream_house)

# my_dream_house.update(type_of_house="castle", has_garage=False, has_pool=False)
# my_dream_house.update({"type of house": "castle", "has_garage": False, "has_pool": False})

# print(my_dream_house)

# ------------------------------------------UPDATING A DICT------------------------------------------


# ------------------------------------------REMOVING FROM A DICT------------------------------------------

# my_favorite_anime = {
#     "name": "Bleach",
#     "main_character": "Kurosaki Ichido",
#     "year_released": 2002,
#     "director": "Isayami"
# }

# del my_favorite_anime["year_released"]

# year = my_favorite_anime.pop("year_released")

# print(year)

# popped_item = my_favorite_anime.popitem()
# print(popped_item)

# key, value = my_favorite_anime.popitem()
# print(key)
# print(value)

# print(my_favorite_anime)

# my_favorite_anime = {
#     "name": "Bleach",
#     "main_character": "Kurosaki Ichido",
#     "year_released": 2002,
#     "director": "Isayami"
# }


# popped_item = my_favorite_anime.popitem()
# print(popped_item)


# popped_item = my_favorite_anime.pop("no_of_seasons")
# print(popped_item)

# ------------------------------------------REMOVING FROM A DICT------------------------------------------

# my_favorite_book = {
#     "title": "How Europe underdeveloped Africa",
#     "genre": "non-fiction",
#     "author": "Walter Rodney",
#     "no_of_pages": 312
# }

# print(len(my_favorite_book))

# print(type(my_favorite_book))


# my_favorite_book = dict(title_of_book="How Europe underdeveloped Africa", genre="non-fiction", author="Walter Rodney", no_of_pages=312)

# print(my_favorite_book)

# numbers = ["ten", "twenty", "thirty"]

# print(dict(numbers))

# numbers = [("ten", 10), ("twenty", 20), ("thirty", 30)]
# numbers = (("ten", 10), ("twenty", 20), ("thirty", 30))
# numbers = [["ten", 10], ["twenty", 20], ["thirty", 30]]
# numbers = (["ten", 10], ["twenty", 20], ["thirty", 30])

# print(dict(numbers))


# ------------------------------------------CLEARING A DICT------------------------------------------

# my_dict = {'ten': 10, 'twenty': 20, 'thirty': 30}

# my_dict.clear()

# print(my_dict)

# my_dict = {}

# print(my_dict)


# ------------------------------------------CLEARING A DICT------------------------------------------


# ------------------------------------------COPYING A DICT------------------------------------------

# import copy

# my_dict = {'ten': 10, 'twenty': 20, 'thirty': 30, 'numbers': [0, 4, 28, 23]}
# my_dict_copy = my_dict.copy()
# my_dict_copy = copy.copy(my_dict)  # shallow
# my_dict_copy = copy.deepcopy(my_dict)  # deep
# print(my_dict is my_dict_copy)


# ------------------------------------------COPYING A DICT------------------------------------------


