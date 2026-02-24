# # # # 1. Create a function called turn_to_upper(names) that takes in a list of names, and returns a list of names uppercased
# # # # after, print the result of the function.
# # # # For example, if names is ["Winifred", "Wilfred", "Justin", "Augusta"], the result would be [ "WINIFRED", "WILFRED", "JUSTIN", "AUGUSTA"]

# def turn_to_upper(names):
#     uppercased_name= [name.upper() for name in names]
#     return uppercased_name

# print(turn_to_upper(["Winifred", "Wilfred", "Justin", "Augusta"]))


# # # # 2. Create a function called get_middle_name that accepts one paramter `name_dict` that takes in a dictionary with keys "first", "middle", and "last".
# # # # The function should return only the middle name.
# # # # For example, if name_dict is {"first": "Tola", "middle": "James", "last": "Akin"}, then the result would be "James". 
# # # # Another example is if name_dict is {"middle": "Chioma", "first": "Ada", "last": "Okeke"}, the result would be "Chioma".
# def name_dict(full_name: dict[str, str]):
#      return {middle_name for middle_name in full_name}
# print(name_dict({"first": "Tola", "middle": "James", "last": "Akin"}))
# print(name_dict({"middle": "Chioma", "first": "Ada", "last": "Okeke"}))

# # # # 3. Create a function called reverse_string that accepts a string as input and returns the string reversed.
# # # # For example, if the string is "Python", the result would be "nohtyP".
# def reverse_string(word):
#      return (word[::-1])
# print(reverse_string("python"))





# # # # 4. Create a function called count_vowels that accepts a string and returns the number of vowels (a, e, i, o, u) in it.
# # # # For example, if the string is "beautiful", the result would be 5.
# def count_vowels(words):
#     vowels = ("a, e, i, o, u")
# # #     return sum(char in vowels for char in words)
# # # print (count_vowels("beautiful"))

# # # # 5. Create a function called even_numbers that takes in a list of integers and returns a new list containing only the even numbers.
# # # # For example, if the list is [1, 2, 3, 4, 5, 6], the result would be [2, 4, 6].

# # # def even_numbers(numbers):
# # #     return [number for number in numbers if number % 2 == 0]

# # # print(even_numbers([1, 2, 3, 4, 5, 6]))


# # # # 6. Create a function called find_max that takes in a list of numbers and returns the maximum number in the list.
# # # # For example, if the list is [12, 45, 3, 67, 23], the result would be 67.

# # # def find_max(numbers):
# # #     return max(numbers) 
# # # print(find_max([12, 45, 3, 67, 23]))

# # # # 7. Create a function called sum_dict_values that takes in a dictionary with numeric values and returns the sum of all the values.
# # # # For example, if the dictionary is {"a": 10, "b": 20, "c": 5}, the result would be 35.
# # # def sum_dict(dictionary: dict[str, int]):
# # #     return sum(dictionary.values())
# # # print(sum_dict({"a": 10, "b": 20, "c": 5}))

# # # # 8. Create a function called word_lengths that takes in a list of words and returns a dictionary where each word is a key and its length is the value.
# # # # For example, if the list is ["apple", "banana", "cherry"], the result would be {"apple": 5, "banana": 6, "cherry": 6}.
# # # def word_lengths(fruits: list[str]):
# # #     return len(fruits)
# # # print(word_lengths(["apple", "banana", "cherry"]))


# # # # 9. Create a function called is_palindrome that takes in a string and returns True if the string is a palindrome (same forwards and backwards), otherwise False.
# # # # For example, if the string is "level", the result would be True. If the string is "hello", the result would be False.
# # # def is_palindrome(text):
# # #     return text[::-1] == text
# # # print(is_palindrome("hello"))




# # # # 10. Create a function called merge_lists that takes in two lists and returns one combined list without duplicates.
# # # # For example, if list1 = [1, 2, 3] and list2 = [3, 4, 5], the result would be [1, 2, 3, 4, 5].
# # # def merge_lists(list):
# # #     list1 = [1, 2, 3] 
# # #     list2 = [3, 4, 5] 
# # #     list1 = set(list1)
# # #     list2 = set(list2)
# # #     return list1 + list2
# # # print(merge_lists([1, 2, 3] , [3, 4, 5]))

    
# # # 11. Create a function called multiply_numbers(a, b=2) that multiplies two numbers.
# # # If the second number is not provided, it should default to 2.
# # # Example 1: multiply_numbers(5) → 10
# # # Example 2: multiply_numbers(5, 3) → 15

# # def multiply_numbers(a, b):
# #     b=2
# #     return a * b
# # print(multiply_numbers(5, b))



# #.............................................................................................
# # Write a function sum_numbers(a, b) that returns the sum of two numbers.
# def sum_numbers(a, b):
#     return a+b
# print(5,3)

# # Write a function is_even(n) that returns True if n is even and False if n is odd.
# def is_even(n):
#    return n % 2==0
# print(is_even(5))
    
# # Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
# def is_prime(n):
    
#     prime = n % 2 != 0 and n > 2



# # Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.
# # Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.
# # Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# # is_alliteration(‘Levelheaded llama’) —> True
# # is_alliteration(‘Crazy Kangaroo’) –> False
# # Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# # old_macdonald(‘macdonald’) —> MacDonald
# # Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.
# # Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# # spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# # spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# # spy_game([1, 7, 2, 0, 4, 5, 0]) —> False
# # Write a function vol(radius) that computes the volume of a sphere given its radius.
# # Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
# # Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.
# # Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.


# def get_total_length(*fruits):
#     return sum(len(word) for word in fruits)
# print(get_total_length("apple", "banana", "car"))

# def highest_score(**scores):
#     return max (score for score in scores)

# print(highest_score())


def multiply(list_items):

    return a * b * c * d

print(multiply([1,2,3,-4]))
