"""Example of a class and object instaniation."""


class Pizza: 
    """Models the idea of a Pizza."""
    # attributes 
    size: str 
    toppings: int 
    extra_cheese: bool 

    def price(self) -> float:
        """Calculate price of a Pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else: 
            total += 8.0
        
        total += self.toppings * 0.75 

        if self.extra_cheese:
            total += 1.0

        return total 
    

a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
a_pizza.extra_cheese = False 
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price()}")