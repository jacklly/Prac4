"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

bonus = 0

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales > 999:
        bonus = sales * 0.15
        input(print("Your bonus is: $", bonus, "  -Press Enter to continue."))
        sales = float(input("Enter sales: $"))
    elif sales < 1000:
        bonus = sales * 0.1
        input(print("Your bonus is: $", bonus, "  -Press Enter to continue."))
        sales = float(input("Enter sales: $"))
else:
    print("ERROR: Please input a correct value.")
