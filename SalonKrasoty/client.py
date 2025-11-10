# Создание класса клиент
class Client:
    
    # Инициализация полей
    def __init__(self, name, age, gender, target_auditory, behaivour):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__target_auditory = target_auditory
        self.__behaivour = behaivour
   
#    Геттеры и сеттеры полей 
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_target_audience(self):
        return self.__target_audience

    def set_target_audience(self, target):
        self.__target_audience = target

    def get_behavior(self):
        return self.__behavior

    def set_behavior(self, behavior):
        self.__behavior = behavior
    
  # Методы
    
    # Простой: ничего не принимает, выводит информацию
    def show_info(self):
        print(f"Клиент: {self.__name}, возраст: {self.__age}, пол: {self.__gender}")

    # С входным параметром: обновляет поведение клиента
    def update_behavior(self, new_behavior):
        self.__behavior = new_behavior
        print(f"Поведение клиента обновлено на: {new_behavior}")

    # С входными и выходными: возвращает возраст в годах + сообщение
    def get_age_category(self):
        if self.__age < 30:
            return "Молодой клиент"
        elif self.__age < 50:
            return "Клиент среднего возраста"
        else:
            return "Пожилой клиент"
