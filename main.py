from types import NoneType


class Soda:
    def __init__(self,ingridient = None):
        self.ingridient = ingridient

    def __call__(self,):
        self.show_my_drink()


    def show_my_drink(self):
        if self.ingridient:
            if isinstance(self.ingridient,str):
                print(f'Газировка и  {self.ingridient}')
            else:
                print('Неверные данные')
        else:
           print('Обычная газировка')

    def __str__(self):
        if self.ingridient:
            if isinstance(self.ingridient, str):
                return f"Газировка и {self.ingridient}"
            else:
                return "Некорректная добавка(должна быть строкой)"
        else:
            return "Обычная газировка"

    def __repr__(self):
        return f"Soda(additive = {repr(self.ingridient)})"


drink1 = Soda()
drink2 = Soda('малина')
drink3 = Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()

print(str(drink1))
print(str(drink2))
print(str(drink3))

print(repr(drink1))
print(repr(drink2))
print(repr(drink3))
