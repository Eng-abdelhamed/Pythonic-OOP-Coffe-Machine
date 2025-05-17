from Coffe_class import Coffee_maker
from Menu_class import Menu
from Money_class import Money_machine



# Initialize system components
coffee_maker = Coffee_maker()
menu = Menu()
money_machine = Money_machine()

def report():
    """Display machine status"""
    coffee_maker.Report()
    money_machine.Report()

# Main machine loop
machine_on = True
while machine_on:
    # Get user input
    customer_choice = input(
        f"\nType REPORT to see resources and profit" +
        f"\nType OFF to stop the machine" + 
        f"\nWhat would you like? {menu.get_items()}: \n"
    ).lower()
    
    if customer_choice == "report":
        report()
    elif customer_choice == "off":
        machine_on = False
    else:
        drink = menu.find_drink(customer_choice)
        
        if drink and coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)