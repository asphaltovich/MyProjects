# Создание класса клиент
class Client:
    def __init__(self, target_audience, age, gender, name, behavior):
        self._target_audience = target_audience
        self._age = age
        self._gender = gender
        self._name = name
        self._behavior = behavior

    # Геттеры и сеттеры
    def get_target_audience(self):
        return self._target_audience

    def set_target_audience(self, target):
        self._target_audience = target

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_behavior(self):
        return self._behavior

    def set_behavior(self, behavior):
        self._behavior = behavior

    # Методы
    # Простой
    def show_basic_info(self):
        print(f"Клиент: {self._name}, возраст: {self._age}")

    # С входными
    def update_behavior(self, new_behavior):
        self._behavior = new_behavior
        print(f"Поведение обновлено: {new_behavior}")

    # Входные и выходные
    def get_age_category(self):
        if self._age < 30:
            return "Молодой клиент"
        elif self._age < 50:
            return "Клиент среднего возраста"
        else:
            return "Пожилой клиент"
