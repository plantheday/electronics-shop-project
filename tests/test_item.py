"""Здесь надо написать тесты с использованием pytest для модуля item."""


from src.item import Item


def test_init():
    phone = Item("iphone", 100000, 9)
    assert phone.name == "iphone"
    assert phone.price == 100000
    assert phone.quantity == 9


def test_calculate_total_price():
    phone = Item("iphone", 100000, 9)
    return phone.price
    assert return(price) == 100000


def test_apply_discount():
    phone = Item("iphone", 100000, 9)
    assert phone.price == phone.price * phone.pay_rate
