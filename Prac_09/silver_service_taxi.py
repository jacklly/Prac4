"""
Silver service taxi class
Jack Kelly
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Deluxe taxi class"""

    def __init__(self, name, fuel, fanciness):
        """Define taxi parameters"""
        super().__init__(name, fuel)
        self.flagfall = 4.5
        self.fanciness = fanciness
        self.price_per_km = self.fanciness * self.price_per_km

    def __str__(self):
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare," \
               f" ${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        return f"${round(super().get_fare()+4.5, 1):.2f}"

