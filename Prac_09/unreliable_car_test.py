"""
Testing of unreliable car class
"""

from unreliable_car import UnreliableCar


def main():
    """create reliable car"""
    corolla = UnreliableCar(100, "1999 Toyota Corolla", 90)
    print(corolla)
    """create unreliable car"""
    rx7 = UnreliableCar(100, "1987 FC Rx7", 20)
    print(rx7)

    """test cars over 100km"""
    for number in range(1, 10):
        corolla.drive(10)
        rx7.drive(10)

    """see state of cars"""
    print(corolla)
    print(rx7)


main()
