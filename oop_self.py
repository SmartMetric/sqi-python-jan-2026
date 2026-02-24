# Task

# Create a class School.

# Add a class attribute COUNTRY = "Nigeria".

# In __init__, store name and location.

# Create two School objects.

# Print the country using:

# the class name

# one object

class School:
    COUNTRY = "Nigeria"
    def __init__(self,store_name, location):
        self.store_name = store_name
        self.location = location
    def country_name(self):
        return f" I am a citizen of {School.COUNTRY}" 
    


# Create a class called Employee with:

        
# attributes: name, department

# method: details()
# which returns:
# "My name is {name} and I work in the {department} department."

# Create a class called Manager that inherits from Employee.

# Do not add any new attributes or methods to Manager.

# Create one Manager object with:

# name: "Amina"

# department: "Finance"

# Call the details() method on the Manager object and print the result.
class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def details(self):
        return f"My name is {self.name} and I work in the {self.department} department."
class Manager(Employee):
    def __init__(self, name, department, level):
        super().__init__(name, department)
        self.level = level

# staff = Manager("Amina", "Finance")
# print(staff.details())



