"""Write a Python program to implement the class chosen with its attributes and methods based on the requirements given below:
identify_distance_that_can_be_travelled(): Return the distance that can be travelled by the vehicle without using the reserve fuel. If the fuel left is less than or equal to reserve fuel, the method should return 0.
identify_distance_travelled(initial_fuel): Return the distance so far travelled by the vehicle based on the initial fuel,fuel left and mileage.
Assume that initial fuel is always greater than fuel left.
Represent a vehicle and test your program by initializing the instance variables and invoking the appropriate methods."""

class Vehicle:
    def __init__(self, mileage=0, fuel_left=0):
        self.mileage = mileage
        self.fuel_left = fuel_left
        self.reserve_fuel = 5  # Reserve fuel is fixed

    def identify_distance_that_can_be_travelled(self):
        if self.fuel_left <= self.reserve_fuel:
            return 0
        return (self.fuel_left - self.reserve_fuel) * self.mileage

    def identify_distance_travelled(self, initial_fuel):
        if initial_fuel > self.fuel_left:
            return (initial_fuel - self.fuel_left) * self.mileage
        return 0

# Create a Vehicle object with mileage 12 km/l and 20 litres of fuel left
car = Vehicle(12, 20)

# Calculate and print the maximum distance without using reserve fuel
print("Maximum distance that can be covered without using the reserve fuel:", car.identify_distance_that_can_be_travelled(), "kms")

# Calculate and print distance travelled assuming initial fuel was 25 litres
print("Distance travelled based on the initial fuel:", car.identify_distance_travelled(25), "kms")