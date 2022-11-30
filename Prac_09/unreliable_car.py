"""
Unreliable car exercise
Jack Kelly
"""

from car import Car
from random import randint


class UnreliableCar(Car):
    """Create class for an unreliable car"""
    def __init__(self, name, fuel, reliability):
        """Define car and reliability"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """See if car will drive, then drive"""
        generated_reliability = randint(0, 100)
        if generated_reliability >= self.reliability:
            distance = 0
        super().drive(distance)