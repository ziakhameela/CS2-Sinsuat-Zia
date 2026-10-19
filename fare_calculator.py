# Travel Fare Calculator
FARE_RATE = 14

name = input("Enter passenger name: ")
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number

# Travel Fare Calculator
FARE_RATE = 14

# Validate passenger name
while True:
    name = input("Enter passenger name: ").strip()
    if name:
        break
    print("Invalid input. Name cannot be empty.")

# Validate distance
while True:
    try:
        distance = float(input("Enter distance (km): "))
        if distance > 0:
            break
        print("Invalid input. Distance must be greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Validate number of passengers
while True:
    try:
        passengers = int(input("Enter number of passengers: "))
        if passengers > 0:
            break
        print("Invalid input. Enter at least 1 passenger.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Calculate fare
total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
