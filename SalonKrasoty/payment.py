# Создание класса Оплата
class Payment:
    def __init__(self, prepayment, payment_method, installment, amount):
        self._prepayment = prepayment
        self._payment_method = payment_method
        self._installment = installment
        self._amount = amount

    # Геттеры и сеттеры
    def get_prepayment(self):
        return self._prepayment

    def set_prepayment(self, prepayment):
        self._prepayment = prepayment

    def get_payment_method(self):
        return self._payment_method

    def set_payment_method(self, method):
        self._payment_method = method

    def get_installment(self):
        return self._installment

    def set_installment(self, installment):
        self._installment = installment

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    # Методы
    # Простой
    def show_payment_info(self):
        print(f"Оплата: {self._amount} руб. через {self._payment_method}")

    # Входной
    def update_amount(self, new_amount):
        self._amount = new_amount
        print(f"Сумма обновлена: {new_amount}")

    # Входные и выходные
    def is_full_payment(self):
        return not self._prepayment and not self._installment
