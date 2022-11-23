"""
taxi test for prac 9
Jack Kelly
"""

from taxi import Taxi

def main():
    """taxi test"""
    my_taxi = Taxi(100, "Prius 1", 1.23)
    my_taxi.get_fare()
    my_taxi.drive(40)
    print(my_taxi)
    print(my_taxi.get_fare())
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(my_taxi.get_fare())


main()