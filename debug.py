from coffee import Coffee
from customer import Customer
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")
carla = Customer("Carla")

# Create coffees
latte = Coffee("Latte")
espresso = Coffee("Espresso")
mocha = Coffee("Mocha")

# Create orders
alice.create_order(latte, 4.5)
alice.create_order(latte, 5.0)
alice.create_order(espresso, 2.5)

bob.create_order(latte, 6.0)
bob.create_order(mocha, 3.0)

carla.create_order(mocha, 3.5)
carla.create_order(mocha, 4.5)
carla.create_order(latte, 3.0)

# Test output
print("\n=== Test Output ===")
print(f"Alice's orders: {len(alice.orders())}")
print(f"Coffees Alice ordered: {[coffee.name for coffee in alice.coffees()]}")
print(f"Latte customers: {[customer.name for customer in latte.customers()]}")
print(f"Latte orders count: {latte.num_orders()}")
print(f"Latte average price: {latte.average_price():.2f}")
print(f"Biggest latte fan: {Customer.most_aficionado(latte).name}")