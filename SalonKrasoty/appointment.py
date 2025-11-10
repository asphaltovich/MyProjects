from datetime import datetime

# Создание класса Запись на приём
class Appointment:
    def __init__(self, client, service, staff, date_time):
        self.__client = client
        self.__service = service
        self.__staff = staff
        self.__date_time = date_time

    # Геттеры и сеттеры
    def get_client(self):
        return self.__client

    def set_client(self, client):
        self.__client = client

    def get_service(self):
        return self.__service

    def set_service(self, service):
        self.__service = service

    def get_staff(self):
        return self.__staff

    def set_staff(self, staff):
        self.__staff = staff

    def get_date_time(self):
        return self.__date_time

    def set_date_time(self, date_time):
        self.__date_time = date_time

    # Методы

    def change_date_time(self, new_date_time):
        self.__date_time = new_date_time
        print(f"Запись изменена на {self.__date_time}")

    def cancel(self):
        print("Запись отменена.")

    # Простой: вывод информации о приеме
    def show_info(self):
        print(f"Прием клиента {self.__client.get_name()} на {self.__service.get_description()} в {self.__date_time}")

    # С входным параметром: перенос на другую дату
    def reschedule(self, new_date_time):
        self.__date_time = new_date_time
        print(f"Запись перенесена на {self.__date_time}")

    # Входные и выходные: проверка, прошла ли дата
    def is_past(self):
        return self.__date_time < datetime.now()
