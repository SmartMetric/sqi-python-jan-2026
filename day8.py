# ---------------------------------------------------ASSIGNMENT---------------------------------------------------

# 1) Find total cost.
# Input: price_per_item = 19, quantity = 3
# Output: 57

price_per_item = 19
quantity = 3
total_cost = price_per_item * quantity
print(int(total_cost))


# 2) Get average of two scores (show result as a number).
# Input: score1 = 78, score2 = 86
# Output: 82.0

score1 = 78
score2 = 86
av_score = (score1 + score2)/2
print(float(av_score))

# 3)How many full boxes are needed given items and box capacity.
# Input: items = 53, box_capacity = 6
# Output (full boxes): 8

items = 53
box_capacity = 6
full_boxes = items // box_capacity 
print(full_boxes)

# 4) How many items left over after filling full boxes.
# Input: items = 53, box_capacity = 6
# Output (leftover items): 5

items = 53
box_capacity = 6
full_boxes = items % box_capacity 
print(full_boxes)

# 5) Test evenness.
# Input: n = 42
# Output: True # (True if n is even, False if odd)

n = 42
print(n % 2 ==0) 

# 6) Compute the cube of a number
# Input: x = 4
# Output: 64

x = 4
print(x ** 3)

# 7) Temperature conversion (Celsius to Fahrenheit).
# Input: celsius = 25
# Output: 77.0
celsius = 25
# Formula= ((1°C × 9/5) + 32) 
Fahrenheit = (25 * (9/5) + 32 )
print(Fahrenheit)

# 8) Currency to smallest unit: convert dollars to cents.
# Input: dollars = 3.25
# Output: 325

# Formula:
# Cents = Dollars × 100

dollars = 3.25
print(int(dollars * 100) )

# 9) Time conversion: given total seconds, compute minutes and remaining seconds.
# Input: total_seconds = 125
# Output: 2 minutes and 5 seconds

# Formula: seconds / 60

total_seconds = 125
minute = total_seconds // 60
sec = total_seconds % 60
print(f"{minute} minutes and {sec} seconds") 

# 10) Check if a number is strictly between two others.
# Input: low = 10, x = 14, high = 20
# Output: True
low = 10 
x = 14
high = 20
# value = low < x and x < high 
value = low < x < high
print(value)

# 11) Is the number divisible by both 3 and 5?
# Input: n = 30
# Output: True
n = 30
print(n % 3== 0 and n % 5 ==0)


# 12) Extract the last digit of a positive integer.
# Input: n = 12345
# Output: 5

n = 12345
n = "12345"
print(int(n[-1]))



# 13) Compare two integers and print if they are equal (True/False).
# Input: a = 42, b = 42
# Output: True
a = 42
b = 42
print(a==b)

# 14) Compute the midpoint (average) between two integers.
# Input: p = 5, q = 8
# Output: 6.5

p = 5
q = 8
print((5+8)/2)

# 15) Compute cost per person: total_bill divided equally among people (show decimal if needed).
# Input: total_bill = 123.45, people = 4
# Output: 30.8625

total_bill = 123.45
people = 4
print(float(total_bill/people))


# 16) Convert a price given in euros to another currency using a rate.
# Input: euros = 50, rate = 1.13
euros = 50
rate = 1.13
naira = euros * rate
print(round(naira, 1), )

# 17) Show the opposite of a given boolean value.
# Input: flag = False
# Output: True

flag = True
print(not flag)

# ---------------------------------------------------ASSIGNMENT---------------------------------------------------

