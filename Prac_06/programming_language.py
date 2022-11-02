"""
Begun at 2:38
Finished at 2:57
Took 19 minutes
"""


class ProgrammingLanguage:
    """Translate info about a programming language"""

    def __init__(self, name, typing, reflection, year):
        """Set as selves"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.reflection:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection = {self.reflection}, First appeared in {self.year}"
