# Classes & Objects in python

# Class creating
class Vehicle:

    # attributes
    color = "Black"
    fuel = "Petrol"
    mileage = "65"

    def start():
        print("When you press clutch & accelrate the car is start")

# Objects creating

car = Vehicle()
print(car.color)

bike = Vehicle()
print(bike.color)

airplane = Vehicle()
print(airplane.mileage)

# We created one class & 3 objects of that class