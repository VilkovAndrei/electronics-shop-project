"""Здесь надо написать тесты с использованием pytest для модуля keyboard."""
from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test__init__():
    assert kb.name == "Dark Project KD87A"
    assert kb.price == 9600.0
    assert kb.quantity == 5
    assert kb.language == 'EN'


def test_change_lang():
    kb.change_lang()
    assert kb.language == 'RU'
    kb.change_lang()
    assert kb.language == 'EN'
