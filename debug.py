from coffee import Coffee
from customer import Customer
from order import Order
# Sample data for testing
customers = [
    {"id": 1, "name": "Alice Johnson", "email": "alicej@example.com"},
    {"id": 2, "name": "Brian Carter", "email": "brianc@example.com"},
    {"id": 3, "name": "Carla Mendes", "email": "carla.m@example.com"},
]

orders = [
    {"customer_id": 1, "item": "Cappuccino", "size": "Medium", "quantity": 1, "price": 3.50},
    {"customer_id": 2, "item": "Iced Latte", "size": "Large", "quantity": 2, "price": 7.00},
    {"customer_id": 3, "item": "Espresso", "size": "Small", "quantity": 1, "price": 2.00},
    {"customer_id": 1, "item": "Chai Latte", "size": "Medium", "quantity": 1, "price": 3.75},
]

alice = Customer("Alice")
bob = Customer("Bob")
carla = Customer("Carla")


latte = Coffee("Latte")
espresso = Coffee("Espresso")
mocha = Coffee("Mocha")

# Alice orders
alice.create_order(latte, 4.5)
alice.create_order(latte, 5.0)
alice.create_order(espresso, 2.5)

# Bob orders
bob.create_order(latte, 6.0)
bob.create_order(mocha, 3.0)

# Carla orders
carla.create_order(mocha, 3.5)
carla.create_order(mocha, 4.5)
carla.create_order(latte, 3.0)

print(latte.orders())