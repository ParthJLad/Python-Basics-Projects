# Create a class Laptop with attributes: brand, RAM, price. Create 2 objects with different values

class Laptop:
    brand = "HP"
    RAM = "8GB"
    price = "1 Lakh"

# first object
obj1 = Laptop()
obj1.brand = "MackBook Air"
obj1.RAM = "16 GB"
obj1.price = "1.5 Lakh"

print("Laptop1 Brand:-", obj1.brand)
print("Laptop1 RAM:-", obj1.RAM)
print("Laptop1 Price:-", obj1.price)

# second object
obj2 = Laptop()
obj2.brand = "DELL"
obj2.RAM = "8 GB"
obj2.price = "90 thousands"
print("Laptop2 Brand:-", obj2.brand)
print("Laptop2 RAM:-", obj2.RAM)
print("Laptop2 Price:-", obj2.price)
