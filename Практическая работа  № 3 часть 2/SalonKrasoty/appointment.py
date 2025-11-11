from datetime import datetime

# Создание класса Запись на приём
class Appointment:
    def __init__(self, date_time):
        self._date_time = date_time

    # Геттеры и сеттеры
    def get_date_time(self):
        return self._date_time

    def set_date_time(self, date_time):
        self._date_time = date_time
    
    # Методы
    # Простой
    def show_info(self):
        print(f"Запись на {self._date_time}")
   # Входной
    def change_date_time(self, new_date_time):
        self._date_time = new_date_time
        print(f"Дата и время изменены на {new_date_time}")

    def cancel_appointment(self):
        print(f"Запись на {self._date_time} отменена.")
        self._date_time = None
  # Входные и выходные
    def is_past(self):
        return self._date_time < datetime.now()
