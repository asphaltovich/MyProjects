
# Создание класса Сервис
class Service:
    def __init__(self, description, price, duration, features, promotion=None):
        self._description = description
        self._price = price
        self._duration = duration
        self._features = features
        self._promotion = promotion

    # Геттеры и сеттеры
    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_duration(self):
        return self._duration

    def set_duration(self, duration):
        self._duration = duration

    def get_features(self):
        return self._features

    def set_features(self, features):
        self._features = features

    def get_promotion(self):
        return self._promotion

    def set_promotion(self, promotion):
        self._promotion = promotion

    # Методы
    # Простой
    def show_service_info(self):
        print(f"Услуга: {self._description}, цена: {self._price} руб, длительность: {self._duration}")

    # С входным
    def apply_promotion(self, promo):
        self._promotion = promo
        print(f"Акция применена: {promo}")
    # Входные и выходные
    def get_discounted_price(self, discount_percentage):
        discounted = self._price * (1 - discount_percentage / 100)
        return discounted
