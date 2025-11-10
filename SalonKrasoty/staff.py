# Создание класса Персонал 
# staff.py
class Staff:
    def __init__(self, qualification, experience, friendliness, professionalism, appearance):
        self._qualification = qualification
        self._experience = experience
        self._friendliness = friendliness
        self._professionalism = professionalism
        self._appearance = appearance

    # Геттеры и сеттеры
    def get_qualification(self):
        return self._qualification

    def set_qualification(self, qualification):
        self._qualification = qualification

    def get_experience(self):
        return self._experience

    def set_experience(self, experience):
        self._experience = experience

    def get_friendliness(self):
        return self._friendliness

    def set_friendliness(self, friendliness):
        self._friendliness = friendliness

    def get_professionalism(self):
        return self._professionalism

    def set_professionalism(self, professionalism):
        self._professionalism = professionalism

    def get_appearance(self):
        return self._appearance

    def set_appearance(self, appearance):
        self._appearance = appearance

    # Методы
    # Простой
    def answer_questions(self):
        print(f"{self._qualification} отвечает на вопросы.")

    # Входными
    def update_experience(self, new_experience):
        self._experience = new_experience
        print(f"Опыт обновлен: {new_experience} лет.")

    # Входные и выходные
    def get_professional_level(self):
        if self._professionalism >= 8:
            return "Высокий уровень"
        elif self._professionalism >= 5:
            return "Средний уровень"
        else:
            return "Начинающий"
