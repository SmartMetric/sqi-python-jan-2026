# # # foods= {"Yam", "Egg", "Afanag", "amala","Abula", "Rice", "avocado", "Almond"}

# # # start_with_a = {food for food in foods if "a"==[0] in foods }
# # # print(start_with_a)



# # # 5. Are all the numbers greater than 10?
# # # # Input: [5, 12, 3, 18, 7]
# # # # Expected Output: False

# # values = [5, 12, 3, 18, 7]

# # above_ten = all(value > 10 for value in values)
# # print(above_ten)



# # # # 6. Is there any name that contains the letter 'a'?
# # # # Input: ["John", "Sara", "Mike", "Amanda"]
# # # # Expected Output: True
# # # names = ["John", "Sara", "Mike", "Amanda"]


# # names = ["John", "Sara", "Mike", "Amanda"]

# # names_with_a = any("a" in name.lower) for name in names)
# # print(names_with_a)

# # 7. Are all the words made up of only uppercase letters?
# # # Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# # # Expected Output: False

# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

# upper_check = all(word for word in greetings if word.upper)
# print(upper_check)

# 13. Are all temperatures above 0°C?
# # Input: [12, 7, 3, -1, 5]
# # Expected Output: False

temperatures = [12, 7, 3, -1, 5]

temp_check = all(temp > 0 for temp in temperatures)
print(temp_check)





