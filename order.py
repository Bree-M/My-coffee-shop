class Customer:
  
    def __init__(self, name):
        self.name = name

class Coffee:
  
    def __init__(self, name):
        self.name = name

class Order:

    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("customer must be an instance of Customer")

        if not isinstance(coffee, Coffee):
            raise ValueError("coffee must be an instance of Coffee")

        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("price must be a float between 1.0 and 10.0")

        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

   
    def customer(self):
        return self._customer

    def coffee(self):
        return self._coffee

    def price(self):
        return self._price   

        


