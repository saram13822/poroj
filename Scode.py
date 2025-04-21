import random

class EightQueensGA:
     def random_solution(self):    

        return random.sample(range(self.n), self.n)
     


     def calculate_fitness(self, solution):
        """محاسبه برازندگی یک راه‌حل."""
        clashes = 0      #شمارش تداخل ها
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if solution[i] == solution[j] or abs(solution[i] - solution[j]) == j - i: #بررسی تداخل
                    clashes += 1
        return 28 - clashes  # برازندگی حداکثر 28 برای 8 وزیر
