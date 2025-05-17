# Coffee Machine Simulator

A Python OOP implementation of a coffee vending machine with resource management, payment processing, and menu system.

## Features

- **Drink Preparation**
  - Tracks water, milk, and coffee resources
  - Checks resource sufficiency before brewing
  - Updates resources after each order

- **Payment System** 
  - Accepts coins (quarters, dimes, nickels, pennies)
  - Calculates change
  - Tracks total profits

- **Menu System**
  - 3 default drinks (latte, espresso, cappuccino)
  - Easy-to-extend for new drinks
  - Case-insensitive drink selection

- **Admin Functions**
  - Resource reporting
  - Profit reporting
  - Machine power control

## Class Structure

| Class | Description |
|-------|-------------|
| `Coffee_maker` | Manages machine resources and brewing |
| `Menu_Item` | Represents a single drink recipe |
| `Menu` | Handles drink menu operations |
| `Money_machine` | Processes payments and profits |


3. For drinks:
- Insert coins when prompted
- Receive your drink (if resources/payment sufficient)
- Get change if overpaid

## 📋 Example Flow

```text
What would you like? |latte||espresso||cappuccino|: 
> latte

Please insert coins:
How many Quarters?: 4
How many dimes?: 2
How many nickles?: 1
How many pennies?: 3

Here is $0.23 in change.
Enjoy your latte!!
```
# How to Use This Project

## Installation

To clone and run this coffee machine simulator:

```bash
# Clone the repository
gh repo clone Eng-abdelhamed/Pythonic-OOP-Coffe-Machine

# Navigate to project directory
cd Pythonic-OOP-Coffe-Machine

# Run the coffee machine
python MainProgram.py
## Usage

1. Run the Python script
2. Choose from available commands:
```
# Using HTTPS
```bash
git clone https://github.com/Eng-abdelhamed/Pythonic-OOP-Coffe-Machine.git

# Or using SSH (requires GitHub SSH setup)
git clone git@github.com:Eng-abdelhamed/Pythonic-OOP-Coffe-Machine.git
```
