"""Здесь надо написать тесты с использованием pytest для модуля item."""


from src.item import Item


def test_init():
    phone = Item("iphone", 100000, 9)
    assert phone.name == "iphone"
    assert phone.price == 100000
    assert phone.quantity == 9
