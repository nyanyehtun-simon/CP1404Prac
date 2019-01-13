class User:
    def __init__(self, name, num_of_tacos = 5, score = 0):
        self.name = name
        self.num_of_tacos = num_of_tacos
        self.score = score

    def pass_the_taco(self):
        return self.num_of_tacos

