# Создание класса Сервис
class Service:
    def __init__(self, description, price, duration, features, promotions=None):
        self.__description = description
        self.__price = price
        self.__duration = duration
        self.__features = features
        self.__promotions = promotions if promotions else []

    # Геттеры и сеттеры
    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_features(self):
        return self.__features

    def set_features(self, features):
        self.__features = features

    def get_promotions(self):
        return self.__promotions

    def set_promotions(self, promotions):
        self.__promotions = promotions

    # Методы 
    # Простой: вывод информации о услуге
    def show_info(self):
        print(f"Услуга: {self.__description}, цена: {self.__price} руб., длительность: {self.__duration} мин.")

    # С входным параметром: добавление акции
    def add_promotion(self, promo):
        self.__promotions.append(promo)
        print(f"Добавлена акция: {promo}")

    # Входные и выходные: возвращает цену с учетом скидки (если есть акция)
    def get_price_with_discount(self, discount_percentage):
        discount_amount = self.__price * discount_percentage / 100
        return self.__price - discount_amount
