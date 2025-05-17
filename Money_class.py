class Money_machine():

    """Handles payment processing and profit tracking"""
    
    Currency = "$"  # Currency symbol
    
    # Coin values in dollars
    coin_values = {
        "Quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        """Initialize with zero profit and money received"""
        self.profit = 0
        self.money_received = 0

    def Report(self):
        """Display current profit"""
        print(f"Money: {self.Currency}{self.profit}")

    def process_coins(self):
        """Calculate total value of coins inserted"""
        print("\nPlease insert coins")
        self.money_received = 0  # Reset before processing new coins
        
        for coin in self.coin_values:
            count = int(input(f"How many {coin}?: "))
            self.money_received += count * self.coin_values[coin]
        
        return self.money_received
    
    def make_payment(self, cost):
        """
        Process payment for a drink
        Args:
            cost (float): Price of the drink
        Returns:
            bool: True if payment successful, False otherwise
        """
        self.process_coins()
        
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"\nHere is {self.Currency}{change} in change.")
            self.profit += cost
            self.money_received = 0  # Reset for next transaction
            return True
        else:
            print("Sorry, that's not enough money. Money refunded!")
            self.money_received = 0
            return False