# You are building a simple simulation of a space mission. There are different types of spacecraft.

# 1. Create a base class
# Create a class called Spacecraft with:
# Attributes:
# name (string)
# fuel (integer)

# Methods:
# launch() — prints "Launching {name}!"
# Reduces fuel by 50 units.
# If not enough fuel, print "Not enough fuel to launch."

# refuel(amount) — adds amount to fuel.

# 2. Create subclasses
# CargoShip
# Has an additional attribute: cargo_weight (integer)
# Override launch() — launching consumes extra fuel depending on cargo:
# total fuel reduction = 50 + (cargo_weight * 2)
#             
# PassengerShip
# Has an additional attribute: passenger_count (integer)
# Override launch() — if passenger_count > 100, print "Too many passengers. 
# Cannot launch."
# Otherwise, launch normally (reduce fuel by 50 units)

# 3. Handle negative refuel amounts.

# # SAMPLE EXECUTION
# # Create objects
# cargo_ship = CargoShip("Galactic Hauler", 200, 30)
# passenger_ship = PassengerShip("Star Voyager", 100, 80)



class Spacecraft:
    def __init__(self, name:str, fuel):
        self.name = name
        self.fuel = fuel
    def launch(self):
        
        if self.fuel < 50:
            print("Not enough fuel to launch")
        else:
            print(f"Launching {self.name}")

    def refuel(self,amount ):
        if amount < 0:
            print("Negative figure not allowed ")
        else:
            self.fuel += amount

class Cargoship(Spacecraft):
    def __init__(self, name: str, fuel,cargo_weight):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight
    def launch(self):
        fuel = 50 + (self.cargo_weight * 2)
class PassengerShip(Spacecraft):
    def __init__(self, name: str, fuel, passenger_count):
        super().__init__(name, fuel)
        self.passsenger_count = passenger_count
    def launch(self):
        if self.passsenger_count > 100:
            print("Too many passengers. Cannot launch")
        else:
            self.fuel -= 50 
cargo_ship = Cargoship("Galactic Hauler", 200,30)
passenger_ship = PassengerShip("Star Voyager", 100,80)

cargo_ship.launch()
print("Launching Galactic Hauler with cargo !")

print("")
# # Attempt to launch both ships
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 200 - (50 + 30*2) = 90




# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 100 - 50 = 50

# # Refuel both ships
# cargo_ship.refuel(50)
# # Output: Refueled Galactic Hauler with 50 units. Fuel is now 140.

# passenger_ship.refuel(30)
# # Output: Refueled Star Voyager with 30 units. Fuel is now 80.

# # Launch again after refueling
# cargo_ship.launch()
# # Output: Launching Galactic Hauler with cargo!
# # Fuel after launch: 140 - (50 + 30*2) = 30

# passenger_ship.launch()
# # Output: Launching Star Voyager!
# # Fuel after launch: 80 - 50 = 30

# # Try to refuel with invalid amount
# cargo_ship.refuel(-10)
# # Output: Cannot refuel with negative amount.

# # Test PassengerShip with too many passengers
# passenger_ship.passenger_count = 120
# passenger_ship.launch()
# # Output: Too many passengers. Cannot launch.

# # Try to launch cargo ship with low fuel
# cargo_ship.launch()
# # Output: Not enough fuel to launch.

