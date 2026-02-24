# # # Basic counter-controlled loop (count up)

# # # Print numbers from 1 to 8 using a while loop.
# # i = 1
# # while i <= 8:
# #     print(i)
# #     i +=1

# # # Print numbers from 3 to 12 using a while loop.
# # i = 3
# # while i <= 12:
# #     print(i)
# #     i +=1

# # # Print numbers from 0 to 6 using a while loop.
# # i = 0
# # while i <= 6:
# #     print(i)
# #     i +=1


# 2) Repeat something N times

# Print "Good morning" 4 times.

# i= 1
# while i < N:
#     print("something")

# Print "Python is fun" 6 times.
# i= 1
# while i < 6:
#     print("Python is fun")

# Print "I will practice today" 3 times.
# i = 1
# while i < 3:
# print("I will practice today")


# 3) Filtering with if inside the loop

# Print numbers from 1 to 20, but print only odd numbers.
# i = 1
# while i <=20:
#     if i % 2 == 1:
#         print(i)
#     i+=1

# Print numbers from 1 to 15, but print only numbers divisible by 3.
# i = 1
# while i <= 15:
#     if i % 3 == 0:
#         print(i)
#     i+=1

# # Print numbers from 10 to 30, but print only numbers divisible by 5.
# i = 10
# while i <= 30:
#     if i % 5 == 0:
#         print(i)
#     i+=1 

# 4) Counting down / decrementing loop

# Print numbers from 10 down to 1.
# i= 10
# while i >= 1:
#     print(i)
#     i-= 1




# Ask the user for a number and count down from it to 1.
# countdown = int(input("Enter a number"))
# i = countdown
# while i >= 1:
#     print(i)
#     i-= 1

# Print numbers from 7 down to 0.
# i = 7
# while i >= 0:
#     print(i)
#     i -= 1


# 5) Skip a specific value (no continue)

# Print numbers 1 to 10 but skip 7.
# i = 1
# while i <= 7:
#     if i != 7:
#         print(i)
#     i+=1       

# 5) Skip a specific value (with continue)

# Print numbers 1 to 10 but skip 7.
# i = 1
# while i <= 10:
#     if i == 7:
#         i+=1
#         continue
#     print(i)
#     i+=1


        
# Print numbers 5 to 15 but skip 10.
# i = 1
# while i <= 15:
#     if i == 10:
#         i+=1
#         continue
#     print(i)
#     i+=1




# Print numbers 5 to 15 but skip 10(no continue)
# i = 1
# while i <= 15:
#     if i != 10:
#         print(i)
#     i+=1

# Print numbers 0 to 12 but skip 0.
# i = 1
# while i <= 12:
#     print(i)
#     i+=1


# 6) Pattern printing (square / triangle idea)
# Square

# Ask for n and print an n × n square of #.

# n = int(input("enter a number:   "))
# i = 1
# while i <= n:
#     print("#" * n)
#     i+=1


# Ask for n and print an n × n square of *.

# n = int(input("enter a number"))
# i = 1
# while i <= n:
#     print ("*" * n)
#     i += 1
    
    


# # Ask for n and print an n × n square of @.
# n = int(input("enter a number"))
# i = 1
# while i <= n:
#     print("@"* n)
#     i += 1



# Right triangle

# Ask for n and print a right triangle of * from 1 to n stars.
# n= int(input("enter a number:  "))
# i = 1
# while i <= n:
#     print("*" * i)
#     i+=1


# Ask for n and print a right triangle of +.
# n = int(input("Enter a number"))
# i = 1
# while i <= n:
#     print("+" * i)
#     i+=1

# # Ask for n and print a right triangle of #.
# n = int(input("Enter of a number"))
# i = 1
# while i <= n:
#      print("#" * i)
#      i +=1 




# 7) while ... else

# Count down from 3 to 1, then in else print "Done!".
# i = 3
# while i>= 1:
#     print(i)
#     i-=1
# else:
#     print("Done")


# # Ask user for a number, count down to 1, then print "Finished!" in else.
# countdown = int(input("enter a number:   "))
# i = countdown
# while i >= 1:
#     print(i)
#     i-=1
# else:
#     print("Finished !")


# # Print numbers 1 to 5, then print "All printed" in else.
# i = 1
# while i <=5:
#     print(i)
#     i+=1
# else:
#     print("All printed")


# 8) Build output on one line (accumulate into string)

# Use a while loop to create "AAAAA" (5 A’s) and print it once.
# result = ""
# i = 0
# while i <= 5:


# Use a while loop to create "000000" (6 zeros) and print it once.

# Use a while loop to create "1111111111" (10 ones) and print it once.





# 9) Generate a sequence (multiples)

# Print the first 8 multiples of 2 starting from 2.

# Print the first 6 multiples of 5 starting from 5.

# Print the first 10 multiples of 3 starting from 3.

# 10) Running total (sum / accumulation)

# Ask the user for n and print the sum of 1 to n.

# Ask the user for n and print the sum of even numbers from 2 to n.

# Ask the user for n and print the sum of odd numbers from 1 to n.

# 11) Input-driven loop (sentinel “stop/yes/no”)

# Keep asking the user to enter item prices until they type "stop", then print total.

# Keep asking the user to enter scores until they type "done", then print total score.

# Keep asking the user to enter numbers until they type "0", then print the sum.

# 12) Validation loop (keep prompting until valid)

# Keep asking for age until the user enters a number ≥ 0.

# Keep asking for a password until it is at least 6 characters.

# Keep asking for a number until the user enters a number between 1 and 10.

# 13) Attempt-limited loop (max tries)

# Let the user guess a secret number (e.g. 7) with 3 attempts.

# Ask the user to enter a PIN "1234" with 4 attempts.

# Ask the user to answer "yes" with 2 attempts, else fail.

# 14) Traverse a string with index (string processing)

# Ask for a word and count how many times "a" appears (use while, index).

# Ask for a sentence and count the number of spaces.

# Ask for a word and build the reversed version without slicing.

# 15) Traverse other data structures (tuple / dictionary idea)

# Ask for comma-separated numbers, convert to a tuple, and find the largest without max().

# Ask for comma-separated numbers, convert to a tuple, and find the smallest without min().



# Lets use this: Write a program that simulates an ATM withdrawal process. 
# The user should enter their # balance and then enter withdrawal amounts until they decide to stop. 
# Ensure the user does # not withdraw more than their balance. 
# # Sample Input and Output: 
# # # Enter your balance: 500 # Enter withdrawal amount: 100 
# # # Remaining balance: 400 # Do you want to make another withdrawal? (yes/no): yes 
# # # Enter withdrawal amount: 50 # Remaining balance: 350 
# # # Do you want to make another withdrawal? (yes/no): no # Final balance: 350

# balance = int(input("Enter your account balance:   "))

# while True : 
#     withdrwal = int(input("How much do you want to withdraw ?:    "))
#     if withdrwal > balance:
#         print( " Insuffiicient Balance")
    
#     else:
#         balance = balance - withdrwal
#         print(f" your balance is {balance}")
#         choice = (input("Do you want to make another withdrawal? (yes/no) :    ") ).lower().strip()
#         if choice == "no":
#             break
# print(f"Your balance is {balance}. Have a great day !")
        





# Exercise 1: Mobile Airtime Purchase System
# Problem

# Write a program that simulates buying mobile airtime.

# User enters their wallet balance once

# User can buy airtime multiple times

# Each purchase must not exceed the current balance

# After each purchase, display the remaining balance

# Ask the user if they want to buy airtime again

# Stop when the user says no

# Display final balance at the end

# Sample Interaction
# Enter your wallet balance: 1000
# Enter airtime amount to buy: 200
# Purchase successful. Remaining balance: 800
# Do you want to buy more airtime? (yes/no): yes
# Enter airtime amount to buy: 300
# Purchase successful. Remaining balance: 500
# Do you want to buy more airtime? (yes/no): no
# Final balance: 500

# balance = int(input("enter your wallet balance:    "))
# while True:
#     amount = int(input("Enter airtime amount to buy:   "))
#     if amount > balance:
#         print("Insufficient balance")
#     else:
#         balance-=amount
#     print(f"Your balance is {balance} ")
#     additional_purchase = (input("Do you want to buy more airtime? (yes/no):  ")).lower().strip()
#     if additional_purchase == "no":
#         break
# print(f"Your wallet balance is {balance}. Have a great day !")


# 🟢 Exercise 2: Online Shopping Cart Payment
# Problem

# Write a program that simulates paying for items in a shopping cart.

# User enters their account balance once

# User enters the price of an item

# If the price is more than the balance → show an error

# If allowed → subtract price from balance

# Ask if user wants to pay for another item

# Repeat until the user exits

# Display final balance

# Sample Interaction
# Enter your account balance: 5000
# Enter item price: 1200
# Payment successful. Remaining balance: 3800
# Pay for another item? (yes/no): yes
# Enter item price: 800
# Payment successful. Remaining balance: 3000
# Pay for another item? (yes/no): no
# Final balance: 3000 

# balance = int(input("enters their account balance:   "))
# while True:
#     price = int(input(" enters the price of an item:  "))
#     if price > balance:
#         print("insufficient fund to purchase item")
#     else:
#         balance = balance - price
#         print(f"Payment successful. Remaining balance: {balance}")
        
#     another_item = input("Pay for another item? (yes/no)").lower().strip()
#     if another_item == "no":
#         break
# print(f"Thank you for patronage. Your final balance is {balance} ")



# Write a program that simulates a grocery store checkout. 
# The user should enter the prices of items until they decide to stop. 
# The program should calculate and display the total cost. 
# # Sample Input and Output: 
# # # Enter item price: 2.99 
# # # Enter another item? (yes/no): yes # Enter item price: 5.49 
# # Enter another item? (yes/no): no # Total cost: 8.48

# Total_cost = 0
# while True:
#     Price = int(input("enter the price of item :   "))
#     Quantity = int(input(" enter the Quantity: "))
#     cost_per_item = Price * Quantity
#     Total_cost += cost_per_item
#     additional_items = input( "Do you want to enter another item? (yes/no):   ").lower().strip()
#     if additional_items == "no":
#         break
#     else:
#         Total_cost
# print(f"Total cost is {Total_cost}")


# 🟢 Exercise 1: Fuel Purchase System
# Problem
# Write a program that simulates buying fuel.

# Rules

# User enters their wallet balance once  # Fuel price is ₦650 per liter  # User can buy fuel multiple times

# Cost = liters × 650 # If cost exceeds balance → show Insufficient balance  # After each purchase, ask:# Do you want to buy more fuel? (yes/no):

# Accept ONLY yes or no  # Any other input → Invalid input  # Stop when user enters no    # Print final balance

wallet_balance = int(input("Enter your wallet balance:   "))
price_per_litre = 650

while True:
    litre = int(input("How many litres?:     "))
    cost = litre * price_per_litre
    wallet_balance-=cost
    if cost > wallet_balance:
        print("Insufficient balance")
        break
    else: 
        additional_purchase = input("Do you want to buy more fuel?    ").lower().strip
        additional_purchase == "no"
    print(f"thank for buying {litre}litres from us. Your wallet balance is {wallet_balance}")
    break

 

    







# Sample Interaction
# Enter your wallet balance: 10000
# Enter liters to buy: 5
# Purchase successful. Remaining balance: 6750
# Do you want to buy more fuel? (yes/no): maybe
# Invalid input. Please enter 'yes' or 'no'.
# Do you want to buy more fuel? (yes/no): yes
# Enter liters to buy: 3
# Purchase successful. Remaining balance: 4800
# Do you want to buy more fuel? (yes/no): no
# Final balance: 4800


# 🟢 Exercise 2: Data Subscription Purchase
# Problem

# Write a program that simulates buying mobile data bundles.

# Rules

# User enters wallet balance once

# Each data bundle costs ₦1200

# User can buy multiple bundles

# Total cost = bundles × 1200

# If balance is insufficient → show error

# After each purchase, ask strictly:

# Buy another bundle? (yes/no):


# Reject anything except yes or no

# Stop when user says no

# Print final balance

# Sample Interaction
# Enter your wallet balance: 5000
# Enter number of bundles: 2
# Purchase successful. Remaining balance: 2600
# Buy another bundle? (yes/no): y
# Invalid input. Please enter 'yes' or 'no'.
# Buy another bundle? (yes/no): yes
# Enter number of bundles: 1
# Purchase successful. Remaining balance: 1400
# Buy another bundle? (yes/no): no
# Final balance: 1400
    