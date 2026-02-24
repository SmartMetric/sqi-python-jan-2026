# # # # # Write a program that takes an integer input from the user and uses a loop to calculate 
# # # # # the sum of its digits. Print the sum. Example:
# # # # # Input: 1234
# # # # # # Output: 10 (1+2+3+4)
# # # # # number = input("enter a number:   ")
# # # # # sum = 0
# # # # # for numbers in number:
# # # # #     sum +=int(numbers)
# # # # # print(sum )

# # # # # Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# # # # # Input: "hello world"
# # # # # Output: Vowels: 3, Consonants: 7

    
# # # # # Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# # # # # Input: 5
# # # # # Output:
# # # # # 5 x 1 = 5
# # # # # 5 x 2 = 10
# # # # # 5 x 3 = 15
# # # # # ...
# # # # # 5 x 12 = 60

# # # number = int(input("Enter a number:   "))
# # # for i in range(1, 13):
# # #     print(number * i)


# # # # # Collect a string from the user and use a loop to reverse the string. Print the reversed string. 
# # # # # Do not reverse the string using [::-1] or reversed().
# # # # # Example:
# # # # # Input: "python"
# # # # # Output: "nohtyp"


# # # # word =(input("Enter a word:   "))
# # # # reversed_text = ""
# # # # for char in word:
# # # #     reversed_text = char + reversed_text
# # # # print(reversed_text)


# # # # # Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. 
# # # Print the new list. Do not use the set() constructor. Use a loop. Example:
# # # # # Input: "1, 2, 3, 2, 4, 3"
# # # # # Output: [1, 2, 3, 4]


# # # # Write a program that takes an integer input n from the user and prints the first 
# # # # 	n numbers in the Fibonacci sequence. Example:
# # # # 	Input: 10
# # # # 	Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# # # ???# #  7. 	Collect a list of numbers from the user (entered as comma-separated values) and use a 
# # # # 	loop to find and print the largest number in the list. Don’t use the built-in max 
# # # # 	function or anything similar.
# # # # 	Input: "10, 20, 5, 15"
# # # # 	Output: 20



# # # #  8. 	Write a program that takes an integer n from the user and calculates the sum of all 
# # # # 	even numbers from 1 to n. Print the sum.
# # # # 	Input: 10
# # # # 	Output: 30 (2 + 4 + 6 + 8 + 10)

# # # n = int(input("Enter number  "))
# # # sum = 0
# # # for number in range (1, n+1):
# # #     if number % 2 == 0:
# # #         sum +=number
# # # print(sum)



# # # #  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# # # # 	in the string. Print each character along with its frequency. Example:
# # # # 	Input: "hello"
# # # # 	Output:
# # # # h: 1
# # # # e: 1
# # # # l: 2
# # # # o: 1


# # # Write a program that takes an integer n from the user and calculates the sum of 
# # # 	squares of all numbers from 1 to n. Print the sum. Example:
# # # 	Input: 3
# # # 	Output: 14 (1^2 + 2^2 + 3^2)

# # # n = int(input("enter a number  "))
# # # sum_of_squares = 0
# # # for numbers in range (1, n +1 ):
# # #     square = numbers**2
# # #     sum_of_squares += square
  
# # # print(sum_of_squares)




# # #  11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# # # 	letter of each word. Print the acronym. Example:
# # # 	Input: "Portable Network Graphics"
# # # 	Output: "PNG"
# # #  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# # # 	Print the count. Example:
# # # 	Input: "Hello world from Python"
# # # 	Output: 4

# # #  13. 	Collect a string from the user and only print out the words that start with the letter 
# # # 	‘S’. Example:
# # # 	Input: “Print only the words that start with s in this Sentence”
# # # 	Output: 
# # # 	start
# # # 	s
# # # 	Sentence

# # #  14. 	Print all the even numbers from 1 to 20 using the range function and a loop.


# # # for numbers in range(1,21):
# # #     if numbers % 2 == 0:
# # #         print(numbers)

# # #  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# # # 	by 3.
# # divisible_by_3 = []
# # for numbers in range(1,51):
# #     if numbers % 3 == 0:
# #         divisible_by_3.append(numbers)
# # print(divisible_by_3)


# #  16.	Go through the string below and if the length of a word is even, print that word.
# # 	st = ‘Print every word in this sentence that has an even number of letters’
# # 	Output: 
# # 	word
# # 	in
# # 	this
# # 	sentence
# # 	that
# # 	an
# # 	even
# # 	number
# # 	of

# word = input("enter a word")
# if char in word:



# #  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# # 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# # 	are multiples of both three and five, print “FizzBuzz”.
# #  18.	You are given two lists, names and grades. Print them together
# # names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# # grades = ['A', 'E', 'F', 'C', 'B']

# # Expected Output:
# # Ken got grade A
# # Mia got grade E
# # Rose got grade F
# # Henry got grade C
# # Suzan got grade B


# colors = ["red", "green", "purple", "brown", "silver"]

# vowels = "AeiouAEIOU"
# brands= ["Gucci", "Aquafina", "Samsung", "Apple", "Dolce&Gabana", "Nike", "New Balance", "Adidas"]
# start_with_vowel= [vowels for brand in brands]
# print(True)

# numbers = [9,12,9,7,1,3]

# squares = [number**2 for number in numbers]
# print(squares)


# numbers = [9,3,8,10,25,7,53]
# value= [number for number in numbers if number  %2 != 0   ]
# print(value)

# brands= ["Gucci", "Aquafina", "Samsung", "Apple", "Dolce&Gabana", "Nike", "New Balance", "Adidas"]
# brand_selection = [brand for brand in brands if len(brand) <= 5]
# print(brand_selection)

countries = ["Nigeria", "USA", "Ghana", "Russia", "Singapore", "Kenya", "Brazil", "Togo"]
developing_countries = ["Nigeria", "Ghana","Kenya", "Togo"]
developed_countries = [country for country in countries if country not in developing_countries]
print(developed_countries)


def talk():
    print("I am talking")
talk()


def to_upper(name):

    print(name.upper())
to_upper("Babajide")


def raise_to_power(base, exponent):
    print((base ** exponent))
raise_to_power(5,3)
    
    