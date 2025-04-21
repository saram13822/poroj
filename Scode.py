import random

class EightQueensGA:
     def random_solution(self):    #لیستی از موقعیت وزیرها    
        """ایجاد یک راه‌حل تصادفی."""
        return random.sample(range(self.n), self.n)
