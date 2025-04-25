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



    def initialize_population(self):
        """ایجاد جمعیت اولیه به صورت تصادفی."""
        return [self.random_solution() for _ in range(self.population_size)]



def find_solution(self):
        """اجرای الگوریتم برای پیدا کردن راه‌حل."""
        for generation in range(self.generations):
            self.create_next_generation()
            best_solution = max(self.population, key=self.calculate_fitness)
            if self.calculate_fitness(best_solution) == 28:  # بررسی وجود راه‌حل بهینه
                return best_solution, generation + 1
        return None, self.generations
