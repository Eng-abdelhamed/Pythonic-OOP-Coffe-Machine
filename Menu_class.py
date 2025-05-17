class Menu_Item():
    """Represents a single drink menu item"""
    
    def __init__(self, name, water, milk, coffee, cost):
        """
        Initialize a menu item
        Args:
            name (str): Name of the drink
            water (int): Water required (ml)
            milk (int): Milk required (ml)
            coffee (int): Coffee required (grams)
            cost (float): Price of the drink
        """
        self.name = name 
        self.cost = cost
        self.ingredients = {
            'water': water,
            'milk': milk,
            'coffee': coffee
        }

class Menu():
    """Handles the coffee machine menu"""
    
    def __init__(self):
        """Initialize with default menu items"""
        self.menu = [
            Menu_Item(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            Menu_Item(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            Menu_Item(name="cappuccino", water=250, milk=50, coffee=24, cost=3)  
        ]

    def get_items(self):
        """Return all drink names as a formatted string"""
        options = ""
        for item in self.menu:
            options += f"|{item.name}|"
        return options
    
    def find_drink(self, order_name):
        """
        Search for a drink by name
        Args:
            order_name (str): Name of drink to find
        Returns:
            Menu_Item: The drink if found, None otherwise
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, this item was not found")
        return None