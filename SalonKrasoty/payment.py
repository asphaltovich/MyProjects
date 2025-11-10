# Создание класса Оплата
class Payment:
    def __init__(self, amount, prepayment=False, payment_method=None, installments=False, promotion_applied=False):
        self.__amount = amount
        self.__prepayment = prepayment
        self.__payment_method = payment_method
        self.__installments = installments
        self.__promotion_applied = promotion_applied

    # Геттеры и сеттеры
    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_prepayment(self):
        return self.__prepayment

    def set_prepayment(self, prepayment):
        self.__prepayment = prepayment

    def get_payment_method(self):
        return self.__payment_method

    def set_payment_method(self, method):
        self.__payment_method = method

    def get_installments(self):
        return self.__installments

    def set_installments(self, installments):
        self.__installments = installments

    def get_promotion_applied(self):
        return self.__promotion_applied

    def set_promotion_applied(self, promotion):
        self.__promotion_applied = promotion

    # Методы

    # Простой: вывод информации о платеже
    def show_payment_info(self):
        print(f"Платеж: {self.__amount} руб., способ: {self.__payment_method}")

    # С входным параметром: обновление суммы
    def update_amount(self, new_amount):
        self.__amount = new_amount
        print(f"Сумма платежа обновлена: {new_amount} руб.")

    # Входные и выходные: возвращает, оплатил ли клиент с акцией
    def is_promotion_applied(self):
        return self.__promotion_applied
