# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02} eur"
    
    def __eq__(self, another):
        if self.__euros == another.__euros and self.__cents == another.__cents:
            return True
        return False
    
    def _converter_to_cents(self):
        balance = self.__euros * 100
        balance += self.__cents
        return balance
    
    def __lt__(self, another):
        return self._converter_to_cents() < another._converter_to_cents()
    
    def __gt__(self, another):
        return self._converter_to_cents() > another._converter_to_cents()
    
    def __ne__(self, value):
        return self._converter_to_cents() != value._converter_to_cents()
 
    def __add__(self, another):
        total_value = self._converter_to_cents() + another._converter_to_cents()
        euros = total_value // 100
        cents = total_value % 100
        return Money(euros, cents)
        
    def __sub__(self, another):
        if self._converter_to_cents() < another._converter_to_cents():
            raise ValueError("Below zerro!")
        else:
            total_value = self._converter_to_cents() - another._converter_to_cents()
            euros = total_value // 100
            cents = total_value % 100
            return Money(euros, cents)


if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(5, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1