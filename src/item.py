import csv


class InstantiateCSVError(Exception):
    def __init__(self):
        super().__init__("Файл items.csv поврежден")


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, file='../src/items.csv') -> None:
        cls.all.clear()
        try:
            with open(file, "r", encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                if len(reader.fieldnames) != 3:
                    raise InstantiateCSVError()
                for dict_item in reader:
                    Item(dict_item['name'], float(dict_item['price']), Item.string_to_number(dict_item['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")
        except KeyError:
            raise InstantiateCSVError()

    @staticmethod
    def string_to_number(str_in_file: str) -> int:
        return int(float(str_in_file))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        result = self.price * self.quantity
        return result

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    def __repr__(self):
        return f"{Item.__name__}(\'{self.name}\', {str(int(self.price))}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Нельзя сложить классы 'Phone' или 'Item' с не 'Phone' или 'Item'")
        return self.quantity + other.quantity
