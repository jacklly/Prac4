"""
test of silver service taxi
Jack Kelly
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test with a fancy taxi"""
    century_taxi = SilverServiceTaxi(100, "Toyota Century", 2)
    print(century_taxi)
    century_taxi.drive(18)
    print(f"${century_taxi.get_fare():.2f}")


main()
