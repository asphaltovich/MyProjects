# Создание класса Персонал 
class Staff:
    def __init__(self, name, qualification, experience, friendliness, professionalism, appearance):
        self.__name = name
        self.__qualification = qualification
        self.__experience = experience
        self.__friendliness = friendliness
        self.__professionalism = professionalism
        self.__appearance = appearance

    # Геттеры и сеттеры
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_qualification(self):
        return self.__qualification

    def set_qualification(self, qualification):
        self.__qualification = qualification

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience

    def get_friendliness(self):
        return self.__friendliness

    def set_friendliness(self, friendliness):
        self.__friendliness = friendliness

    def get_professionalism(self):
        return self.__professionalism

    def set_professionalism(self, professionalism):
        self.__professionalism = professionalism

    def get_appearance(self):
        return self.__appearance

    def set_appearance(self, appearance):
        self.__appearance = appearance

    # Методы

    def answer_questions(self):
        print(f"{self.__name} отвечает на вопросы.")

    # Простой: вывод информации о персонале
    def show_info(self):
        print(f"Специалист {self.__name}, квалификация: {self.__qualification}")

    # С входным параметром: обновление опыта
    def update_experience(self, new_experience):
        self.__experience = new_experience
        print(f"Опыт обновлен до {new_experience} лет.")

    # Входные и выходные: возвращает уровень профессионализма
    def get_professional_level(self):
        if self.__professionalism >= 8:
            return "Высокий уровень"
        elif self.__professionalism >= 5:
            return "Средний уровень"
        else:
            return "Начинающий"
