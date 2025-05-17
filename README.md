# ☕ Coffee Machine Simulator

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

## Usage

1. Run the Python script
2. Choose from available commands:
