import datetime


class Guitar:
    NOW = datetime.datetime.now()

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${}".format(self.name, self.year, self.cost)

    def get_age(self):
        return self.NOW.year - self.year

    def is_vantage(self):
        return self.get_age() >= 50
