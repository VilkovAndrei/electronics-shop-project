"""Здесь надо написать тесты с использованием pytest для модуля phone."""
import pytest

from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)
phone2 = Phone("Techno Pova 3", 20000.0, 15, 1)

def test__init__():
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120000.0
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2

def test__repr__():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test__str__():
    assert str(phone1) == 'iPhone 14'

def test__add__():
    assert phone1 + phone2 == 20

def test_number_of_sim():
    with pytest.raises(ValueError, match=r"Количество SIM-карт должно быть целым числом больше нуля"):
        phone2.number_of_sim = -1
