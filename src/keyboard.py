from src.item import Item


class MixinLayout:
    KB_LAY = 'EN'

    def set_change_lang(self):
        if self.KB_LAY == 'EN':
            self.KB_LAY = 'RU'
            return
        self.KB_LAY = 'EN'
        return

    def get_layout(self):
        return self.KB_LAY


class Keyboard(Item, MixinLayout):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = MixinLayout.get_layout(self)

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        MixinLayout.set_change_lang(self)
        self.__language = MixinLayout.get_layout(self)
