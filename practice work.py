class Rival:
    life = 3
    def attack(self):
        print("Ouch!")
        self.life -=1
    def checkLife(self):
        if self.life <=0:
            print("You won!")
        else:
            print(self.life)
thanos = Rival()
magneto = Rival()
thanos.attack()
thanos.attack()
thanos.attack()
thanos.checkLife()
# Атаки магнето
magneto.attack()
magneto.attack()
magneto.attack()

# Проверка жизни магнето
magneto.checkLife()
#
#



mport datetime
birthday = datetime.date(2017, 6, 1)

print(birthday)

import datetime
x = datetime.datetime.now()
print(x.year)

import datetime
x = datetime.datetime.now()

print(x.year,x.month,x.day)

import datetime
x = datetime.datetime.now()

print(x.year,x.month,x.day, x.hour, x.minute, x.second)

from datetime import date
birthday = date(2017, 6, 1)
print(birthday)

from datetime import date as h
birthday = h(2017, 6, 1)
print(birthday)

class SoyuzDocking:
    def __init__(self):
        self.distance = 1000  # начальное расстояние в метрах
        self.speed = 500  # начальная скорость в м/с
        self.fuel = 100  # запас топлива в кг

    def has_docked(self):
        return self.distance <= 0

    def perform_burn(self, burn_amount):
        # Уменьшаем топливо
        if burn_amount > self.fuel:
            burn_amount = self.fuel  # не больше имеющегося топлива
        self.fuel -= burn_amount
        # Уменьшаем скорость пропорционально потраченному топливу
        self.speed -= burn_amount
        if self.speed < 0:
            self.speed = 0  # скорость не может быть отрицательной

    def update_distance(self):
        # Обновляем расстояние, исходя из текущей скорости
        self.distance -= self.speed
        if self.distance < 0:
            self.distance = 0


# Вступительные инструкции
print("Добро пожаловать в симуляцию стыковки Союз Т-6!")
print("Ваша миссия – стыковка со станцией Салют-7.")
print("Вы можете управлять скоростью космического корабля сжигая топливо.")
print("Каждая единица сожженного топлива замедляет космический корабль на 1 м/с.")
print("Удачи экипажу!\n")

# Создаем объект корабля
docking_sequence = SoyuzDocking()

# Основной цикл игры
while not docking_sequence.has_docked():
    # 1. Вывод текущих данных
    print(f"Расстояние до Салют-7: {docking_sequence.distance} метров")
    print(f"Скорость: {docking_sequence.speed} м/с")
    print(f"Топливо: {docking_sequence.fuel} кг\n")

    # 2. Проверка - закончилось ли топливо
    if docking_sequence.fuel <= 0:
        print("Кончилось топливо!")
        print("Миссия провалена. Союз Т-6 не смог состыковаться с Салют-7.")
        break

    # 3. Проверка - ближе 11 м, возможность автопилота
    if docking_sequence.distance < 11:
        autopilot = input(
            "До станции Салют-7 осталось менее 11 метров. Активировать режим автопилота для автоматической стыковки? (да/нет): ")
        if autopilot.lower() == 'да':
            print("Автопилот активирован.")
            # Автопилот автоматически снижает скорость и завершает стыковку
            if docking_sequence.speed <= docking_sequence.distance:
                print("Стыковка подтверждена. Поздравляем экипаж!")
            else:
                print("Миссия провалена. Союз Т-6 не смог состыковаться с Салют-7.")
            break

    # 4. Запрос, сколько топлива сжечь
    try:
        burn_amount = int(input("Сколько сжечь топлива для снижения скорости: "))
        if burn_amount < 0:
            print("Некорректный ввод. Попробуйте снова.\n")
            continue
    except ValueError:
        print("Пожалуйста, введите число.\n")
        continue

    # 5. Выполняем сжигание топлива и обновление расстояния
    docking_sequence.perform_burn(burn_amount)
    docking_sequence.update_distance()

    # 6. Проверка условия завершения
    if docking_sequence.distance <= 11 and docking_sequence.speed <= docking_sequence.distance:
        print("Стыковка подтверждена. Поздравляем экипаж!")
        break
    elif docking_sequence.distance == 0:
        print("Вы достигли станции, но не подготовлены к стыковке.")
        print("Миссия провалена.")
        break
