from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number: int):
        super().__init__(name, price, quantity)
        if int(number)!=number or number <= 0:
             raise ValueError('Количество SIM-карт должно быть целым числом больше нуля')
        self.__number_of_sim = number

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        if int(number) != number or number <= 0:
            raise ValueError("Количество SIM-карт должно быть целым числом больше нуля")
        self.__number_of_sim = number

    def __repr__(self):
        return f"{Phone.__name__}(\'{self.name}\', {str(int(self.price))}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, (Item, Phone)):
            raise ValueError("Нельзя сложить классы 'Phone' или 'Item' с не 'Phone' или 'Item'")
        return self.quantity + other.quantity
