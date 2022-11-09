"""
Guitar Program!
Started: 6 30
Finished:
"""

from Prac_06.guitar import Guitar


def main():
    with open("guitars.csv", "r", encoding="utf-8-sig") as in_file:
        guitars = []
        for line in in_file:
            split_line = line.strip().split(",")
            guitar = Guitar(split_line[0], split_line[1], float(split_line[2]))
            guitars.append(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
