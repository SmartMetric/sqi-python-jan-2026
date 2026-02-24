# 🟢 BASIC (4 Questions)

# 👉 One clear inner condition, no tricks.

# Q1
# teams = [
#     ["Ada", "Bola"],
#     ["Sam", "Tim"],
#     ["Ife", "Ola"]
# ]
# ✅ Check if any team has all members’ names longer than 2 characters.

# name_longer_2 = any(all(len(name) > 2 for name in team)for team in teams)
# print(name_longer_2)

# Q2
# scores = [
#     [60, 70, 80],
#     [40, 50, 55],
#     [90, 95, 100]
# ]


# ✅ Check if any group has all scores greater than 50.

# scores_greater_50 = any(all( group > 50 for group in scores ) for score in scores)


# Q3
# numbers = [
#     [2, 4, 6],
#     [1, 3, 5],
#     [8, 10, 12]
# ]


# ✅ Check if any list contains all even numbers.

# any(all(number % 2 == 0 for number in list) for list in numbers)



# for number in numbers


# Q4
# words = [
#     ["cat", "dog"],
#     ["apple", "banana"],
#     ["pen", "ink"]
# ]


# ✅ Check if any group has all words longer than 3 characters.


# longer_than3 = any(all(len(letter) > 3 for letter in word) for word in words)


# 🟡 MEDIUM (3 Questions)

# 👉 Requires combining length, comparison, or membership logic.

# Q5
# classes = [
#     [45, 55, 65],
#     [70, 80, 90],
#     [30, 40, 50]
# ]


# #✅ Check if any class has all scores ≥ 60.
# score_greater_60 = any(all(score >= 60 for score in class) for class in classes)

# ()



# Q6
# sentences = [
#     ["I", "love", "Python"],
#     ["Code", "is", "fun"],
#     ["Generators", "are", "awesome"]
# ]


# ✅ Check if any sentence has all words longer than 2 characters.

# char_greater_2 = any(all(len(word) < 2 in word for words in sentences) for word in sentences)


# Q7
# rows = [
#     [3, 6, 9],
#     [2, 4, 6],
#     [5, 10, 15]
# ]


# ✅ Check if any row has all numbers divisible by 3.

# divisible_by3= any(all(number % 3 ==0 for number in row) for row in rows)

# row in rows

# 🔴 ADVANCED (3 Questions)

# 👉 Multiple logic layers, reasoning required.

# Q8
# departments = {
#     "HR": ["Ada", "Ife"],
#     "Tech": ["Sam", "Bola", "Tim"],
#     "Sales": ["Ola", "Uche"]
# }


# ✅ Check if any department has all names longer than 3 characters.


# longer_than3 = any(all(len(name) > 3 for name in department) for department in departments)
# Q9
# data = [
#     [10, 20, 30],
#     [15, 25, 35],
#     [40, 50, 60]
# ]


# ✅ Check if any group has all numbers divisible by both 5 and 10.

# Q10
# records = [
#     ["A", "B", "C"],
#     ["AA", "BB", "CC"],
#     ["AAA", "BBB"]
# ]
# ✅ Check if any record has all strings of equal length and length ≥ 2.

# length_greater_2 = any(all(len(letter) >= 2 for letter in record ) for record in records)



# 🧠 ONE UNCHANGING PATTERN (Burn this in)

# All 10 questions reduce to:

# any(
#     all(CONDITION for item in inner)
#     for inner in outer
# )