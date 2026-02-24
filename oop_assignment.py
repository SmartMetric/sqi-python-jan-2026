# # 1. Create a class called Laptop with the following attributes:
# #    - brand
# #    - ram (in GB)
# #    - storage (in GB)
# #    - price
# #
# #    The class should have two methods:
# #    - upgrade_ram(extra_ram): increases the ram by extra_ram
# #    - laptop_info(): returns "{brand} laptop with {ram}GB RAM and 
# #      {storage}GB storage costs {price}."
# #
# #    After defining the class, create 2 different Laptop objects with 
# #    different values.

# class Laptop:
#     def __init__(self, brand, ram, storage, price):
#         self.brand = brand
#         self.ram = ram
#         self.storage = storage
#         self.price = price

        
#     def ugrade_ram(self, extra_ram):
#         self.ram += extra_ram
    
#     def laptop_info(self):
#         return f"{self.brand} laptop with {self.ram}GB RAM and {self.storage}GB storage costs {self.price}"
    
# HP= Laptop("HP", 30, 5, 500000)
# Dell = Laptop("Dell", 30, 5, 620000)


# # 2. Create a class called Employee with the following attributes:
# #    - name
# #    - position
# #    - salary
# #
# #    The class should have two methods:
# #    - give_raise(amount): increases salary by amount
# #    - employee_info(): returns "{name} works as a {position} and 
# #   earns {salary} per year."
# #
# #    After defining the class, create 3 different Employee objects with 
# #   different values.
# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
        
#     def give_raise (self, amount):
#         self.salary += amount
#     def employee_info(self): 
#         return f"{self.name} works as a {self.position} and earns {self.salary} per year."
     
# Ella = Employee("Ella Joshua", "Secretary", 50000)
# Mohammed = Employee("Mohammed Madaki", "Notary Writer", 50000)
# John = Employee("John Aluko", "Data Analyst", 50000)
          
    
# # 3. Create a class called Phone with the following attributes:
# #    - brand
# #    - model
# #    - battery_percentage
# #
# #    The class should have two methods:
# #    - charge(amount): increases battery_percentage by amount 
# #   (do not exceed 100)
# #    - phone_status(): returns "{brand} {model} battery is at 
# #   {battery_percentage}%."
# #
# #    After defining the class, create 2 different Phone objects with 
# #   different values.
# class Phone:
#     def __init__(self, brand, model, battery_percentage):
#           self.brand = brand
#           self.model = model
#           self.battery_percentage = battery_percentage
#     def charge(self, amount):
#         self.battery_percentage += amount 
#         if self.battery_percentage >= 100:
#              self.battery_percentage = 100

#     def phone_status(self): 
#         return f"{self.brand} {self.model} battery is at {self.battery_percentage}%."

# Samsung = Phone("Samsung", "S2", 90)   
# Nokia = Phone("Nokia", "3310", 100) 


# # 4. Create a class called Product with the following attributes:
# #    - name
# #    - price
# #    - quantity_in_stock
# #
# #    The class should have three methods:
# #    - restock(amount): increases quantity_in_stock by amount
# #    - sell(amount): decreases quantity_in_stock by amount
# #    - inventory_value(): returns total value of stock 
# #   (price * quantity_in_stock)
# #
# #    After defining the class, create 3 different Product objects with 
# #   different values.
# class Product:
#     def __init__(self, name, price, quantity_in_stock):
#           self.name = name
#           self.price = price
#           self.quantity_in_stock = quantity_in_stock
#     def restock(self, amount):
#         self.quantity_in_stock += amount
#     def sell(self, amount):
#          self.quantity_in_stock -= amount
#     def inventory_value(self):
#         return f"total value of stock {self.price * self.quantity_in_stock}"
         
# Coke = Product("Coke", 500, 1)
# Fanta = Product("Fanta", 500, 1)
# Water = Product("Water", 500, 3)


# # 5. Create a class called Course with the following attributes:
# #    - course_name
# #    - instructor
# #    - students (a list of student names)
# #
# #    The class should have two methods:
# #    - add_student(name): adds a student to the students list
# #    - total_students(): returns the number of students enrolled
# #
# #    After defining the class, create 2 different Course objects 
# # with different values.

# class Course:
#     def __init__(self, course_name, instructor, students) :
#         self.course_name = course_name
#         self.instructor = instructor
#         self.students = students 
#     def add_student(self, name):
#         self.students.append(name)
#     def total_students(self):
#         sum(self.students)
# Mythology = Course("Mythology", "Prof.Salami", ["Olu", "Sola", "James"])

# Python = Course("Python", "Miss Winnie", ["Olu", "Adil", "Francis, Pelumi"])


# #6. Create a class called Circle with the following attributes:
# #     - radius
# #
# #     The class should have two methods:
# #     - area(): returns 3.14 * radius * radius
# #     - circumference(): returns 2 * 3.14 * radius
# #
# #     After defining the class, create 3 different Circle objects with different values.

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius
#     def circumference(self):
#         return 2 * 3.14 * self.radius


# # Fill in the Line class methods to accept coordinates as a pair of tuples and 
# # return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.


# # class Line:
# #     def __init__(self, coor1, coor2): 
# #         pass

# #     def distance(self):
# #         pass

# #     def slope(self):
# #         pass

# # # EXAMPLE EXECUTION

# # coordinatel = (3,2)
# # coordinate2 = (8,10)

# # line_1 = Line(coordinatel, coordinate2)

# # print(line_1.distance())  # 9.433981132056603
# # print(line_1.slope())  # 1.6



# # Fill in the class

# class Cylinder:
#     def __init__(self, height=1, radius=1):
#         self.height = height
#         self. radius = radius


#         return 3.14 * self.radius * self.radius * self.height

#     def volume (self):
        

#     # def surface_area(self):
#     #     pass

# # EXAMPLE EXECUTION

# # cylinder = Cylinder(2,3)
# # print(cylinder.volume()) 
# #  # 56.52#