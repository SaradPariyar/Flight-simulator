class Car:

    # Class initializer that sets registration number and maximum speed
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num  # Registration number
        self.max_speed = max_speed  # Maximum speed
        self.current_speed = 0  # Current speed (initially zero)
        self.travelled_distance = 0  # Travelled distance (initially zero)

    # Class method that changes the current speed based on a parameter
    def accelerate(self, change):
        # Add the change to the current speed
        self.current_speed += change

        # Check if the current speed exceeds the maximum speed
        if self.current_speed > self.max_speed:
            # Set the current speed to the maximum speed
            self.current_speed = self.max_speed

        # Check if the current speed is below zero
        if self.current_speed < 0:
            # Set the current speed to zero
            self.current_speed = 0

    # Class method that increases travelled distance based on number of hours
    def drive(self, hours):
        # Calculate how much distance is travelled in given time at constant speed
        distance = hours * self.current_speed

        # Add distance to travelled distance
        self.travelled_distance += distance


# Main program where you create a list of cars for race

import random  # Import random module for generating random numbers

cars = []  # Create an empty list for storing car objects

for i in range(10):
    max_speed = random.randint(100, 200)  # Generate a random maximum speed between 100 and 200 km/h
    reg_num = "ABC-" + str(i + 1)  # Generate a registration number as "ABC-1", "ABC-2" etc.
    new_car = Car(reg_num, max_speed)  # Create a new car object with given parameters
    cars.append(new_car)  # Append the new car object to the list

# Start the race until one of the cars has travelled at least 10,000 km

winner = None  # Initialize winner as None

while not winner:
    for car in cars:
        change = random.randint(-10, 15)  # Generate a random change in speed between -10 and +15 km/h
        car.accelerate(change)  # Change the current speed of car using accelerate method
        car.drive(1)  # Drive for one hour using drive method

        if car.travelled_distance >= 10000:
            winner = car.reg_num  # Set winner as registration number of winning car
            break  # Break out of loop

# Print out properties of each car formatted into table

print("Reg Num\tMax Speed\tCurrent Speed\tTravelled Distance")
print("-------------------------------------------------------")

for car in cars:
    print(car.reg_num + "\t" + str(car.max_speed) + "\t\t" + str(car.current_speed) + "\t\t" + str(
        car.travelled_distance))

print("-------------------------------------------------------")
print("The winner is:", winner)