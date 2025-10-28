class File:
    def __init__(self, name, date_create, type_fail):
        self.name = name
        self.date_create = date_create
        self.type_fail = type_fail

    def display(self):
        print(f"Название файла: {self.name}")
        print(f"Дата создания файла: {self.date_create}")
        print(f"Тип файла: {self.type_fail}")

# Создаем два файла
file_a = File("ГДЗ по математике", "12.12.2022", ".docx")
file_b = File("руководство по эксплуатации клавиатуры", "12.12.2024", ".pdf")

# Вывод информации о файлах
print("Первый файл:")
file_a.display()
print("\nВторой файл:")
file_b.display()
