# # 1) Print numbers from 1 to 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1


# # 2) Print "Hello" 3 times
# i = 0
# while i < 3:
#     print("Hello")
#     i += 1


# # 3) Print only even numbers from 2 to 10 (do not use += 2)
# i = 2
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# # 4) Print numbers in reverse from 5 to 1
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1


# # 5) Print numbers from 1 to 10, but skip 5 (no continue)
# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1


# # 6) Print a square of stars (user enters n)
# n = int(input("Enter a number: "))
# i = 1
# while i <= n:
#     print("*" * n)
#     i += 1


# # 7) Print a right triangle of stars (user enters n)
# n = int(input("Enter a number: "))
# i = 1
# while i <= n:
#     print("*" * i)
#     i += 1


# # 8) Print a countdown (user enters start)
# start = int(input("Enter a number: "))
# i = start
# while i >= 1:
#     print(i)
#     i -= 1
# print("Go!")


# # 9) Print "1" ten times on the same line
# i = 1
# result = ""
# while i <= 10:
#     result += "1"
#     i += 1
# print(result)


# # 10) Print the first 12 multiples of 3 starting from 3
# i = 1
# while i <= 12:
#     print(3 * i)
#     i += 1


# # 11) Print numbers from 1 to 10
# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# # 12) Sum of natural numbers up to n (user enters n)
# n = int(input("Enter a number: "))
# i = 1
# total = 0
# while i <= n:
#     total += i
#     i += 1
# print(total)


# # 13) Guessing game (random 1..50, max 5 attempts, hints)


# # 14) Keep asking for password until correct ("secret")
# password = input("Enter password: ")
# while password != "secret":
#     password = input("Enter password: ")
# print("Access granted")


# # 15) Countdown from a number to zero (user enters n)
# n = int(input("Enter a number: "))
# while n >= 0:
#     print(n)
#     n -= 1


# # 16) Print all even numbers from 1 to n (user enters n)
# n = int(input("Enter a number: "))
# i = 1
# while i <= n:
#     if i % 2 == 0:
#         print(i)
#     i += 1


# # 17) Power using while loop (base^exponent)
# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))
# result = 1
# i = 0
# while i < exponent:
#     result *= base
#     i += 1
# print(f"{base} raised to the power of {exponent} is {result}")


# # 18) Count vowels in a string
# s = input("Enter a string: ").lower().strip()
# i = 0
# count = 0
# while i < len(s):
#     if s[i] in "aeiou":
#         count += 1
#     i += 1
# print(count)


# # 19) Reverse a string using while loop (no slicing, no reversed)
# s = input("Enter a string: ")
# i = len(s) - 1
# rev = ""
# while i >= 0:
#     rev += s[i]
#     i -= 1
# print(rev)


# # 20) Comma-separated integers -> tuple -> find minimum (no min())



# # 21) Count occurrences of each character in a string (dictionary)



# # 22) ATM withdrawal simulation
# balance = float(input("Enter your balance: "))
# choice = "yes"

# while choice.lower() == "yes":
#     amount = float(input("Enter withdrawal amount: "))
#     if amount <= balance:
#         balance -= amount
#         print(f"Remaining balance: {balance}")
#     else:
#         print("Insufficient balance.")
#     choice = input("Do you want to make another withdrawal? (yes/no): ")

# print(f"Final balance: {balance}")





# # 23) Grocery store checkout total
# total = 0.0
# choice = "yes"

# while choice.lower() == "yes":
#     price = float(input("Enter item price: "))
#     total += price
#     choice = input("Enter another item? (yes/no): ")

# print(f"Total cost: {total}")


# # 24) Keep asking for a valid password (8..25 chars)
# pwd = input("Enter password: ")
# while len(pwd) < 8 or len(pwd) > 25:
#     print("Password must be at least 8 characters long and have a maximum of 25 characters.")
#     pwd = input("Enter password: ")
# print("Password accepted.")


# # 25) Keep asking for valid age (>= 0)
# age = int(input("Enter your age: "))
# while age < 0:
#     print("Invalid age. Please enter a valid age.")
#     age = int(input("Enter your age: "))
# print("Age accepted.")


# # 26) Inventory tracker (add/remove/exit)
# inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam": 2}

# op = input("Enter operation (add/remove/exit): ").strip().lower()
# while op != "exit":
#     item = input("Enter item: ").strip().lower()
#     qty = int(input("Enter quantity: "))

#     if op == "add":
#         inventory[item] = inventory.get(item, 0) + qty
#     elif op == "remove":
#         if item in inventory:
#             inventory[item] = max(0, inventory[item] - qty)
#         else:
#             inventory[item] = 0

#     print(f"Current inventory: {inventory}")
#     op = input("Enter operation (add/remove/exit): ").strip().lower()
