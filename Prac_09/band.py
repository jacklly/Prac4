"""
Create band class for other files
Jack Kelly
"""


class Band:
    """Create band class for my_band"""

    def __init__(self, band_name):
        """init"""
        self.band_name = band_name
        self.band_list = []
        self.musician_list = []

    def __str__(self):
        """string for band"""
        printable_band_list = ",".join(self.band_list)
        return f"{self.band_name} ({printable_band_list}"

    def add(self, musician):
        """Adding a musician / their instruments"""
        self.band_list.append(musician.__str__())
        self.musician_list.append(musician)

    def play(self):
        """play instruments"""
        for musician in self.musician_list:
            """Ensure musician has instrument"""
            if not musician.instruments:
                print(f"{musician.name} needs an instrument!")
            else:
                print(f"{musician.name} is playing: {musician.instruments}")
