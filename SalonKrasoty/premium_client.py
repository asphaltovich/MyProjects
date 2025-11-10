
from client import Client

# Создание класса ПремиумКлиент
class PremiumClient(Client):
    def __init__(self, target_audience, age, gender, name, behavior, vip_level):
        super().__init__(target_audience, age, gender, name, behavior)
        self._vip_level = vip_level

    def get_vip_level(self):
        return self._vip_level

    def set_vip_level(self, vip_level):
        self._vip_level = vip_level

    # Переопределение метода
    def show_basic_info(self):
        super().show_basic_info()
        print(f"VIP-статус: {self._vip_level}")
