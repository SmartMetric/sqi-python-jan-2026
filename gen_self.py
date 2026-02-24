# # # Practice 1
# # # numbers = [3, 9, 12, 15]
# # # Create a generator that produces numbers greater than 10.

# # numbers = [3, 9, 12, 15]
# # gen = (number > 10 for number in numbers)
# # for num in gen:
# #     print(num)

# # Practice 2
# # names = ["Ada", "Bola", "Sam"]


# # Create a generator that produces True or False depending on whether each name contains "a" (case-insensitive).

# names = ["Ada", "Bola", "Sam"]
# gen = ("a" in name.lower() for name in names)
# for a in gen:
#     print(a)

# Practice 1
# scores = [55, 70, 90, 40]


# Check if all scores are at least 50.
# scores = [55, 70, 90, 40]
# score_check = all(score >= 50 for score in scores)
# print( score_check)

# Practice 3
# ages = [12, 15, 18, 14]


# Check if all ages are 18 or above.

# ages = [12, 15, 18, 14]
# age_check = all(age >= 18 for age in ages)
# print(age_check)


# Practice Question 1
# animals = ["cat", "dog", "elephant", "ant"]


# Check if every animal name contains at least one vowel.

# animals = ["cat", "dog", "elephant", "ant"]
# vowels = "aeiou"

# atleast_onev = all(any(letter in vowels for letter in animal)for animal in animals)
# print(atleast_onev)

# Practice Question 2
# Check if any team has all its members’ names longer than 2 characters.

# teams = [
#     ["Ada", "Bola", "Chi"],
#     ["Sam", "Tim"],
#     ["Ife", "Ola"]
# ]

# more_than_two = any(all(len(name)>2 for name in team) for team in teams)
# print(more_than_two)






# Practice Question 3
# 

# Check if every product has at least one component that contains the letter “e”.

products = {
    "Laptop": ["keyboard", "screen", "battery"],
    "Phone": ["screen", "battery"],
    "Tablet": ["screen", "pen"]
}


















 























animals = ["tiger", "lynx", "elephant", "rhythm"]
vowels = "aeiou"

result = all(
    any(letter in vowels for letter in animal.lower())
    for animal in animals
)

print(result)
