class Coffee_maker():
    """Handles coffee machine resources and drink preparation"""
    
    def __init__(self):
        """Initialize with default resource levels"""
        self.resources = {
            'water': 300,    # ml of water
            'milk': 200,     # ml of milk
            'coffee': 100    # grams of coffee
        }

    def Report(self):
        """Display current resource levels"""
        print(f"Water  {self.resources['water']} ml")
        print(f"Milk   {self.resources['milk']} ml")
        print(f"Coffee {self.resources['coffee']} ml")

    def is_resource_sufficient(self, drink):
        """
        Check if there are enough resources to make a drink
        Args:
            drink (Menu_Item): The drink to check resources for
        Returns:
            bool: True if resources are sufficient, False otherwise
        """
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"\nThere is not enough {item}")
                can_make = False
        return can_make
        
    def make_coffee(self, order):
        """
        Deduct resources and make the coffee
        Args:
            order (Menu_Item): The drink being made
        """
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"\nEnjoy your {order.name}!!")
