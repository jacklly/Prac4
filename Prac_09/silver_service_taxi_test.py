"""
test of silver service taxi
Jack Kelly
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    century_taxi = SilverServiceTaxi(100, "Toyota Century", 2)
    print(century_taxi)
    century_taxi.drive(18)
    print(century_taxi.get_fare())


main()