# Scenario: You want to create a bank account that supports deposits and 
# withdrawals.

# Task: Create a bank account class that has two attributes:

# owner
# balance

# and two methods:
# deposit
# Withdraw

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount_deposited):
        self.balance += amount_deposited
        print("deposit successful")
    def withdrawal(self, amount_withdrawn):
        if amount_withdrawn <= self.balance:
            self.balance -= amount_withdrawn
            print(f"{amount_withdrawn} was successfully withdrawn. Your balance is {self.balance}")
        else:
            print("Insufficient fund")

acct1 = BankAccount('Winnie', 100)
print(acct1.balance)
        
    

        


# Withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and 
# test to make sure the account 
# can't be overdrawn.

# You are not expected to use the input function, just pass in values 
# for the amounts into 
# the methods directly, no need for loops either.

# See the next slide for a sample execution of the code you will 
# write.

# class Account: 
#     pass
    

# #1. Instantiate the class
# acct1 = Account('Winnie', 100)

# #2. Print the object
# print(acct1)
# # Output:
# # Account owner: Winnie
# # Account balance: $100

# #3. Show the account owner attribute
# print(acct1.owner)  # Winnie

# #4. Show the account balance attribute 
# print(acct1.balance)  # 100

# #5. Make a series of deposits and withdrawals 
# acct1.deposit(50)  # Output: Deposit Accepted

# acct1.withdraw(15)  # Output: Withdrawal Accepted

# #6. Make a withdrawal that exceeds the available balance 
# acct1.withdraw(500)  # Output: Funds Unavailable!


