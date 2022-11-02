"""
Started: 3:00
Finished:

"""


class Guitar:
    """Make a guitar processing class"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        age = 2022 - int(self.year)
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
