"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

from src.item import Item


def test_init():
    phone = Item("iphone", 100000, 9)
    assert phone.name == "iphone"
    assert phone.price == 100000
    assert phone.quantity == 9

def test_calculate_total_price():
    pen = Item("pen", 10, 5)
    assert pen.calculate_total_price() == 50


def test_apply_discount():
    pencil = Item("pencil", 5, 10)
    pencil.apply_discount()
    assert pencil.price == 5



