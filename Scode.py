import random

class EightQueensGA:
     def random_solution(self):    

        return random.sample(range(self.n), self.n)
