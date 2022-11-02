"""
Began 3:20

"""
from Prac_06.guitar import Guitar

"""Create a program that reads guitar inputs and sorts them to a list"""


def main():
    guitars_list = []
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print(f"{name} ({year}) : {cost:.2f} added!")
        new_guitar = Guitar(name, year, cost)
        guitars_list.append(new_guitar)
        name = input("Name: ")

    guitars_list.append(Guitar("Rusan Cloud Guitar", 1983, 111200))
    guitars_list.append(Guitar("Hohner Madcat", 1977, 5882.32))
    guitars_list.append(Guitar("Rickenbacker 330", 1958, 3416.71))
    guitars_list.append(Guitar("Auerswald Symbol Guitar", 1995, 200000))

    print("These are my guitars: ")
    number = 1
    max_price = max(len(str(guitar.cost)) for guitar in guitars_list) + 3
    max_name = max(len(guitar.name) for guitar in guitars_list)
    for i, guitar in enumerate(guitars_list, 1):
        if guitar.is_vintage():
            print(
                f"Guitar {i:2}: {guitar.name:{max_name}} ({guitar.year}), worth ${guitar.cost:{max_price},.2f} (Vintage)")
        else:
            print(f"Guitar {i:2}: {guitar.name:{max_name}} ({guitar.year}), worth ${guitar.cost:{max_price},.2f}")
        number = number + 1


main()
