"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

item1 = Item("Смартфон", 10000.0, 20)
item2 = Item("Ноутбук", 20000.0, 5)

def test__init__():
    assert item1.name == "Смартфон"
    assert item2.price == 20000.0
    assert item1.quantity == 20

def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000.0


def test_apply_discount():
    Item.pay_rate = 0.1
    item2.apply_discount()
    assert item2.price == 2000.0


def test__init__all():
    start_len = len(Item.all)
    Item("test", 1, 1)
    assert len(Item.all) == start_len + 1


def test_name():
    item2.name = "СуперСмартфон"
    assert item2.name == "СуперСмарт"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('101') == 101
    assert Item.string_to_number('101.0') == 101
    assert Item.string_to_number('101.5') == 101
