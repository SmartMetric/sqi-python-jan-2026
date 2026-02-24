class Person:
    def __init__(self, first_name: str, last_name: str, age: int, height: float, is_male:bool):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.is_male= is_male

    def walk(self):
        return "I am walking"
    
    def run(self):
        return "I am running"
    
    def intro(self):
    
        return f"My name is {self.first_name} {self.last_name}"
    
person1 = Person("Ajana", "Olumide", 23, 3, True)
print(person1.age)
print(person1.intro())
print(person1.run())

person2 = Person("Damilola", "Ola", 22, 4.3, False)
print(person2.age)
print(person2.intro())
print(person2.run())



class Car:
    def __init__(self, brand, model, year, horsepower, fuel_type):
        self.brand = brand
        self.model= model
        self.year= year
        self.horsepower= horsepower
        self.fuel_type= fuel_type
            
    def car_info(self ):
        return f"This is a {self.year} {self.brand} with {self.horsepower} HP running on {self.fuel_type} "
    
prado = Car("Toyota", "Prado", 2023, 6, "Petrol")  
bora = Car("Volkswage", "Bora", 2016, 4, "Hybrid")
Vibe = Car("Pontiac", "Vibe", 2018, 7, "Diesel")



class Student:
    def __init__(self, name, age, grades):
        self.name=name
        self.age=age
        self.grades=grades
    
# OOP - Object Oriented Programming


# class BankAccount:
#     # magic dunder (double underscore) method
#     def __init__(self, bank_name: str, account_holder: str, balance: float, is_savings: bool):
#         print("something")
#         self.my_bank_name = bank_name
#         self.account_holder = account_holder
#         self.balance = balance
#         self.is_savings = is_savings

#     def withdraw(self, amount):
#         self.balance -= amount
#         return "Withdrawal accepted"
    

#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposit accepted")
    

# account1 = BankAccount("Wema", "Olumide Ajayi", 90_000_000, False)
# print(account1.my_bank_name)
# print(account1.withdraw(1_000_000))
# print(account1.balance)
# account1.deposit(7000)

# print(account1.balance)


# print(account1.balance)

# account1.balance = 100_000_000

# print(account1.balance)

# account2 = BankAccount("Fidelity", "Francis Ezebue", 8_500_992, True)


# print(account2.balance)

# print(account2.is_savings)


# BankAccount("Wema", "Olumide Ajayi", 90_000_000, False)
# print(BankAccount("Wema", "Olumide Ajayi", 90_000_000, False).bank_name)


# print(id(BankAccount("Wema", "Olumide Ajayi", 90_000_000, False)))
# print(id(BankAccount("Wema", "Olumide Ajayi", 90_000_000, False)))


# Create a class Person with the attributes: first_name, last_name, age, height, is_male
# The actions the person created out of the Person class can take are:

# 1. walk - Print "I am walking"
# 2. run - Print "I am running"
# 3. intro - My name is {frist_name} {last_name}

# Create two instances of the Person class
# Print their age, make them introduce themselves, and make them run.


# class Person:
#     def __init__(self, first_name: str, last_name: str, age: int, height: float, is_male: bool):
#         self.full_name = first_name + " " + last_name
#         self.age = age
#         self.height = height
#         self.is_male = is_male

#     def walk(self):
#         print("i am walking")

#     def walk_some_distance(self, distance):
#         print(f"I am walking {distance} km.")

#     def run(self):
#         return "I am running"
    
#     def intro(self):
#         print(f"My name is {self.full_name}")


# winnie = Person("Winifred", "Igboama", 24, 1.62, False)
# print(winnie.age)
# winnie.intro()
# winnie.walk_some_distance(7)
# print(winnie.run())




# 1. Create a class called Car with the following attributes:
#    - brand
#    - model
#    - year
#    - horsepower
#    - fuel_type
#
#    The class should have a method called car_info() that returns:
#    "This is a {year} {brand} {model} with {horsepower} HP running on {fuel_type}."
#
#    After defining the class, create 3 different Car objects with different values.





# 2. Create a class called Student with the following attributes:
#    - name
#    - age
#    - grades (a list of integers)
#
#    The class should have two methods:
#    - average_grade(): returns the average of all grades
#    - is_passing(): returns True if the average grade is >= 50, otherwise False
#
#    After defining the class, create 2 different Student objects with different values.

# class Student:
#     def __init__(self, name: str, age: int, grades: list[int]):
#         self.name = name
#         self.age = age
#         self.grades = grades

#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
    
#     def is_passing(self):
#         return self.average_grade() >= 50


# pelumi = Student("Pelumi", 13, [90, 34, 89, 100, 26])
# print(pelumi.average_grade())
# print(pelumi.is_passing())





# 1. Create a class called Laptop with the following attributes:
#    - brand
#    - ram (in GB)
#    - storage (in GB)
#    - price
#
#    The class should have two methods:
#    - upgrade_ram(extra_ram): increases the ram by extra_ram
#    - laptop_info(): returns "{brand} laptop with {ram}GB RAM and {storage}GB storage costs {price}."
#
#    After defining the class, create 2 different Laptop objects with different values.





# 2. Create a class called Employee with the following attributes:
#    - name
#    - position
#    - salary
#
#    The class should have two methods:
#    - give_raise(amount): increases salary by amount
#    - employee_info(): returns "{name} works as a {position} and earns {salary} per year."
#
#    After defining the class, create 3 different Employee objects with different values.





# 3. Create a class called Phone with the following attributes:
#    - brand
#    - model
#    - battery_percentage
#
#    The class should have two methods:
#    - charge(amount): increases battery_percentage by amount (do not exceed 100)
#    - phone_status(): returns "{brand} {model} battery is at {battery_percentage}%."
#
#    After defining the class, create 2 different Phone objects with different values.





# 4. Create a class called Product with the following attributes:
#    - name
#    - price
#    - quantity_in_stock
#
#    The class should have three methods:
#    - restock(amount): increases quantity_in_stock by amount
#    - sell(amount): decreases quantity_in_stock by amount
#    - inventory_value(): returns total value of stock (price * quantity_in_stock)
#
#    After defining the class, create 3 different Product objects with different values.





# 5. Create a class called Course with the following attributes:
#    - course_name
#    - instructor
#    - students (a list of student names)
#
#    The class should have two methods:
#    - add_student(name): adds a student to the students list
#    - total_students(): returns the number of students enrolled
#
#    After defining the class, create 2 different Course objects with different values.





# 6. Create a class called Circle with the following attributes:
#     - radius
#
#     The class should have two methods:
#     - area(): returns 3.14 * radius * radius
#     - circumference(): returns 2 * 3.14 * radius
#
#     After defining the class, create 3 different Circle objects with different values.



# ------------------------------------------------CLASS ATTRS & INHERITANCE------------------------------------------------

# class Rectangle:

#     NO_OF_SIDES = 4

#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#         self.area = length * breadth

#     def perimeter(self):
#         return 2 * (self.length + self.breadth)
    
#     def print_no_of_sides(self):
#         # return f"A square has {self.NO_OF_SIDES} sides"
#         return f"A rectangle has {Rectangle.NO_OF_SIDES} sides"
    

# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)

#     def print_no_of_sides(self):
#         return f"A square has {Rectangle.NO_OF_SIDES} sides"
    
    

# rectangle = Rectangle(6, 5)
# square1 = Square(3)

# print(square1.print_no_of_sides())
# print(rectangle.print_no_of_sides())

# print(square1.length)
# print(square1.breadth)
# print(square1.area)
# print(square1.perimeter())

# square1 = Square(3)
# square2 = Square(12)

# print(square1.area)
# print(square1.perimeter())

# print(square1.NO_OF_SIDES)
# print(square2.NO_OF_SIDES)

# print(square1.print_no_of_sides())

# print(square2.area)
# print(square2.perimeter())

# print(square2.print_no_of_sides())

# print(Square.NO_OF_SIDES)


# class Animal:
#     def __init__(self, name: str, type: str, has_tail: bool, can_fly: bool, is_mammal: bool, age: int):
#         self.name = name
#         self.type = type
#         self.has_tail = has_tail
#         self.can_fly = can_fly
#         self.is_mammal = is_mammal
#         self.age = age
#         self.article = "an" if self.type[0].lower() in "aeiou" else "a"

#     def intro(self):
#         return f"My name is {self.name}. I am a/an {self.type}. I am {self.age} years old."
    
#     def speak(self):
#         return f"{self.type} is speaking"
    

# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, "dog", True, False, True, age)
#         self.article = "an"
#         self.breed = breed

#     def intro(self):
#         animal_intro = super().intro()
#         animal_intro += f" I am a/an {self.breed}. I am {self.article} dog."
#         return animal_intro  


# elephant = Animal("Winnie", "Elephant", True, False, True, 2)
# dog = Dog("Bruno", 3, "Siberian Husky")

# print(elephant.intro())
# print(dog.intro())

# class Book:
#     def __init__(self, author: str, title: str, no_of_pages: int, is_fiction: bool, year_of_pub: int):
#         self.author = author
#         self.title = title
#         self.no_of_pages = no_of_pages
#         self.is_fiction = is_fiction
#         self.year_of_pub = year_of_pub

#     def __str__(self):
#         return f"{self.title} by {self.author} published in {self.year_of_pub}"

# class Library:
#     def __init__(self, books: list[Book]):
#         self.books = books

#     def add_book(self, book: Book):
#         if isinstance(book, Book):
#             self.books.append(book)
#             return "Book added successfully"
#         return "Only Books can be added to the library"
    
#     def how_many_pages(self):
#         return sum(book.no_of_pages for book in self.books)

    
# book1 = Book(author="George Orwell", title="1984", no_of_pages=328, is_fiction=True, year_of_pub=1949)
# book2 = Book(author="Michelle Obama", title="Becoming", no_of_pages=448, is_fiction=False, year_of_pub=2018)
# book3 = Book(author="J.K. Rowling", title="Harry Potter and the Philosopher's Stone", no_of_pages=223, is_fiction=True, year_of_pub=1997)

# print(book1)
# print(book2)
# print(book3)

# community_library = Library([book1, book2])
# print(community_library.add_book(1))
# print(community_library.add_book(book3))
# print(community_library.books)
# print(community_library.how_many_pages())


# print(isinstance(1, Book))
# print(isinstance(1, int))
# print(isinstance(book2, Book))

# class CartItem:
#     def __init__(self, item_name, price, qty):
#         self.total =  price * qty

# class Cart:
#     def __init__(self, cart_items: list[CartItem]):
#         self.cart_items = cart_items

#     def cart_total(self):
#         return sum(cart_item.total for cart_item in self.cart_items)

# class CartItem:
#     def __init__(self, item_name, price, qty):
#         self.price =  price
#         self.qty = qty

# class Cart:
#     def __init__(self, cart_items: list[CartItem]):
#         self.cart_items = cart_items

#     def cart_total(self):
#         return sum((cart_item.price * cart_item.qty) for cart_item in self.cart_items)


# cart_item1 = CartItem("eggs", 250, 4)
# cart_item2 = CartItem("bread", 1200, 6)
# cart = Cart([cart_item1, cart_item2])
# print(cart.cart_total()) # -> 8200




# ============================================================
# EXERCISE: Vehicle Classes
# ============================================================
#
# 1. Create a class called `Vehicle` with the following:
#
#    __init__ receives: name (str), type (str), has_engine (bool),
#                       is_electric (bool), can_fly (bool), top_speed (int)
#
#    Store all parameters as instance attributes.
#    Also create an attribute called `category`:
#       - If top_speed is greater than 100, category should be "fast"
#       - Otherwise, category should be "slow"
#
#    Methods:
#       describe(self) -> str
#           Returns: "This is {name}. It is a {type}. Its top speed is {top_speed} km/h."
#
#       honk(self) -> str
#           Returns: "The {type} is honking"
#
#
# 2. Create a class called `Bicycle` that inherits from `Vehicle`.
#
#    __init__ receives: name, top_speed, gear_count
#
#    Calls the parent __init__ with the following fixed values:
#       type = "bicycle", has_engine = False, is_electric = False, can_fly = False
#       (name and top_speed come from the parameters)
#
#    After calling super().__init__, override category to be "eco-friendly"
#    Also store gear_count as an instance attribute.
#
#    Override describe(self):
#       Start by calling the parent's describe() method.
#       Append to it: " It has {gear_count} gears. It is {category}."
#       Return the full string.
#
#
# 3. Create the following objects and print their descriptions:
#
#    car = Vehicle("Thunderbolt", "Car", True, False, False, 200)
#    bicycle = Bicycle("Greenway", 25, 21)
#
#    print(car.describe())
#    print(bicycle.describe())
#
#
# EXPECTED OUTPUT:
#
# This is Thunderbolt. It is a Car. Its top speed is 200 km/h.
# This is Greenway. It is a bicycle. Its top speed is 25 km/h. It has 21 gears. It is eco-friendly.
#
# ============================================================


# Write your code below:

# ------------------------------------------------CLASS ATTRS & INHERITANCE------------------------------------------------


# ------------------------------------------------ASSIGNMENT CORRECTION------------------------------------------------



# 1. Create a class called Playlist with the following attributes:
#    - name
#    - songs (a list of strings)
#
#    The class should have three methods:
#    - add_song(song): adds a new song title to the playlist
#    - total_songs(): returns the total number of songs
#    - show_songs(): returns all song titles as a comma-separated string
#
#    After defining the class, create a Playlist and add a few songs.



# class Playlist:
#     def __init__(self, name, songs: list[str]):
#         self.name = name
#         self.songs = songs

#     def add_song(self, song):
#         self.songs.append(song)

#     def total_songs(self):
#         return len(self.songs)
    
#     def show_songs(self):
#         return ", ".join(self.songs)

# # # Example usage:
# pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
# pl.add_song("Lose Yourself")
# pl.add_song("Can't Hold Us")

# print(pl.name, "has", pl.total_songs(), "songs")
# print("Songs:", pl.show_songs())

# Expected Output:
# Workout Jams has 4 songs
# Songs: Eye of the Tiger, Stronger, Lose Yourself, Can't Hold Us


# 2. Create a class called ShoppingCart with the following attributes:
#    - owner
#    - items (a dictionary where keys are item names and values are prices)
#
#    The class should have three methods:
#    - add_item(item, price): adds the item with its price
#    - total_cost(): returns the sum of all prices
#    - most_expensive(): returns the item with the highest price
#
#    After defining the class, create a ShoppingCart and add multiple items.

# class ShoppingCart:
#     def __init__(self, owner: str, items: dict[str, int]):
#         self.owner = owner
#         self.items = items

#     def __str__(self):
#         return f"{self.owner}'s cart contains: "+ ", ".join(self.items)

#     def add_item(self, item, price):
#         self.items[item] = price

#     def total_cost(self):
#         return sum(self.items.values())
    
#     def most_expensive(self):
#         return max(self.items, key=self.items.get)

# shopping_cart = ShoppingCart("Winnie", {"eggs": 1000, "rice": 70000, "bread": 3000})
# print(shopping_cart.total_cost())

# shopping_cart.add_item("milk", 1200)

# print(shopping_cart)

# print(shopping_cart.total_cost())


# 3.

# class OrderItem:
#     def __init__(self, item_name, qty):
#         self.item_name = item_name
#         self.qty = qty

# class Order:
#     def __init__(self, order_items: list[OrderItem]):
#         self.order_items = order_items


# class Warehouse:
#     def __init__(self, inventory: dict[str, int]):
#         self.inventory = inventory

#     def place_order(self, order: Order):
#         temp_inventory = self.inventory.copy()
#         order_fulfillable = True
#         for order_item in order.order_items:
#             if order_item.item_name in self.inventory and order_item.qty <= self.inventory[order_item.item_name]:
#                 temp_inventory[order_item.item_name] -= order_item.qty
#             else:
#                 order_fulfillable = False
#                 return False
#         if order_fulfillable:
#             self.inventory = temp_inventory
#             return True
            



# warehouse = Warehouse({
#     "laptop": 10,
#     "phone": 25,
#     "headphones": 50
# })

# order1 = Order([
#     OrderItem("laptop", 2),
#     OrderItem("phone", 5),
# ])

# order2 = Order([
#     OrderItem("laptop", 9), 
#     OrderItem("headphones", 2)
# ])

# print(warehouse.place_order(order1))
# # -> True

# print(warehouse.inventory)
# # -> {'laptop': 8, 'phone': 20, 'headphones': 50}

# print(warehouse.place_order(order2))
# # -> False

# print(warehouse.inventory)
# # -> {'laptop': 8, 'phone': 20, 'headphones': 50}

# order3 = Order([
#     OrderItem("tv", 7)
# ])

# print(warehouse.place_order(order3))


# print(warehouse.inventory)

# order4 = Order([
#     OrderItem("headphones", 7)
# ])

# print(warehouse.place_order(order4))


# print(warehouse.inventory)

# ------------------------------------------------ASSIGNMENT CORRECTION------------------------------------------------



# class ShoppingCart:
#     def __init__(self, owner: str, items: dict[str, int]):
#         self.owner = owner
#         self.items = items
#         print("running in init")

#     def __str__(self):
#         return f"{self.owner}'s cart contains: "+ ", ".join(self.items)
    

#     def __repr__(self):
#         return f'ShoppingCart("{self.owner}", {self.items})'
    
#     def __len__(self):
#         return len(self.items)
        

#     def add_item(self, item, price):
#         self.something = "Something"
#         self.items[item] = price

#     def total_cost(self):
#         return sum(self.items.values())
    
#     def most_expensive(self):
#         print(self.something)
#         return max(self.items, key=self.items.get)

# shopping_cart = ShoppingCart("Winnie", {"eggs": 1000, "rice": 70000, "bread": 3000})

# # print(isinstance(shopping_cart, ShoppingCart))

# # print(shopping_cart.total_cost())

# # shopping_cart.add_item("milk", 1200)
# # print(shopping_cart.most_expensive())


# print(str(shopping_cart))
# print(repr(shopping_cart))
# print(len(shopping_cart))


# # print(len(7))
# print(len([7]))



# class Device:
#     def operate(self):
#         print("I am operating the device")

# class SmartPhone:
#     def operate(self):
#         print("I am operating the smartphone")

# class SmartTV:
#     def operate(self):
#         print("I am operating the Smart TV")

# device = Device()
# samsung = SmartPhone()
# lg_tv = SmartTV()
# devices = [device, samsung, lg_tv]

# for device in devices:
#     device.operate()

# class Device:
#     def operate(self):
#         return "I am operating the"

# class SmartPhone(Device):
#     def operate(self):
#        return super().operate() + " smartphone"

# class SmartTV(Device):
#     def operate(self):
#         return super().operate() + " smart TV"

# device = Device()
# samsung = SmartPhone()
# lg_tv = SmartTV()
# devices = [samsung, lg_tv]

# for device in devices:
#     print(device.operate())


# class Device:
#     def operate(self):
#         return "I am operating the device"

# class SmartPhone(Device):
#     pass

# class SmartTV(Device):
#     pass

# device = Device()
# samsung = SmartPhone()
# lg_tv = SmartTV()
# devices = [samsung, lg_tv]

# for device in devices:
#     print(device.operate())



# You are building a simple simulation of a fantasy battle. Create different types of game 
# characters.

# 1. Create a base class
# Create a class called GameCharacter that has:
# Attributes:
# name (string)
# health (integer)
# attack_power (integer)

# Methods:
# A method attack(target) that reduces the target's health by self.attack_power.

# 2. Create subclasses
# Warrior
# Has an extra attribute: armor (integer)
# Override attack(target) so that it deals extra 10 damage.

# Mage
# Has an extra attribute: mana (integer)
# Override attack(target) so that it uses 5 mana each time it attacks. 
# If mana is less than 5, print "Not enough mana to attack".

# 3. Handle cases where the target is the same as the attacker.

class GameCharacter:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        if target == self:
            print(f"{self.name} cannot attack themself")
            return
        
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name}!")
        print(f"{target.name}'s health is now {target.health}")


class Warrior(GameCharacter):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)
        self.armor = armor

    def attack(self, target):
        target.health -= 10
        super().attack(target)

class Mage(GameCharacter):
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def attack(self, target):
        if self.mana < 5:
            print("Not enough mana to attack")
            return
        super().attack(target)
        self.mana -= 5


# SAMPLE EXECUTION 1
warrior = Warrior(name="Thor", health=100, attack_power=10, armor=20)
mage = Mage(name="Merlin", health=100, attack_power=10, mana=10)
warrior.attack(mage)
# Output:
# Thor attacks Merlin!
# Merlin's health is now 80
mage.attack(warrior)
# Output:
# Merlin attacks Thor!
# Thor's health is now 90
mage.attack(warrior)
# Output:
# Merlin attacks Thor!
# Thor's health is now 80
mage.attack(warrior)
# Output:
# Not enough mana to attack
print(warrior.health)  # 80
print(mage.health)  # 80
print(mage.mana)  # 0



# SAMPLE EXECUTION 2
merlin = Mage(name="Merlin", health=100, attack_power=20, mana=10)
gaius = Mage(name="Gaius", health=100, attack_power=10, mana=30)

merlin.attack(gaius)
# Output:
# Merlin attacks Gaius
# Gaius’s health is now 80
gaius.attack(merlin)
# Output:
# Gaius attacks Merlin
# Merlin’s health is now 90
gaius.attack(gaius)
# Output:
# Gaius cannot attack themself
gaius.attack(merlin)
# Output:
# Gaius attacks Merlin
# Merlin’s health is now 80
merlin.attack(gaius)
# Output:
# Merlin attacks Gaius
# Gaius’s health is now 60
merlin.attack(gaius)
# Output:
# Not enough mana to attack



    

        
