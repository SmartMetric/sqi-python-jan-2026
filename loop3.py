# Print numbers from 1 to 5
# Expected Output:
# 1
# 2
# 3
# 4
# 5

# i = 1
# while i <= 5:
#     print(i)
#     i+=1











# Print "Hello" 3 times
# Expected Output:
# Hello
# Hello
# Hello

# i = 0
# while i < 3:
#     print("Hello")
#     i+=1





# Print only even numbers from 2 to 10 (do not use += 2)
# Expected Output:
# 2
# 4
# 6
# 8
# 10

# i= 1
# while i < 10:
#     if i % 2 == 0:
#         print(i)
#         i+=1

# Print numbers in reverse from 5 to 1 using a while loop.
# Expected Output:
# 5
# 4
# 3
# 2
# 1

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

#  5.	Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10

# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1

#  


# Output:
# ***
# ***
# ***

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****


#  7.	Print a right triangle of stars
# Ask the user to enter a number
# Example:
# Input: 4

# Output:
# *
# **
# ***
# ****

# stars = int(input("enter your number of stars"))

# i= 1

# while i <= 4:

#     print("*")
#     i += 1

#  8. 	Print a countdown
# Ask the user to enter a number where they want to start the countdown from.
# Example:
# Input: 5

# Output:
# 5
# 4
# 3
# 2
# 1
# Go!

# countdown = int(input("Enter a number:  "))
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# else:
#     print("Go !")


#  9. 	Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111

# value = []
# i = 1

# while i <= 10:
#     value.append(str(i))
#     print (",".join( value))
    # i +=1


# 10.  Print a list of the first 12 multiples of 3 starting from 3

# 12 multiple of 3 is 36 (3*12)

# i = 0
# while i <= 36:
#     if i % 12 == 0:
#         i+=1
#         print(i)
#         i+=1


# Write a program that uses a while loop to print numbers from 1 to 10.

# i = 0
# while i <= 10:
#     print(i)
#     i +=1



# Write a program that takes an integer n from the user and calculates the sum of all 
# # natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).
# n = int(input("Enter a number:   "))
# i = 0
# while n < 0:
#     print(n)
#     i+=1

# Write a program that uses a while loop to print numbers from 1 to 10.

# i = 0
# while i < 10:
#     print(i)
#     i += 1

# Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).



# Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. 
# E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, 
# their guess is too low.






# Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.

# Write a program that takes an integer input from the user and uses a while loop to print a 
# countdown from that number to zero.



# Write a program that takes an integer n from the user and uses a 
# while loop to print all even numbers from 1 to n.

# n = int(input("enter a number:  "))

# i = 1
# while i < n:
#     if n %2==0:
#         print(i)
#     i+=1






# Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625

base = int(input("Enter the base:  "))
exponent = int(input("Enter the base:  "))
result = 1

i = 1
while i < result:
    result = result * base
    print(i)
    



# Write a program that takes a string input from the user and uses a while loop to count the number of 
# vowels (a, e, i, o, u) in the string.
# Write a program that takes a string input from the user and uses a while loop to reverse the string.
# Do not use slicing or reversed().





#  10.	Write a program that takes comma-separated integers from the user, converts that
# 	to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
#       Use the min() function.
#  11. 	Write a program that takes a string input from the user and uses a while loop to count
# 	the occurrences of each character, storing the counts in a dictionary.
# 	Sample Input:
# 	Enter a string: Hello
# 	Sample Output:
# 	{‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}

# Write a program that simulates an ATM withdrawal process. The user should enter their 
# balance and then enter withdrawal amounts until they decide to stop. Ensure the user does
# not withdraw more than their balance.
# Sample Input and Output:
# Enter your balance: 500
# Enter withdrawal amount: 100
# Remaining balance: 400
# Do you want to make another withdrawal? (yes/no): yes
# Enter withdrawal amount: 50
# Remaining balance: 350
# Do you want to make another withdrawal? (yes/no): no
# Final balance: 350
# Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# Sample Input and Output:
# Enter item price: 2.99
# Enter another item? (yes/no): yes
# Enter item price: 5.49
# Enter another item? (yes/no): no
# Total cost: 8.48
# Write a program that continuously prompts the user to enter a password until they enter a valid one. A valid password must be at least 8 characters long and have a maximum of 25 characters.
# Sample Input and Output:
# Enter password: hello
# Password must be at least 8 characters long and have a maximum of 25 characters.
# Enter password: mysecretpasswordisasecret
# Password accepted.

#  4.	Write a program that asks for the user's age and keeps prompting them until they 
# 	enter a valid age (greater than or equal to 0).
# 	Sample Input and Output:
# 	Enter your age: -5
# 	Invalid age. Please enter a valid age.
# 	Enter your age: 25
# 	Age accepted.
#  5. 	Write a program that tracks the inventory of items in a store. The user should be able 
# 	to add or remove items and the program should display the current inventory after each
# 	operation. The program stops when the user decides to exit.
# 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit




# n = int(input("Enter a number: "))
# i = 1

# while i <= n:
#     print("*" * n)
#     i += 1


# i = 1
# result = ""

# while i <= 10:
#     result += "1"
#     i += 1

# print(result)

i = 1



# while i <= 10:
#     print(i*',' ) 
#     i+=1