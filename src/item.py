import csv

# from descriptors import descriptors


class Item:
    """
    Класс для представления товара в магазине.
    """
    __pay_rate = 1.0
    all = []
    CSV_FILE = '../src/items.csv'

    # name = descriptors.GoodsName()
    # price = descriptors.GoodsPrice()
    # quantity = descriptors.GoodsQuantity()

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
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.__pay_rate

    def __str__(self):
        return f"{self.__name} {self.price} {self.quantity}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise ValueError("длина наименования товара не может быть больше 10 симвовов")
        self.__name = new_name

    @classmethod
    def set_pay_rate(cls, new_rate) -> None:

        if 0 <= new_rate:
            cls.__pay_rate = new_rate
        else:
            raise ValueError("Не может быть отрицательным или равным '0'")

    @classmethod
    def instantiate_from_csv(cls, CSV_PATH='../src/items.csv'):
        with open(CSV_PATH) as file:
            file_reader = csv.DictReader(file, delimiter=',')
            for i in file_reader:
                name, price, quantity = i.get('name'), int(i.get('price')), int(i.get('quantity'))
                cls.all.append((name, price, quantity))

    @staticmethod
    def string_to_number(any_string: str) -> int:
        try:
            return int(any_string)
        except ValueError:
            return int(any_string[0: any_string.find('.')])
