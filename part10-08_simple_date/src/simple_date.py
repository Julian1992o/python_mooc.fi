# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"

    def converter(self):
        total_days = self.__year * 360 + self.__month * 30 + self.__day
        return total_days
    
    def __lt__(self, another):
        return self.converter() < another.converter()
    
    def __gt__(self, another):
        return self.converter() > another.converter()
    
    def __eq__(self, another):
        return self.converter() == another.converter()
    
    def __ne__(self, another):
        return self.converter() != another.converter()

    def __add__(self, value):
        sum_days = self.converter() + value
        year = sum_days // 360
        month_mod = sum_days % 360
        month = month_mod // 30
        day = month_mod % 30
        return SimpleDate(day, month, year)
    
    def __sub__(self, value):
        sum_days = self.converter() - value.converter()
        return abs(sum_days)
    

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
