"""
make loop
    allow user to input item price
    allow user to input item no.
    deduce total price
    ask if thats all
    if y
        total price
    else
        return
"""

TotalSales = 0
Contin = "N"

while Contin == "N":
    print("Your current total is: $", TotalSales)
    ItemCost = float(input("Price of item:"))
    ItemNo = int(input("Number of items:"))
    TotalSales = TotalSales + (ItemCost * ItemNo)
    Contin = input("Is that all? (Y/N)").upper()

if TotalSales > 100:
    TotalSales = TotalSales * 0.9
    print("You have spent over $100 and have earned a 10% discount!")

print(f"Your final total comes to: ${TotalSales:.2f}")
