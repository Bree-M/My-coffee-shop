class Coffee:
    def __init__(self,name):
        self.name = name

        if isinstance(self._name, str) and len(self._name) >= 3:
            return self._name
        else:
            raise ValueError("Name must be atleast 3 characters.")
    
    @property
    def name(self):
        return self._name
    
    def orders(self):
        from order import Order
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.order()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        if self.num_orders() == 0:
            return 0
        return sum(order.price for order in self.order()) / len(self.order())
    
    
   
   
