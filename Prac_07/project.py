"""Project class"""


class Project:
    """Class that defines a project item"""

    def __init__(self, name="", date="", priority=0, cost_estimate=0, completion_percentage=0):
        """Init for project"""
        self.name = name
        self.date = date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Print the project"""
        return f"{self.name}, start: {self.date}, priority {self.priority}, estimate: ${self.cost_estimate:}" \
               f", completion: {self.completion_percentage}%"

    def completed(self):
        """Return true for complete project"""
        if self.completion_percentage == "100":
            return True
        else:
            return False
