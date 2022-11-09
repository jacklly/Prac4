"""
Guitar Program!
Started: 6 30
Finished:
"""

from Prac_06.guitar import Guitar


def main():
    """create guitar lists"""
    guitars, savable_guitars = list_creation()
    """add guitars"""
    guitar_adder(guitars, savable_guitars)
    """sort guitars"""
    guitars.sort()
    """display guitars"""
    display_guitars(guitars)
    """save guitars"""
    save_guitars(savable_guitars)


def save_guitars(savable_guitars):
    with open("guitars.csv", "w", encoding="utf-8-sig") as out_file:
        for guitar in savable_guitars:
            print(guitar, file=out_file)


def display_guitars(guitars):
    print("Your guitars:")
    for guitar in guitars:
        print(guitar)


def guitar_adder(guitars, savable_guitars):
    choice = input("Do you wish to add a guitar? (Y/N)").upper()
    while choice == "Y":
        name = input("Name: ")
        year = input("Year: ")
        cost = input("Cost: ")
        combo = (name, year, cost)
        additive = (",").join(combo)
        savable_guitars.append(additive)
        guitars.append(Guitar(name, year, float(cost)))
        choice = input("Do you wish to add another guitar? (Y/N)").upper()


def list_creation():
    with open("guitars.csv", "r", encoding="utf-8-sig") as in_file:
        guitars = []
        savable_guitars = []
        for line in in_file:
            split_line = line.strip().split(",")
            savable_line = line.strip()
            guitar = Guitar(split_line[0], split_line[1], float(split_line[2]))
            guitars.append(guitar)
            savable_guitars.append(savable_line)
    return guitars, savable_guitars


main()
