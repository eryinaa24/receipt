#Item Total Price Calculator & Formatter
A simple Python script that takes an item's details (name, quantity, and unit price) as input, calculates the total cost, and displays the output in a neatly formatted, aligned layout.

#Features
Flexible Input Parsing: Accepts multi-variable input on a single line using .split().
Data Type Casting: Automatically converts quantity to integers and price to floating-point numbers.
Structured Formatting: Uses Python f-strings with alignment specifiers (<, >, and precise decimal rounding) to mimic a clean receipt/table format.

#How It Works
Line 1: Enter the Item Name (String).
Line 2: Enter both the Quantity (Integer) and Unit Price (Float) separated by a space.
Output: The script calculates Total = Quantity * Price and prints the item name, quantity, and total price with custom spacing.

#Code Structure
S: Item Name
Q: Quantity
U: Unit Price / Price per item
Total: The calculated total cost (Q * U)

#Usage Example
Input:
Apple
5 1.50
Output:
Apple    5      7.50

#Requirements
Python 3.6+ (required for f-string formatting)
